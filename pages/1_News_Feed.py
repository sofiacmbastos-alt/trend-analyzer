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

    title = a.get("title") or "No title"

    summary = (
        a.get("summary")
        or a.get("description")
        or a.get("content")
        or "No summary available"
    )

    source = (
        a.get("source")
        or a.get("source_name")
        or a.get("publisher")
        or "Unknown source"
    )

    if title.lower() == "null":
        continue

    st.subheader(title)
    st.caption(f"Source: {source}")
    st.write(summary)
    st.divider()
