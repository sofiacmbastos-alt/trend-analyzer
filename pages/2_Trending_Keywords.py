import streamlit as st
import pandas as pd
from collections import Counter
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Trend Insights",
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

df = pd.read_csv("fashion_news.csv")

all_text = (
    df["titulo"].fillna("") + " " +
    df["resumo"].fillna("")
).str.lower()

text = " ".join(all_text)

words = re.findall(r'\b[a-z]+\b', text)

stop_words = {
     "the","and","for","with","that","this","from","p","s","these",
    "have","your","about","into","their","they","trend","week","everyone","now","see",
    "will","been","were","being","after","before","dress","dresses","whether","ahead",
    "over","under","while","where","which","when",
    "what","than","then","also","more","most","fashion","style","styles","trend","trends",
    "brand","brands","designer","designers",
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

st.subheader("Most Mentioned Keywords")

st.markdown(
    '<div class="section-title">Top Keywords</div>',
    unsafe_allow_html=True
)

cols = st.columns(2)

for i, (word, count) in enumerate(top_words[:8]):

    with cols[i % 4]:

        with st.container(border=True):

            st.metric(
                label=word.title(),
                value=count
            )

# ----------------------
# WORD CLOUD
# ----------------------

st.markdown(
    '<div class="section-title">Fashion Vocabulary Cloud</div>',
    unsafe_allow_html=True
)

def custom_color_func(*args, **kwargs):
    colors = [
        "#111111",  # black
        "#6E6259",  # taupe
        "#A89B8C",  # beige
        "#8B7355",  # warm brown
    ]
    import random
    return random.choice(colors)

text_for_cloud = " ".join(words)

wordcloud = WordCloud(
    width=1200,
    height=600,
    background_color="#F7F2E9",
    collocations=False
).generate(text_for_cloud)

wordcloud.recolor(color_func=custom_color_func)

fig, ax = plt.subplots(figsize=(12, 6))

ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")

st.pyplot(fig)
