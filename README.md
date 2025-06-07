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

Este projeto tem como foco o desenvolvimento de um sistema de previsão de risco de inundação utilizando técnicas de aprendizado de máquina. Ele analisa dados meteorológicos históricos de Bom Retiro do Sul, SC, para identificar padrões e condições que tipicamente precedem eventos de inundação.

O núcleo do projeto está em um Jupyter Notebook (analise_alagamentos_modelo.ipynb) onde são realizadas a análise dos dados, o treinamento e a avaliação do modelo. Os dados meteorológicos, obtidos a partir da API Open-Meteo através de um script Python dedicado (scripts/extrator_base_de_dados.py), abrangem o período de 1 de fevereiro de 2024 a 30 de junho de 2024. Este conjunto de dados inclui uma gama abrangente de variáveis horárias, tais como precipitação, temperatura a várias alturas, velocidade e direção do vento a diferentes altitudes, temperatura e humidade do solo a várias profundidades, humidade relativa, cobertura de nuvens e pressão à superfície.

As etapas de pré-processamento de dados incluem o tratamento de valores em falta utilizando o preenchimento antecipado e a conversão adequada da informação de data para a análise de séries temporais. Um aspeto fundamental do projeto é a definição de uma variável-alvo sintética, flood_risk. Esta variável binária é activada (definida para 1) quando a precipitação horária excede 5 mm e a humidade do solo a 0-1 cm de profundidade excede 0,35; caso contrário, é 0. Embora isto forneça uma definição de trabalho para o treino do modelo, reconhece-se que o conjunto de dados é desequilibrado, com muito menos instâncias de “risco de inundação”.

A Análise Exploratória de Dados (EDA) é realizada para visualizar tendências na precipitação e na humidade do solo, incluindo uma


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


