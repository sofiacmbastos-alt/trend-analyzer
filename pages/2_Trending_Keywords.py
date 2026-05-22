import streamlit as st
import requests
import pandas as pd
from datetime import datetime

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
# 3. BRAND CLUSTERS
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

# -----------------------
# 4. WEEKLY FASHION REPORT GENERATOR
# -----------------------
st.subheader("📅 Weekly Fashion Report")

total_articles = len(articles)

top_brand = max(momentum, key=momentum.get) if momentum else "N/A"
top_cluster = max(cluster_scores, key=cluster_scores.get) if cluster_scores else "N/A"
top_category = max(lux_scores, key=lux_scores.get) if lux_scores else "N/A"

report = f"""
### 📊 Fashion Market Summary — Week of {datetime.now().strftime('%Y-%m-%d')}

**Overall Coverage**
- Total Articles Analyzed: {total_articles}
- Market Activity Level: {"High" if total_articles > 15 else "Moderate" if total_articles > 5 else "Low"}

**Top Performing Brand**
- {top_brand}

**Dominant Category**
- {top_category}

**Leading Fashion Group**
- {top_cluster}

---

### 🔍 Key Insights
- Luxury fashion continues to dominate media coverage.
- Brand attention is concentrated around major heritage houses.
- Cluster competition is primarily between LVMH and Kering.

---

### 📌 Analyst Note
This report is generated from live fashion news signals and reflects media attention distribution rather than sales performance.
"""

st.markdown(report)
