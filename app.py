import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from collections import Counter
import re

st.set_page_config(
    page_title="ModeRn",
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

[data-testid="stMetric"] {
    background: rgba(255,255,255,0.9);
    border: 1px solid #E5DDD0;
    padding: 20px;
    border-radius: 18px;
    box-shadow: 0 3px 12px rgba(0,0,0,.04);
}

.subtitle {
    text-align: center;
    color: #7A7268;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 60px;
}

.hero-text {
    text-align:center;
    margin-top:25px;
    margin-bottom:60px;
}

.hero-title {
    font-size:2.5rem;
    letter-spacing:4px;
    font-family:Georgia, serif;
    color:#111111;
}

.hero-subtitle {
    text-transform:uppercase;
    letter-spacing:3px;
    color:#7A7268;
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
    "hailey bieber",
    "dua lipa",
    "kim kardashian",
    "kristin stewart",
    "taylor russell",
    "zendaya",
    "bad bunny",
    "harry styles",
    "lilly allen",
    "sydney sweeney",
    "naomi osaka",
    "justin bieber",
    "victoria beckham",
    "madonna",
    "hannah einbinder",
    "alex consani",
    "jennifer lopez",
    "kaia gerber",
    "gigi hadid",
    "jacob elordi",
    "kylie jenner",
    "timothee chalamet",
    "taylor swift",
    "ariana grande",
    "jane birkin"
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
    "louis vuitton",
    "schiaparelli",
    "lulu lemon",
    "loewe",
    "valentino",
    "ralph lauren"
    "fendi",
    "coach",
    "isabel marant",
    "havaianas",
    "uniqlo",
    "zara",
    "balenciaga",
    "manolo blahnik",
    "michael kors",
    "celine",
    "stella mccartney",
    "miu miu",
    "calvin klein"
    
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
The Mode-Rn
</div>

<div class="subtitle">
CULTURAL SIGNALS • TREND ANALYSIS • FASHION NEWS
</div>
""", unsafe_allow_html=True)

# ----------------------
# FASHION EDITORIAL LAYOUT
# ----------------------

components.html("""
<style>

.slider-container {
    position: relative;
    width: 100%;
    height: 700px;
    overflow: hidden;
    border-radius: 20px;
}

.slide {
    position: absolute;
    width: 100%;
    height: 100%;
    object-fit: cover;
    opacity: 0;
    animation: fade 15s infinite;
}

.slide:nth-child(1) {
    animation-delay: 0s;
}

.slide:nth-child(2) {
    animation-delay: 5s;
}

.slide:nth-child(3) {
    animation-delay: 10s;
}

@keyframes fade {
    0% {opacity:0;}
    10% {opacity:1;}
    30% {opacity:1;}
    40% {opacity:0;}
    100% {opacity:0;}
}

</style>

<div class="slider-container">
    <img class="slide" src="https://i.pinimg.com/736x/92/00/8c/92008c600225f042f92ab96d019eb711.jpg">
    <img class="slide" src="https://i.pinimg.com/1200x/d0/91/eb/d091eb1059b3ac344fcf056c905fb2fd.jpg">
    <img class="slide" src="https://i.pinimg.com/1200x/6b/dd/46/6bdd46e2f3ae7e5a7028847282aa10bb.jpg">
</div>
""", height=720)
# ----------------------
# TREND CARDS
# ----------------------

row1 = st.columns(3)

with row1[0]:
    st.metric("TOP TREND", top_trend)

with row1[1]:
    st.metric("BRAND LEADER", top_brand.title())

with row1[2]:
    st.metric("CULTURAL ICON", top_celeb.title())

st.markdown("<br>", unsafe_allow_html=True)

row2 = st.columns(2)

with row2[0]:
    st.metric("COLOR TREND", top_color.title())

with row2[1]:
    st.metric("STYLE TREND", top_style.title())
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
# ARTICLES
# ----------------------

st.markdown(
    '<div class="section-title">Latest Articles</div>',
    unsafe_allow_html=True
)

# Make Streamlit containers look like luxury cards
st.markdown("""
<style>
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.85);
    border: 1px solid #E5DDD0 !important;
    border-radius: 18px !important;
    box-shadow: 0 3px 12px rgba(0,0,0,.04);
    padding: 8px;
}
</style>
""", unsafe_allow_html=True)

cols = st.columns(2)

for i, (_, row) in enumerate(df.iterrows()):

    with cols[i % 2]:

        with st.container(border=True):

            st.markdown(f"### {row['titulo']}")

            st.caption(f"📰 {row['fonte']}")

            st.write(row["resumo"])

            st.link_button(
                "Read Article",
                row["link"],
                use_container_width=True
            )
