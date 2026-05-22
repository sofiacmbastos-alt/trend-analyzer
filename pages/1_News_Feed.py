import streamlit as st
import requests

st.title("DEBUG MODE")

NEWS_API_KEY = st.secrets["NEWS_API_KEY"]

url = "https://api.freenewsapi.io/v1/news"

params = {
    "topic": "fashion",
    "language": "en"
}

headers = {
    "x-api-key": NEWS_API_KEY
}

response = requests.get(url, params=params, headers=headers)

st.write("Status:", response.status_code)

data = response.json()

st.write("FULL API RESPONSE:")
st.write(data)
