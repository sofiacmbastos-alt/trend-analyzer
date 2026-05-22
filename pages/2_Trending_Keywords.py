import streamlit as st
import requests

st.title("📊 Fashion Trend Intelligence")

NEWS_API_KEY = st.secrets["NEWS_API_KEY"]

data = requests.get(
    "https://api.freenewsapi.io/v1/news",
    params={"topic": "fashion", "language": "en"},
    headers={"x-api-key": NEWS_API_KEY}
).json()

articles = data.get("articles") or data.get("data") or []

keywords = [
    "gucci", "prada", "balenciaga", "nike", "dior",
    "streetwear", "luxury", "runway", "vintage",
    "sustainable", "aesthetic"
]

# -----------------------
# DOCUMENT FREQUENCY (KEY FIX)
# -----------------------
def doc_frequency(keyword, articles):
    count = 0
    for a in articles:
        text = ((a.get("title") or "") + " " + (a.get("description") or "")).lower()
        if keyword in text:
            count += 1
    return count

scores = {}
total_docs = len(articles) or 1

for k in keywords:
    df = doc_frequency(k, articles)

    # normalize by number of articles (NOT word count)
    scores[k] = round((df / total_docs) * 100, 2)

# remove noise (VERY IMPORTANT)
filtered = {k: v for k, v in scores.items() if v > 0}

st.subheader("🔥 Active Trends (Document Frequency %)")

if not filtered:
    st.warning("No strong trend signals found. Try different keywords or more data.")
else:
    st.bar_chart(filtered)
    st.dataframe(filtered)
