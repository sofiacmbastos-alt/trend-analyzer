import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fashion Intelligence Dashboard", layout="wide")

st.title("👗 Fashion Intelligence Dashboard")

df = pd.read_csv("fashion_news.csv")

for _, row in df.iterrows():
    with st.container(border=True):
        st.subheader(row["title"])

        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(row["summary"])

        with col2:
            st.metric("Sentiment", row["sentiment"])

        st.caption(f"Source: {row['source']} | Date: {row['date']}")

        if pd.notna(row["url"]):
            st.link_button("Read Article", row["url"])
