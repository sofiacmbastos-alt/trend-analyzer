import streamlit as st
import requests

st.title("📰 Fashion News Feed")

NEWS_API_KEY = st.secrets.get("NEWS_API_KEY")

url = "https://api.freenewsapi.io/v1/news"

params = {
    "topic": "fashion",
    "language": "en"
}

headers = {
    "x-api-key": NEWS_API_KEY
}

response = requests.get(url, params=params, headers=headers)

st.write("Status Code:", response.status_code)

data = response.json()

st.write("Raw Data Preview:", data)  # DEBUG

articles = data.get("articles", [])

st.write("Articles found:", len(articles))

if not articles:
    st.warning("No articles returned. Check API key or topic.")
else:
    for article in articles[:10]:
        st.subheader(article.get("title", "No title"))
        st.write(article.get("summary", ""))
