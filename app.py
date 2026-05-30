import streamlit as st
import pandas as pd
from collections import Counter
import re

st.set_page_config(
    page_title="Fashion Intelligence Dashboard",
    layout="wide"
)

# ----------------------
# STYLING
# ----------------------

st.markdown("""
<style>

.stApp {
    background-color: #F7F2E9;
}

.main-title {
    font-size: 4rem;
    font-weight: 300;
    letter-spacing: 5px;
    text-align: center;
    color: #111111;
    margin-top: 30px;
    margin-bottom: 10px;
    font-family: Georgia, serif;
}

.subtitle {
    text-align: center;
    color: #7A7268;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 60px;
}

.metric-card {
    background: rgba(255,255,255,0.7);
    border: 1px solid #E5DDD0;
    border-radius: 18px;
    padding: 25px;
    text-align: center;
    min-height: 140px;
    box-shadow: 0 3px 10px rgba(0,0,0,0.04);
}

.metric-label {
    color: #7A7268;
    text-transform: uppercase;
    font-size: 0.8rem;
    letter-spacing: 1px;
}

.metric-value {
    margin-top: 18px;
    font-size: 1.6rem;
    font-weight: 600;
    color: #111111;
}

.section-title {
    font-size: 2rem;
    color: #111111;
    margin-top: 50px;
    margin-bottom: 25px;
    font-family: Georgia, serif;
}

.analysis-card {
    background: white;
    border-radius: 18px;
    border: 1px solid #E5DDD0;
    padding: 30px;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------
# LOAD DATA
# ----------------------

df = pd.read_csv("fashion_news.csv")

# ----------------------
# TREND EXTRACTION
# ----------------------

all_text = (
    df["titulo"].fillna("") + " " +
    df["resumo"].fillna("")
).str.lower()

text = " ".join(all_text)

colors = [
    "red","blue","green","black",
    "white","pink","yellow",
    "brown","beige","orange"
]

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

celebrities = [
    "billie eilish",
    "cara delevingne",
    "bella hadid",
    "kendall jenner",
    "hailey bieber"
]

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

    counts = {
        k:v for k,v in counts.items()
        if v > 0
    }

    if counts:
        return max(counts, key=counts.get)

    return "N/A"

top_color = most_mentioned(colors)
top_style = most_mentioned(styles)
top_brand = most_mentioned(brands)
top_celeb = most_mentioned(celebrities)

words = re.findall(r'\b[a-z]+\b', text)

stop_words = {
    "the","and","for","with","that",
    "this","from","have","your",
    "about","into","their","they",
    "will","fashion"
}

words = [
    w for w in words
    if w not in stop_words and len(w) > 4
]

top_trend = Counter(words).most_common(1)[0][0].title()

# ----------------------
# HEADER
# ----------------------

st.markdown("""
<div class="main-title">
FASHION INTELLIGENCE
</div>

<div class="subtitle">
TREND FORECASTING • BRAND MONITORING • CULTURAL SIGNALS
</div>
""", unsafe_allow_html=True)

# ----------------------
# TREND CARDS
# ----------------------

cards = [
    ("🔥 Top Trend", top_trend),
    ("🏆 Brand Leader", top_brand.title()),
    ("⭐ Influencer", top_celeb.title()),
    ("🎨 Color Trend", top_color.title()),
    ("👗 Style Trend", top_style.title())
]

cols = st.columns(5)

for col, (label, value) in zip(cols, cards):

    with col:
        with st.container(border=True):

            st.caption(label)

            st.markdown(
                f"""
                <h2 style="
                    text-align:center;
                    margin-top:15px;
                    margin-bottom:10px;
                    color:#111111;
                ">
                {value}
                </h2>
                """,
                unsafe_allow_html=True
            )
# ----------------------
# ANALYSIS
# ----------------------

st.markdown(
    '<div class="section-title">Trend Analysis</div>',
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="analysis-card">

    Current fashion coverage suggests growing momentum around
    <b>{top_trend}</b>.

    <br><br>

    <b>{top_brand.title()}</b> is currently the most visible
    fashion brand in media coverage while
    <b>{top_celeb.title()}</b> remains the strongest
    celebrity influence.

    <br><br>

    Color discussions are dominated by
    <b>{top_color.title()}</b> while style narratives
    continue to center around
    <b>{top_style.title()}</b> aesthetics.

    <br><br>

    These insights were automatically generated
    from the latest fashion media coverage.

    </div>
    """,
    unsafe_allow_html=True
)

# ----------------------
# TREND CARDS
# ----------------------

cards = [
    ("🔥 Top Trend", top_trend),
    ("🏆 Brand Leader", top_brand.title()),
    ("⭐ Influencer", top_celeb.title()),
    ("🎨 Color Trend", top_color.title()),
    ("👗 Style Trend", top_style.title())
]

cols = st.columns(5)

for col, (label, value) in zip(cols, cards):

    with col:

        with st.container(border=True):

            st.caption(label)
            st.subheader(value)
