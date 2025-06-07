import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
import sqlite3

# Setup Open-Meteo API
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Parâmetros da requisição
url = "https://historical-forecast-api.open-meteo.com/v1/forecast"
params = {
    "latitude": -29.609973745047824, # Latitude de Bom Retiro do Sul, SC
    "longitude": -51.94574601250332, # Longitude de Bom Retiro do Sul, SC
    "start_date": "2024-02-01",
    "end_date": "2024-06-30",
    "hourly": ["temperature_2m", "wind_speed_10m", "wind_direction_10m", "wind_gusts_10m", 
               "soil_temperature_0cm", "soil_moisture_0_to_1cm", "soil_moisture_1_to_3cm", 
               "soil_temperature_6cm", "wind_speed_80m",
               "precipitation", "relative_humidity_2m", "cloud_cover", "cloud_cover_low", 
               "cloud_cover_mid", "cloud_cover_high", "surface_pressure", "wind_direction_80m", 
               "wind_direction_120m", "wind_direction_180m", "wind_speed_180m", "wind_speed_120m", 
               "temperature_80m", "temperature_120m", "temperature_180m", "soil_temperature_18cm", 
               "soil_temperature_54cm", "soil_moisture_3_to_9cm", "soil_moisture_9_to_27cm", 
               "soil_moisture_27_to_81cm"],
    "timezone": "America/Sao_Paulo",
    "wind_speed_unit": "ms"
}
responses = openmeteo.weather_api(url, params=params)
response = responses[0]
hourly = response.Hourly()

# Criação do DataFrame
hourly_data = {
    "date": pd.date_range(
        start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
        end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
        freq=pd.Timedelta(seconds=hourly.Interval()),
        inclusive="left"
    )
}

# Adiciona todas as variáveis no DataFrame
columns = params["hourly"]
for idx, col in enumerate(columns):
    hourly_data[col] = hourly.Variables(idx).ValuesAsNumpy()

df = pd.DataFrame(hourly_data)

# 📦 Salvando no banco SQLite
db_path = "dados_meteorologicos.db"
conn = sqlite3.connect(db_path)
table_name = "dados_horarios"

# Criação da tabela e inserção dos dados
df.to_sql(table_name, conn, if_exists="replace", index=False)
conn.close()

print(f"✅ Dados salvos com sucesso no banco '{db_path}', tabela '{table_name}'")
