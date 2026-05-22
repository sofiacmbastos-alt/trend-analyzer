import streamlit as st
import requests
from collections import Counter

st.title("📊 Trending Keywords")

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

articles = data.get("articles", [])[:50]

text = " ".join([a.get("title", "") for a in articles]).lower()

keywords = [
    "streetwear", "luxury", "runway", "vintage",
    "sustainable", "minimalism", "aesthetic",
    "gucci", "prada", "balenciaga"
]

counts = {k: text.count(k) for k in keywords}

st.bar_chart(counts)
