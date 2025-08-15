# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# CardioAI

## CardioSync

## 👨‍🎓 Integrantes: 
- Alex da Silva Lima (RM559784)
- Johnatan Sousa Macedo Loriano (RM559546)
- Matheus Augusto Rodrigues Maia (RM560683)
- Bruno Henrique Nielsen Conter (RM560518)
- Fabio Santos Cardoso (RM560479)

## 👩‍🏫 Professores:
### Tutor(a) 
- Nome do Tutor
### Coordenador(a)
- Nome do Coordenador

## 📜 Descrição

Este repositório é dedicado ao projeto acadêmico CardioIA, desenvolvido para o curso de Inteligência Artificial da FIAP. O objetivo final do projeto é criar uma plataforma digital inteligente que simule um ecossistema de cardiologia moderna, integrando dados clínicos, modelos de Machine Learning, Visão Computacional, IoT e agentes inteligentes para auxiliar na triagem, diagnóstico, monitoramento e previsões médicas.

Este repositório foi criado com uma estrutura modular, pensando na evolução do projeto ao longo das próximas 7 fases do curso. A cada nova fase, o código-fonte e a documentação serão atualizados e expandidos.

---

### **Fase 1: Batimentos de Dados**

Nesta primeira fase, o grupo atuou como **Cientista de Dados Hospitalar**. O foco principal foi a coleta, organização e preparação de três tipos de dados fundamentais que servirão de base para o desenvolvimento dos módulos de IA.

---

### **1. Dados Numéricos (IoT)**

* **Descrição e Origem**: O dataset numérico, com mais de 100 linhas, foi compilado para simular dados de pacientes com foco em saúde cardiovascular. Ele contém variáveis como idade, sexo, pressão arterial (sistólica e diastólica), colesterol, histórico familiar de doenças cardíacas e frequência cardíaca. As informações são fictícias, criadas para a finalidade deste projeto acadêmico.

* **Link para o Dataset**: [Insira o link público do seu Google Drive/OneDrive aqui]

* **Relevância Clínica e para a IA**: A escolha dessas variáveis é estratégica para a IA, pois são indicadores-chave de risco cardiovascular. Modelos de Machine Learning podem ser treinados com esses dados para identificar padrões e prever a probabilidade de eventos cardíacos. A governança de dados é crucial aqui; a qualidade e a veracidade dos dados de entrada (mesmo que simulados) são fundamentais para garantir que os modelos de IA não gerem vieses ou diagnósticos imprecisos no futuro.

### **2. Dados Textuais (NLP)**

* **Descrição e Origem**: Foram selecionados dois artigos em formato `.txt` de fontes como SciELO para simular textos médicos. Os arquivos abordam tópicos como sintomas de doenças cardíacas, tratamentos e saúde pública relacionada à cardiologia.

* **Caminho no Repositório**: Os arquivos de texto estão localizados em `assets/docs/`.

* **Relevância Clínica e para a IA**: A análise desses textos por meio de técnicas de Processamento de Linguagem Natural (NLP) é essencial. A IA pode ser usada para:
    * **Extração de Sintomas**: Identificar termos e frases que descrevem sintomas para automatizar a triagem.
    * **Classificação de Tópicos**: Organizar a vasta literatura médica para facilitar a pesquisa e a tomada de decisão clínica.
    * **Análise de Sentimentos**: Entender a percepção do paciente ou a gravidade dos relatos de saúde em documentos como prontuários.

### **3. Dados Visuais (Visão Computacional)**

* **Descrição e Origem**: O conjunto visual inclui mais de 100 imagens que simulam exames cardiológicos, como ECGs e raio-X torácico. As imagens foram obtidas de fontes abertas e plataformas de dataset público para fins de estudo.

* **Link para as Imagens**: [Insira o link público do seu Google Drive/OneDrive aqui]

* **Relevância Clínica e para a IA**: A Visão Computacional (VC) será fundamental para o projeto. Com essas imagens, algoritmos de VC podem ser treinados para:
    * **Detecção de Padrões**: Identificar anormalidades e arritmias em ECGs.
    * **Identificação de Bordas**: Mapear a silhueta do coração em um raio-X para detectar cardiomegalia.
    * **Reconhecimento de Anomalias**: Identificar padrões que indicam doenças em exames, auxiliando a equipe médica no diagnóstico.

---

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

**Fase 1: Preparação de Dados**

1.  **Pré-requisitos**:
    * Python 3.x
    * Bibliotecas Python para análise de dados (ex: Pandas, Matplotlib, scikit-learn).
    * Git para clonar o repositório.

2.  **Instalação e Execução**:
    ```bash
    # Clone o repositório
    git clone [https://github.com/brunocorisco86/cardioai.git](https://github.com/brunocorisco86/cardioai.git)

    # Navegue até a pasta do projeto
    cd cardioai

    # Instale as dependências (se aplicável para fases futuras)
    pip install -r requirements.txt
    ```
    Nesta fase, o foco é a organização dos dados e da documentação. O código de análise será desenvolvido nas próximas etapas e adicionado na pasta `src/`.

## 🗃 Histórico de lançamentos

* 0.1.0 - 14/08/2025
    * Estrutura inicial do repositório
    * Coleta e organização dos datasets numéricos, textuais e visuais (Fase 1)
    * Criação do README.md detalhado

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
