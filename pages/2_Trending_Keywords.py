import streamlit as st
import requests
from collections import Counter

st.title("📊 Fashion Trend Intelligence")

NEWS_API_KEY = st.secrets["NEWS_API_KEY"]

url = "https://api.freenewsapi.io/v1/news"

data = requests.get(url, params={"topic": "fashion", "language": "en"},
                     headers={"x-api-key": NEWS_API_KEY}).json()

articles = data.get("articles") or data.get("data", []) or []

# split into fake time windows
mid = len(articles) // 2
today = articles[:mid]
yesterday = articles[mid:]

keywords = [
    "streetwear", "luxury", "runway", "vintage",
    "sustainable", "minimalism", "aesthetic",
    "gucci", "prada", "balenciaga", "nike"
]

def extract_counts(data_chunk):
    text = " ".join([
        (a.get("title", "") + " " + a.get("description", "")).lower()
        for a in data_chunk if isinstance(a, dict)
    ])
    return {k: text.count(k) for k in keywords}

today_counts = extract_counts(today)
yesterday_counts = extract_counts(yesterday)

# velocity calculation
trend = {}

for k in keywords:
    t = today_counts.get(k, 0)
    y = yesterday_counts.get(k, 0)

    if y == 0 and t > 0:
        trend[k] = 100  # new trend spike
    elif t == 0 and y > 0:
        trend[k] = -100  # dying trend
    else:
        trend[k] = round(((t - y) / (y + 1)) * 100, 2)

# ---------------- UI ----------------

st.subheader("🔥 Trend Velocity (Up / Down)")

for k, v in sorted(trend.items(), key=lambda x: x[1], reverse=True):
    if v > 20:
        st.write(f"📈 {k}: +{v}% (Rising)")
    elif v < -20:
        st.write(f"📉 {k}: {v}% (Declining)")
    else:
        st.write(f"➖ {k}: {v}% (Stable)")

import pandas as pd

st.subheader("🔥 Brand Heatmap")

df = pd.DataFrame({
    "brand": list(today_counts.keys()),
    "today": list(today_counts.values()),
    "yesterday": [yesterday_counts.get(k, 0) for k in today_counts.keys()]
})

df["trend_score"] = df["today"] - df["yesterday"]

st.bar_chart(df.set_index("brand")["trend_score"])
