import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Fashion Intelligence Dashboard",
    layout="wide"
)

st.title("👗 Fashion Intelligence Dashboard")

df = pd.read_csv("fashion_news.csv")

for _, row in df.iterrows():

    with st.container(border=True):

        st.subheader(row["titulo"])

        st.caption(f"📰 {row['fonte']}")

        st.write(row["resumo"])

        st.link_button(
            "🔗 Ler matéria completa",
            row["link"]
        )

        st.divider()
