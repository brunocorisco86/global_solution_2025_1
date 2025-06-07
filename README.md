# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## Nome do grupo

## 👨‍💻 Integrantes
- [Alex da Silva Lima (RM559784)](https://www.linkedin.com/in/a1exlima/)
- [Johnatan Sousa Macedo Loriano (RM559546)](https://www.linkedin.com/in/johnatanloriano/)
- [Matheus Augusto Rodrigues Maia (RM560683)](https://www.linkedin.com/in/matheus-maia-655bb1250/)
- [Bruno Henrique Nielsen Conter (RM560518)](https://www.linkedin.com/in/brunoconter/)
- [Fabio Santos Cardoso (RM560479)](https://www.linkedin.com/in/fabiosantoscardoso/)

## 👩‍🏫 Professores
- **Tutor:** [Leonardo Ruiz Orabona](https://www.linkedin.com/in/leonardoorabona/?originalSubdomain=br)  
- **Coordenador:** [André Godoi](https://www.linkedin.com/in/profandregodoi/)


## 📜 Descrição

This project focuses on developing a flood risk prediction system using machine learning techniques. It analyzes historical meteorological data for Bom Retiro do Sul, SC, to identify patterns and conditions that typically precede flood events.

The core of the project lies in a Jupyter Notebook (`analise_alagamentos_modelo.ipynb`) where data analysis, model training, and evaluation are performed. Meteorological data, sourced from the Open-Meteo API via a dedicated Python script (`scripts/extrator_base_de_dados.py`), covers the period from February 1, 2024, to June 30, 2024. This dataset includes a comprehensive range of hourly variables such as precipitation, temperature at various heights, wind speed and direction at different altitudes, soil temperature and moisture at multiple depths, relative humidity, cloud cover, and surface pressure.

Data preprocessing steps include handling missing values using forward fill and converting date information appropriately for time-series analysis. A key aspect of the project is the definition of a synthetic target variable, `flood_risk`. This binary variable is triggered (set to 1) when hourly precipitation exceeds 5mm and soil moisture at 0-1cm depth surpasses 0.35; otherwise, it is 0. While this provides a working definition for model training, it's acknowledged that the dataset is imbalanced, with far fewer "flood risk" instances.

Exploratory Data Analysis (EDA) is conducted to visualize trends in precipitation and soil moisture, including a detailed look at a specific potential flood period between April 28 and May 2, 2024. Correlations between various features and the synthetic flood risk are also examined, with precipitation showing a strong positive correlation.

For model training, a selection of features (`precipitation`, `soil_moisture_0_to_1cm`, `soil_moisture_1_to_3cm`, `relative_humidity_2m`, `surface_pressure`, `cloud_cover`) are chosen and scaled using `StandardScaler`. A Random Forest Classifier is then trained on this data, split into 80% training and 20% testing sets (stratified due to class imbalance). The model's performance is evaluated using a classification report and confusion matrix, and feature importance is also derived from the classifier.

The project also outlines a conceptual framework for an alert system, suggesting that the trained model could be used to predict flood probability on new data. Alerts could then be triggered if this probability surpasses a predefined threshold, potentially integrating with messaging services for real-time notifications. Future work could involve refining the target variable with actual flood event data and exploring other machine learning models.


## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>.github</b>: Nesta pasta ficarão os arquivos de configuração específicos do GitHub que ajudam a gerenciar e automatizar processos no repositório.

- <b>assets</b>: aqui estão os arquivos relacionados a elementos não-estruturados deste repositório, como imagens.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: aqui estão todos os documentos do projeto que as atividades poderão pedir. Na subpasta "other", adicione documentos complementares e menos importantes.

- <b>scripts</b>: Posicione aqui scripts auxiliares para tarefas específicas do seu projeto. Exemplo: deploy, migrações de banco de dados, backups.

- <b>src</b>: Todo o código fonte criado para o desenvolvimento do projeto ao longo das 7 fases.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

*Acrescentar as informações necessárias sobre pré-requisitos (IDEs, serviços, bibliotecas etc.) e instalação básica do projeto, descrevendo eventuais versões utilizadas. Colocar um passo a passo de como o leitor pode baixar o seu código e executá-lo a partir de sua máquina ou seu repositório. Considere a explicação organizada em fase.*


## 🗃 Histórico de lançamentos

* 0.5.0 - XX/XX/2024
    * 
* 0.4.0 - XX/XX/2024
    * 
* 0.3.0 - XX/XX/2024
    * 
* 0.2.0 - XX/XX/2024
    * 
* 0.1.0 - XX/XX/2024
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


