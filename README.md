# Daily Python Tasks

Este repositório contém um projeto Python que automatiza a busca diária de notícias de tecnologia usando a API da NewsAPI.

## Funcionalidades

- Busca as 5 principais notícias de tecnologia dos EUA diariamente.
- Salva os artigos no arquivo `data/latest_data.json`.
- Workflow GitHub Actions executa o script automaticamente todo dia às 9h (horário de Brasília).
- Realiza commit automático das atualizações para manter o histórico e o gráfico de contribuições ativo.

## Como usar localmente

1. Clone o repositório:

   ```bash
   git clone https://github.com/Igor-B-Lopes/daily-python-tasks.git
   cd daily-python-tasks

2. Crie um ambiente virtual e ative:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt

4. Crie um arquivo .env na raiz do projeto com sua chave da NewsAPI:

   ```bash
   NEWSAPI_KEY=sua_chave

5. Execute o script manualmente:

   ```bash
   python src/main.py

## GitHub Actions
O workflow automatizado está configurado para rodar o script diariamente e realizar commit automático das atualizações no arquivo de notícias.

Tecnologias utilizadas
Python 3.11

Requests

python-dotenv

GitHub Actions
