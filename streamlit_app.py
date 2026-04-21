import streamlit as st
import requests

API_URL = "https://stock-risk-system-611966324618.us-central1.run.app/"

st.title("📊 Stock Risk Intelligence")

if st.button("Run Analysis"):
    res = requests.get(API_URL, timeout=10)
    result = res.json()

    st.write("Decision:", result["decision"])
    st.write("Probability:", round(result["probability"], 4))
    st.write("Volatility:", round(result["volatility"], 4))