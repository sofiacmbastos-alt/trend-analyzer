import streamlit as st
import requests

st.title("📰 Fashion News Feed")

# Load API key safely
NEWS_API_KEY = st.secrets.get("NEWS_API_KEY")

if not NEWS_API_KEY:
    st.error("Missing NEWS_API_KEY in Streamlit secrets")
    st.stop()

# API request
url = "https://api.freenewsapi.io/v1/news"

params = {
    "topic": "fashion",
    "language": "en"
}

headers = {
    "x-api-key": NEWS_API_KEY
}

response = requests.get(url, params=params, headers=headers)

# Handle bad response
if response.status_code != 200:
    st.error(f"API error: {response.status_code}")
    st.write(response.text)
    st.stop()

data = response.json()

articles = data.get("articles", [])

# -----------------------
# CLEAN + FILTER ARTICLES
# -----------------------
clean_articles = []

for a in articles:
    title = a.get("title")

    # skip broken entries
    if not title or title.lower() == "null":
        continue

    clean_articles.append({
        "title": title,
        "summary": a.get("summary") or "No summary available",
        "source": a.get("source") or "Unknown source"
    })

# Show result count
st.write(f"Showing {len(clean_articles)} articles")

# -----------------------
# DISPLAY
# -----------------------
if not clean_articles:
    st.warning("No valid articles found.")
else:
    for article in clean_articles[:15]:
        st.subheader(article["title"])
        st.caption(f"Source: {article['source']}")
        st.write(article["summary"])
        st.divider()
