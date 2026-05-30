import streamlit as st
import pandas as pd
from collections import Counter
import re

df = pd.read_csv("fashion_news.csv")

all_text = (
    df["titulo"].fillna("") + " " +
    df["resumo"].fillna("")
).str.lower()

text = " ".join(all_text)

words = re.findall(r'\b[a-z]+\b', text)

stop_words = {
    "the","and","for","with","that",
    "this","from","have","your",
    "about","into","their","they",
    "will","fashion"
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
