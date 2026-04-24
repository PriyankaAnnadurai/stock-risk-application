import streamlit as st
import requests
import matplotlib.pyplot as plt

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
    data = requests.get(url).json()

    decision = data["decision"]
    probability = data["probability"] * 100
    volatility = data["volatility"] * 100

    # ---- METRICS ----
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"### Decision: {decision}")

    with col2:
        st.markdown(f"### Confidence: {probability:.2f}%")

    with col3:
        st.markdown(f"### Volatility: {volatility:.2f}%")

    st.markdown("---")

    # =========================
    # 📊 BAR CHART
    # =========================
    st.subheader("📊 Metrics Overview")

    labels = ["Confidence", "Volatility"]
    values = [probability, volatility]

    fig1, ax1 = plt.subplots()
    ax1.bar(labels, values)
    ax1.set_ylabel("Percentage")
    ax1.set_title("Model Metrics")

    st.pyplot(fig1)

    # =========================
    # 🎯 GAUGE CHART (SIMULATED)
    # =========================
    st.subheader("🎯 Confidence Gauge")

    fig2, ax2 = plt.subplots()

    # Draw semicircle
    ax2.pie(
        [probability, 100 - probability],
        startangle=180,
        counterclock=False,
        wedgeprops={'width': 0.3}
    )

    ax2.text(0, 0, f"{probability:.1f}%", ha='center', va='center', fontsize=18)
    ax2.set_aspect('equal')

    st.pyplot(fig2)

    # ---- INSIGHTS ----
    st.markdown("### 🔍 Insights")

    if decision == "BUY":
        st.success("Market looks good → Consider Buying")
    elif decision == "SELL":
        st.error("High risk → Consider Selling")
    else:
        st.warning("Market neutral → Hold position")
