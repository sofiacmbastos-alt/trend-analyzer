import streamlit as st
import requests

st.title("📰 Fashion News Feed")

NEWS_API_KEY = st.secrets["NEWS_API_KEY"]

url = "https://api.freenewsapi.io/v1/news"

params = {
    "topic": "fashion",
    "language": "en"
}

headers = {
    "x-api-key": NEWS_API_KEY
}

response = requests.get(url, params=params, headers=headers)
data = response.json()

# -----------------------
# SAFE EXTRACTION
# -----------------------
raw = data.get("data") or data.get("articles") or data.get("results")

if isinstance(raw, dict):
    articles = raw.get("news", []) or raw.get("articles", [])
elif isinstance(raw, list):
    articles = raw
else:
    articles = []

# -----------------------
# CLEAN ARTICLES
# -----------------------
clean_articles = []

for a in articles:
    if not isinstance(a, dict):
        continue

    title = a.get("title")

    if not title or title.lower() == "null":
        continue

    clean_articles.append({
        "title": title,
        "summary": a.get("summary") or "No summary available",
        "source": a.get("source") or "Unknown source"
    })

# -----------------------
# UI
# -----------------------
st.write(f"Showing {len(clean_articles)} articles")

if not clean_articles:
    st.warning("No articles found (check API response structure).")
else:
    for article in clean_articles[:15]:
        st.subheader(article["title"])
        st.caption(article["source"])
        st.write(article["summary"])
        st.divider()
