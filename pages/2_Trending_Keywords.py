import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.title("Luxury Fashion Intelligence Dashboard")

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
    "Haute Couture": ["chanel", "dior", "valentino", "schiaparelli", "givenchy", "jean paul gaultier", "fendi", "maison margiela", "balenciaga"],
    "Leather Goods": ["louis vuitton", "hermes", "gucci", "prada", "goyard", "bottega veneta", "loewe", "delvaux", "moynat", "celine", "ferragamo", "fendi", "saint laurent", "balenciaga", "dior", "chanel", "valextra", "berluti", "rimowa", "mulberry", "coach", "tods", "mcm", "longchamp", "etro", "tom ford", "valentino", "bvlgari", "moreau paris", "mark cross", "launer london"],
    "Contemporary Luxury": ["balenciaga", "loewe", "bottega veneta", "saint laurent", "jacquemus", "the row", "miu miu", "celine", "alaia", "tom ford", "amiri", "khaite", "jil sander", "acne studios", "courreges", "coperni", "diesel", "off-white", "marine serre", "fear of god", "ann demeulemeester", "dries van noten", "toteme", "loro piana", "brunello cucinelli", "gabriela hearst", "proenza schouler",
"a.p.c.", "stone island", "moncler", "miu miu", "marc jacobs", "celine", "kenzo", "emilio pucci", "chloe"] ,
    "Avant-Garde": ["maison margiela", "rick owens", "comme des garcons", "alexander mcqueen", "mcqueen", "jimmy choo", "chrome hearts", "yohji yamamoto", "issey miyake", "ann demeulemeester", "julius", "undercover", "vetements", "craig green", "boris bidjan saberi", "guidi", "carol christian poell", "raf simons", "haider ackermann", "marine serre", "demobaza", "takahiromiyashita the soloist", "number (n)ine", "alyx", "dark shadow", "hussein chalayan", "iris van herpen", "junya watanabe", "noir kei ninomiya", "song for the mute", "damir doma", "miharayasuhiro", "attachment", "label under construction"] ,
    "Heritage Luxury": ["burberry", "fendi", "armani", "versace", "chanel", "dior", "saint laurent", "cartier", "givenchy", "louis vuitton", "lv", "hermes", "prada", "goyard", "lanvin", "bvlgari", "ferragamo", "celine", "loro piana", "brunello cucinelli", "valentino", "loewe", "bottega veneta", "gucci", "balmain", "vacheron constantin", "patek philippe", "rolex", "van cleef & arpels", "berluti", "tods", "zegna", "moynat", "delvaux", "dunhill", "etro", "missoni", "moncler", "pomellato", "chaumet", "piaget", "rimowa", "jaeger-lecoultre", "bally", "longchamp", "launer london"],
    "Premium Lifestyle": ["tommy hilfiger", "polo ralph lauren", "ralph lauren", "boss", "hugo boss", "lacoste", "coach", "michael kors", "tory burch", "kate spade", "longchamp", "gant", "brooks brothers", "calvin klein", "armani exchange", "emporio armani", "allsaints", "theory", "reiss", "sandro", "maje", "club monaco", "ted baker", "paul smith", "vivienne westwood", "diesel", "true religion", "dkny", "stuart weitzman", "furla", "tocca"]
}

lux_scores = {
    k: sum(text.count(b) for b in brands)
    for k, brands in luxury.items()
}

st.subheader("Luxury Sub-Categories")
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

st.subheader("House Momentum")
st.bar_chart(momentum)

# -----------------------
# 3. BRAND CLUSTERS
# -----------------------
clusters = {

"LVMH": ["louis vuitton", "dior", "fendi", "celine", "loewe", "givenchy", "kenzo", "berluti", "rimowa", "loro piana", "emilio pucci", "marc jacobs", "patou", "fred", "bvlgari", "tag heuer", "hublot", "zenith", "tiffany & co"],

"Kering": ["gucci", "saint laurent", "balenciaga", "bottega veneta", "mcqueen", "alexander mcqueen", "brioni", "boucheron", "pomellato", "qeelin", "ginori 1735"],

"Richemont": ["cartier", "van cleef & arpels", "dunhill", "delvaux", "alaia", "chloe", "montblanc", "piaget", "vacheron constantin", "jaeger-lecoultre", "iwc", "panerai"],

"Prada Group": ["prada", "miu miu", "churchs", "car shoe", "marchesi 1824"],

"Chanel": ["chanel"],

"Hermes": ["hermes"],

"Capri Holdings": ["versace", "jimmy choo", "michael kors"],

"OTB Group": ["maison margiela", "marni", "jil sander",
"diesel"],

"Tapestry": ["coach", "kate spade", "stuart weitzman"],

"Moncler Group": ["moncler", "stone island"],

"Independent Luxury": [ "rick owens", "comme des garcons", "yohji yamamoto", "issey miyake",
"the row", "jacquemus", "tom ford", "valentino", "goyard", "brunello cucinelli", "zegna", "moynat", "launer london", "chrome hearts"]
} 

cluster_scores = {
    k: sum(text.count(b) for b in brands)
    for k, brands in clusters.items()
}

st.subheader("Fashion Conglomerates")
st.bar_chart(cluster_scores)

df = pd.DataFrame({
    "Cluster": list(cluster_scores.keys()),
    "Mentions": list(cluster_scores.values())
})

st.dataframe(df)

# -----------------------
# 4. WEEKLY FASHION REPORT GENERATOR
# -----------------------
st.subheader("Weekly Fashion Report")

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

### 📌 Note from the developers
This report is generated from live fashion news signals and reflects media attention distribution rather than sales performance.
"""

st.markdown(report)
