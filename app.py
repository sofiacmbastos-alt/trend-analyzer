import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Fashion Intelligence Dashboard",
    layout="wide"
)

st.title("👗 Fashion Intelligence Dashboard")

df = pd.read_csv("fashion_news.csv")

cols = st.columns(2)

for i, (_, row) in enumerate(df.iterrows()):

    with cols[i % 2]:
        with st.container(border=True):

            st.subheader(row["titulo"])

            st.markdown(
                f"**Fonte:** {row['fonte']}"
            )

            st.write(row["resumo"])

            st.link_button(
                "Ler mais",
                row["link"],
                use_container_width=True
            )
