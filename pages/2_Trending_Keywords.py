import streamlit as st
import pandas as pd
from collections import Counter
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

df = pd.read_csv("fashion_news.csv")

all_text = (
    df["titulo"].fillna("") + " " +
    df["resumo"].fillna("")
).str.lower()

text = " ".join(all_text)

words = re.findall(r'\b[a-z]+\b', text)

stop_words = {
     "the","and","for","with","that","this","from","p","s",
    "have","your","about","into","their","they","trend","week","everyone","now","see",
    "will","been","were","being","after","before",
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

st.dataframe(
    pd.DataFrame(
        top_words,
        columns=["Keyword", "Mentions"]
    )
)

# ----------------------
# WORD CLOUD
# ----------------------

st.subheader("Fashion Vocabulary Cloud")

def custom_color_func(*args, **kwargs):
    colors = [
        "#111111",  # black
        "#6E6259",  # taupe
        "#A89B8C",  # beige
        "#8B7355",  # warm brown
    ]
    import random
    return random.choice(colors)

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
