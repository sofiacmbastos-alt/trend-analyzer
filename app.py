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

.stTextInput input {
    background: white;
    border: 1px solid #E5DDD0;
    border-radius: 30px;
    padding: 16px;
    font-size: 18px;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,255,255,0.85);
    border: 1px solid #E5DDD0 !important;
    border-radius: 24px !important;
    box-shadow: 0 3px 12px rgba(0,0,0,.04);
    padding: 20px;
}

.stButton button {
    background: #111111;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6rem 1.2rem;
}

.stButton button:hover {
    background: #333333;
}

</style>
""", unsafe_allow_html=True)

# ----------------------
# LOAD DATA
# ----------------------

df = pd.read_csv("merged.csv")

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
    width: 900px;      /* smaller width */
    height: 600px;
    margin: auto;
    overflow: hidden;
    border-radius: 20px;
}

.slide {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;   /* use contain if you want no cropping */
    opacity: 0;
    animation: fade 15s infinite;
}

.slide:nth-child(1) { animation-delay: 0s; }
.slide:nth-child(2) { animation-delay: 5s; }
.slide:nth-child(3) { animation-delay: 10s; }

@keyframes fade {
    0% { opacity: 0; }
    10% { opacity: 1; }
    30% { opacity: 1; }
    40% { opacity: 0; }
    100% { opacity: 0; }
}

</style>

<div class="slider-container">
    <img class="slide" src="https://i.pinimg.com/1200x/28/dd/36/28dd360f47a9eb030f249b1a0b780641.jpg">
    <img class="slide" src="https://i.pinimg.com/1200x/d0/91/eb/d091eb1059b3ac344fcf056c905fb2fd.jpg">
    <img class="slide" src="https://i.pinimg.com/1200x/03/13/05/031305344c599ac801c4b739b7f8c357.jpg">
</div>
""", height=420)

# ----------------------
# ARTICLE SEARCH
# ----------------------

# ----------------------
# ARTICLE SEARCH
# ----------------------

with st.container(border=True):

    st.markdown(
        "### Search Articles"
    )

    col1, col2 = st.columns([3,1])

    with col1:
        search = st.text_input(
            "",
            placeholder="Search brands, celebrities, trends, sustainability..."
        )

    with col2:
        sources = ["All Sources"] + sorted(
            df["fonte"].dropna().unique().tolist()
        )

        source_filter = st.selectbox(
            "Source",
            sources
        )
        
# Apply filters

filtered_df = df.copy()

if search.strip():

    filtered_df = filtered_df[
        filtered_df["titulo"].fillna("").str.contains(
            search,
            case=False,
            na=False
        )
        |
        filtered_df["resumo"].fillna("").str.contains(
            search,
            case=False,
            na=False
        )
    ]

if source_filter != "All Sources":

    filtered_df = filtered_df[
        filtered_df["fonte"] == source_filter
    ]

if search.strip():

    st.markdown(
        f"### Results for: **{search}**"
    )
    
st.caption(f"{len(filtered_df)} articles found")

# ----------------------
# LATEST ARTICLES
# ----------------------

st.markdown(
    '<div class="section-title">Latest Articles</div>',
    unsafe_allow_html=True
)

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

for i, (_, row) in enumerate(filtered_df.iterrows()):

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
