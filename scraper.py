import feedparser
import pandas as pd

# Fontes de notícias (RSS)
feeds = [
    ("Vogue", "https://www.vogue.com/"),
    ("Elle", "https://www.elle.com/"),
    ("I-d", "https://i-d.co/"),
    ("Harper's Bazaar", "https://www.harpersbazaar.com/")
]

dados = []

for fonte, url in feeds:
    feed = feedparser.parse(url)

    for noticia in feed.entries:
        dados.append({
            "titulo": noticia.get("title", ""),
            "fonte": fonte,
            "resumo": noticia.get("summary", ""),
            "link": noticia.get("link", "")
        })

# Cria tabela
df = pd.DataFrame(dados)

# Remove duplicados
df = df.drop_duplicates(subset=["titulo"])

# Salva CSV
df.to_csv("fashion_news.csv", index=False, encoding="utf-8-sig")

print(f"{len(df)} notícias salvas em fashion_news.csv")
