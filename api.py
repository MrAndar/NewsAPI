import requests
import streamlit as st

API_KEY = "INSERT_YOUR_API_KEY_HERE"
url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={API_KEY}"

request = requests.get(url)
content = request.json()

# Streamlit webapp
st.set_page_config(layout="wide")
st.title("News API - webapp")
col1, col2 = st.columns([1.5, 0.5])

for article in content["articles"]:
    with col1:
        st.subheader(article["title"])
        st.text(article["description"])
        st.text(f"Author: {article["author"]}")
        st.write(f"[Continue reading...]({article["url"]})")
    with col2:
        try:
            st.image(article["urlToImage"], width=300)
        except:
            st.text("No image available")
