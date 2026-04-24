import streamlit as st
import requests

# Page config
st.set_page_config(page_title="Stock Risk Intelligence", layout="wide")

# ---- CUSTOM CSS ----
st.markdown("""
<style>
.main {
    background-color: #f5f7fb;
}
.title {
    font-size: 40px;
    font-weight: bold;
}
.card {
    padding: 20px;
    border-radius: 12px;
    background-color: white;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}
.metric {
    font-size: 28px;
    font-weight: bold;
}
.subtext {
    color: gray;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown('<div class="title">📊 Stock Risk Intelligence</div>', unsafe_allow_html=True)
st.write("Get real-time insights on market risk and investment decisions.")

# ---- BUTTON ----
if st.button("🚀 Run Analysis"):
    url = "https://stock-risk-system-611966324618.us-central1.run.app"
    response = requests.get(url)
    data = response.json()

    decision = data["decision"]
    probability = data["probability"] * 100
    volatility = data["volatility"] * 100

    # ---- METRICS ROW ----
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        color = "orange" if decision == "HOLD" else "green" if decision == "BUY" else "red"
        st.markdown(f"<div class='metric' style='color:{color}'>{decision}</div>", unsafe_allow_html=True)
        st.markdown("<div class='subtext'>Decision</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"<div class='metric'>{probability:.2f}%</div>", unsafe_allow_html=True)
        st.markdown("<div class='subtext'>Model Confidence</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f"<div class='metric'>{volatility:.2f}%</div>", unsafe_allow_html=True)
        st.markdown("<div class='subtext'>Market Volatility</div>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # ---- EXPLANATION ----
    st.markdown("### 🧠 Risk Decision Overview")

    if decision == "BUY":
        st.success("The model suggests a BUY. Market conditions look favorable.")
    elif decision == "SELL":
        st.error("The model suggests a SELL. Risk is high.")
    else:
        st.warning("The model suggests HOLD. Market is neutral, wait for better signals.")

    # ---- INSIGHTS ----
    st.markdown("### 🔍 Key Insights")

    st.write(f"• **Confidence:** {probability:.2f}% → Moderate certainty")
    st.write(f"• **Volatility:** {volatility:.2f}% → Market stability indicator")
    st.write(f"• **Decision:** {decision} → Recommended action")

    st.info("⚠️ This is not financial advice. Do your own research before investing.")
