from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

API_KEY = os.getenv("NEWSAPI_KEY")
NEWS_URL = (
    "https://newsapi.org/v2/top-headlines?"
    "category=technology&language=en&country=us&pageSize=5"
)

def fetch_tech_news():
    headers = {"Authorization": API_KEY}
    response = requests.get(NEWS_URL, headers=headers)
    response.raise_for_status()
    data = response.json()
    return data.get("articles", [])

def save_data(data, filename="data/latest_data.json"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def main():
    print("Buscando notícias de tecnologia...")
    try:
        articles = fetch_tech_news()
        save_data(articles)
        print(f"Salvas {len(articles)} notícias em 'data/latest_data.json'")
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article['title']}")
    except Exception as e:
        print("Erro ao buscar notícias:", e)

if __name__ == "__main__":
    main()
