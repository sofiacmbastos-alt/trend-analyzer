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

    # CARD UI
    with st.container():
        st.markdown(
            f"""
            <div style="
                padding: 15px;
                border-radius: 12px;
                border: 1px solid #ddd;
                margin-bottom: 12px;
                background-color: #111;
                color: white;
            ">
                <h4 style="margin-bottom:5px;">{title}</h4>
                <p style="font-size:12px; color:gray;">{source}</p>
                <p style="font-size:14px;">{summary}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
