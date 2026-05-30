import streamlit as st
import pandas as pd
from collections import Counter
import re

st.set_page_config(
    page_title="Fashion Intelligence Dashboard",
    layout="wide"
)

# ----------------------
# LOAD DATA
# ----------------------
df = pd.read_csv("fashion_news.csv")

# ----------------------
# SIMPLE TREND EXTRACTION
# ----------------------

all_text = (
    df["titulo"].fillna("") + " " +
    df["resumo"].fillna("")
).str.lower()

text = " ".join(all_text)

# Colors
colors = [
    "red", "blue", "green", "black",
    "white", "pink", "yellow",
    "brown", "beige", "orange"
]

# Styles
styles = [
    "minimalist",
    "minimalism",
    "streetwear",
    "vintage",
    "summer",
    "boho",
    "luxury",
    "casual",
    "elegant"
]

# Celebrities
celebrities = [
    "billie eilish",
    "cara delevingne",
    "bella hadid",
    "kendall jenner",
    "hailey bieber"
]

# Brands
brands = [
    "balenciaga",
    "gucci",
    "prada",
    "dior",
    "chanel",
    "zara",
    "h&m",
    "versace",
    "louis vuitton"
]

def most_mentioned(items):
    counts = {
        item: text.count(item.lower())
        for item in items
    }

    counts = {k:v for k,v in counts.items() if v > 0}

    if counts:
        return max(counts, key=counts.get)

    return "N/A"

top_color = most_mentioned(colors)
top_style = most_mentioned(styles)
top_brand = most_mentioned(brands)
top_celeb = most_mentioned(celebrities)

# Most common word
words = re.findall(r'\b[a-z]+\b', text)

stop_words = {
    "the","and","for","with","that",
    "this","from","have","your","about",
    "into","their","they","will","fashion"
}

words = [w for w in words if w not in stop_words and len(w) > 4]

top_trend = Counter(words).most_common(1)[0][0].title()

# ----------------------
# HEADER
# ----------------------

st.title("👗 Fashion Intelligence Dashboard")

# ----------------------
# KPI CARDS
# ----------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🔥 Top Trend", top_trend)

with col2:
    st.metric("🏆 Most Mentioned Brand", top_brand.title())

with col3:
    st.metric("⭐ Most Influential Celebrity", top_celeb.title())

col4, col5 = st.columns(2)

with col4:
    st.metric("🎨 Trending Color", top_color.title())

with col5:
    st.metric("👗 Trending Style", top_style.title())

# ----------------------
# AI ANALYSIS
# ----------------------

st.subheader("📊 Trend Analysis")

st.info(
    f"""
Current fashion coverage suggests growing interest around **{top_trend}**.

The most discussed brand is **{top_brand.title()}** while
**{top_celeb.title()}** appears as the strongest celebrity influence.

Color trends are leaning toward **{top_color.title()}**
and style conversations are centered around
**{top_style.title()}**.

These insights were generated automatically from the latest
fashion news articles.
"""
)

# ----------------------
# ARTICLES
# ----------------------

st.subheader("📰 Latest Articles")

cols = st.columns(2)

for i, (_, row) in enumerate(df.iterrows()):

    with cols[i % 2]:

        with st.container(border=True):

            st.markdown(
                f"### {row['titulo']}"
            )

            st.caption(
                f"📰 {row['fonte']}"
            )

            st.write(row["resumo"])

            st.link_button(
                "Read Article",
                row["link"],
                use_container_width=True
            )
