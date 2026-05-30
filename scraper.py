import feedparser
import pandas as pd

feeds = [
    ("Vogue", "https://www.vogue.com/feed/rss"),
    ("ELLE", "https://www.elle.com/rss/fashion.xml"),
]

dados = []

for fonte, url in feeds:
    try:
        feed = feedparser.parse(url)

        for noticia in feed.entries:
            dados.append({
                "titulo": noticia.get("title", ""),
                "fonte": fonte,
                "resumo": noticia.get("summary", ""),
                "link": noticia.get("link", "")
            })

        print(f"{fonte}: OK")

    except Exception as e:
        print(f"Erro em {fonte}: {e}")

df = pd.DataFrame(dados)

df = df.drop_duplicates(subset=["titulo"])

df.to_csv(
    "fashion_news.csv",
    index=False,
    encoding="utf-8-sig"
)

print(f"{len(df)} notícias salvas.")


