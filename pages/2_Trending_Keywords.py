import streamlit as st
import requests
from collections import Counter

st.title("📊 Fashion Trend Intelligence")

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

articles = (
    data.get("articles")
    or data.get("data", [])
    or data.get("results", [])
)

# combine text
text = " ".join([
    (a.get("title", "") + " " + a.get("description", "")).lower()
    for a in articles
    if isinstance(a, dict)
])

# base keywords
keywords = [
    "streetwear", "luxury", "runway", "vintage",
    "sustainable", "minimalism", "aesthetic",
    "gucci", "prada", "balenciaga", "dior", "nike"
]

# frequency count
counts = Counter()

for kw in keywords:
    counts[kw] = text.count(kw)

# -----------------------
# TREND SCORE (upgrade)
# -----------------------
total_mentions = sum(counts.values()) or 1

trend_scores = {
    k: round((v / total_mentions) * 100, 2)
    for k, v in counts.items()
}

# sort
sorted_trends = dict(
    sorted(trend_scores.items(), key=lambda x: x[1], reverse=True)
)

st.subheader("🔥 Emerging Fashion Trends (Score %)")

st.bar_chart(sorted_trends)

st.write("### Trend Breakdown")
st.dataframe(sorted_trends)
