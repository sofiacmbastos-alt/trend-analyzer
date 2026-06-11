import streamlit as st
import pandas as pd
from collections import Counter
import re

st.set_page_config(
    page_title="ModeRn Intelligence",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: #F7F2E9;
}

.page-title {
    font-size: 3rem;
    font-weight: 300;
    letter-spacing: 4px;
    text-align: center;
    color: #111111;
    margin-top: 30px;
    margin-bottom: 10px;
    font-family: Georgia, serif;
}

.page-subtitle {
    text-align: center;
    color: #7A7268;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 50px;
}

.section-title {
    font-size: 1.8rem;
    color: #111111;
    margin-top: 40px;
    margin-bottom: 20px;
    font-family: Georgia, serif;
}

.keyword-card {
    background: rgba(255,255,255,0.85);
    border: 1px solid #E5DDD0;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 3px 12px rgba(0,0,0,.04);
}

</style>
""", unsafe_allow_html=True)

df = pd.read_csv("merged.csv")

all_text = (
    df["titulo"].fillna("") + " " +
    df["resumo"].fillna("")
).str.lower()

text = " ".join(all_text)

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
    "jane birkin",
    "emma watson",
    "gracie abrams",
    "katie holmes",
    "sarah pidgeon",
    "lilly collins",
    "naomi osaka",
    "jung kook",
    "rihanna",
    "aubrey plaza"
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
    "ralph lauren",
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

st.image(
    "IMG_6592.jpg",
    use_container_width=True
)

st.markdown("""
<div class="page-title">
MODE-RN INTELLIGENCE
</div>

<div class="page-subtitle">
Keyword Intelligence • Media Signals • Trend Forecasting
</div>
""", unsafe_allow_html=True)

words = re.findall(r'\b[a-z]+\b', text)

stop_words = {
     "the","and","for","with","that","this","from","p","s","these",
    "have","your","about","into","their","they","trend","week","everyone","now","see",
    "will","been","were","being","after","before","dress","dresses","whether","ahead",
    "over","under","while","where","which","when",
    "what","than","then","also","more","most","fashion","style","styles","trend","trends",
    "brand","brands","designer","designers","https","tried","start",
    "collection","collections",
    "season","seasons",
    "show","shows",
    "runway","week",
    "spring","summer","fall","winter",
    "look","looks",
    "wear","wearing","wears",
    "latest","new","news",
    "launch","launched",
    "industry","market",
    "retail","retailer",
    "global",
    "said","says","according",
    "including","include",
    "featuring","first","today","year",
    "years","time","times",
    "could","would","should",
    "many","much","make","made",
    "like","just","still","even","bazaar",
    "wwd","business","magazine",
    "editor","editors"
}

words = [w for w in words if w not in stop_words and len(w) > 4]

top_words = Counter(words).most_common(20)


# ----------------------
# TREND SNAPSHOT
# ----------------------


snapshot = st.columns(4)

with snapshot[0]:
    st.metric("TOP TREND", top_trend)

with snapshot[1]:
    st.metric("BRAND LEADER", top_brand.title())

with snapshot[2]:
    st.metric("CULTURAL ICON", top_celeb.title())

with snapshot[3]:
    st.metric("COLOR TREND", top_color.title())

    
st.markdown(
    '<div class="section-title">Top Keywords</div>',
    unsafe_allow_html=True
)

cols = st.columns(2)

for i, (word, count) in enumerate(top_words[:8]):

    with cols[i % 2]:

        with st.container(border=True):

            st.metric(
                label=word.title(),
                value=count
            )

st.markdown(
    '<div class="section-title">Source Analysis</div>',
    unsafe_allow_html=True
)

source_counts = (
    df["fonte"]
    .value_counts()
    .head(10)
)

st.bar_chart(source_counts)
