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

data = requests.get(url, params=params, headers=headers).json()

articles = data.get("articles", [])[:20]

for a in articles:
    st.subheader(a.get("title"))
    st.write(a.get("summary", ""))
