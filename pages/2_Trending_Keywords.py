import streamlit as st
import requests
import pandas as pd

st.title("💎 Luxury Fashion Intelligence Dashboard")

# -----------------------
# LOAD DATA
# -----------------------
NEWS_API_KEY = st.secrets["NEWS_API_KEY"]

data = requests.get(
    "https://api.freenewsapi.io/v1/news",
    params={"topic": "fashion", "language": "en"},
    headers={"x-api-key": NEWS_API_KEY}
).json()

articles = data.get("articles") or data.get("data") or []

text = " ".join([
    ((a.get("title") or "") + " " + (a.get("description") or "")).lower()
    for a in articles if isinstance(a, dict)
])

# -----------------------
# 1. LUXURY SUB-CATEGORIES
# -----------------------
luxury = {
    "Haute Couture": ["chanel", "dior", "valentino", "schiaparelli"],
    "Leather Goods": ["louis vuitton", "hermes", "gucci", "prada"],
    "Contemporary Luxury": ["balenciaga", "loewe", "bottega veneta", "saint laurent"],
    "Avant-Garde": ["maison margiela", "rick owens", "comme des garcons"],
    "Heritage Luxury": ["burberry", "fendi", "armani", "versace"]
}

lux_scores = {
    k: sum(text.count(b) for b in brands)
    for k, brands in luxury.items()
}

st.subheader("💎 Luxury Sub-Categories")
st.bar_chart(lux_scores)

# -----------------------
# 2. HOUSE MOMENTUM
# -----------------------
houses = {
    "Chanel": ["chanel"],
    "Dior": ["dior"],
    "Louis Vuitton": ["louis vuitton"],
    "Gucci": ["gucci"],
    "Prada": ["prada"],
    "Balenciaga": ["balenciaga"]
}

momentum = {
    k: sum(text.count(b) for b in brands)
    for k, brands in houses.items()
}

st.subheader("📈 House Momentum")
st.bar_chart(momentum)

# -----------------------
# 3. RUNWAY vs CELEBRITY SPLIT
# -----------------------
runway_keywords = ["runway", "fashion week", "collection", "show"]
celebrity_keywords = ["wore", "outfit", "spotted", "look"]

runway_score = sum(text.count(k) for k in runway_keywords)
celebrity_score = sum(text.count(k) for k in celebrity_keywords)

split = {
    "Runway": runway_score,
    "Celebrity": celebrity_score
}

st.subheader("🧵 Runway vs 🌟 Celebrity")
st.bar_chart(split)

# -----------------------
# 4. MEDIA TYPE CLASSIFICATION
# -----------------------
media = {
    "Editorial": runway_score,
    "Celebrity": celebrity_score,
    "Commercial": text.count("campaign") + text.count("ad")
}

st.subheader("📰 Media Type Split")
st.bar_chart(media)

# -----------------------
# 5. LUXURY DOMINANCE SCORE (LDS)
# -----------------------
total_luxury = sum(lux_scores.values()) or 1
lds = (total_luxury / len(articles)) * 100 if articles else 0

st.subheader("💰 Luxury Dominance Score (LDS)")
st.metric("Luxury Coverage %", f"{lds:.2f}%")

# -----------------------
# 6. BRAND CLUSTERS
# -----------------------
clusters = {
    "LVMH": ["louis vuitton", "dior", "fendi"],
    "Kering": ["gucci", "balenciaga", "saint laurent", "bottega veneta"]
}

cluster_scores = {
    k: sum(text.count(b) for b in brands)
    for k, brands in clusters.items()
}

st.subheader("🏢 Fashion Conglomerates")
st.bar_chart(cluster_scores)

df = pd.DataFrame({
    "Cluster": list(cluster_scores.keys()),
    "Mentions": list(cluster_scores.values())
})

st.dataframe(df)
