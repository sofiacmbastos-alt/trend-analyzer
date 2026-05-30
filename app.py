import streamlit as st
import pandas as pd

st.title("Fashion Intelligence Dashboard")

df = pd.read_csv("fashion_news.csv")

st.dataframe(df)
