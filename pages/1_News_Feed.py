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

    source = (
        a.get("source")
        or a.get("source_name")
        or a.get("publisher")
        or ""
    )

    summary = (
        a.get("description")
        or a.get("content")
        or ""
    )

    st.subheader(title)

    if source:
        st.caption(source)

    # only show summary if it actually exists
    if summary:
        st.write(summary)

    st.divider()
