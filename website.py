import streamlit as st
import requests
from groq import Groq

# -----------------------
# LOAD API KEYS SECURELY
# -----------------------
NEWS_API_KEY = st.secrets["NEWS_API_KEY"]
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

st.title("Fashion Trend Tracker")

# -----------------------
# FETCH FASHION NEWS
# -----------------------
url = "https://api.freenewsapi.io/v1/news"

params = {
    "topic": "fashion",
    "language": "en"
}

headers = {
    "x-api-key": NEWS_API_KEY
}

response = requests.get(url, params=params, headers=headers)
data = response.json()

articles = data.get("articles", [])[:10]

# -----------------------
# NEWS FEED UI
# -----------------------
st.header("Latest Fashion News")

for article in articles:
    st.subheader(article.get("title", "No title"))
    st.write(article.get("summary", ""))

# -----------------------
# BUILD AI CONTEXT
# -----------------------
context = "\n".join([
    article.get("title", "")
    for article in articles
])

# -----------------------
# AI PROMPT
# -----------------------
prompt = f"""
Summarize today's fashion trends from these headlines:

{context}

Focus on:
- aesthetics
- luxury fashion
- streetwear
- runway trends
"""

# -----------------------
# GROQ AI CALL
# -----------------------
completion = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

summary = completion.choices[0].message.content

# -----------------------
# DISPLAY AI SUMMARY
# -----------------------
st.header("AI Fashion Summary")
st.write(summary)
