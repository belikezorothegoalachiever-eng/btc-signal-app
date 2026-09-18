import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Quotex Signal Analyzer",
    page_icon="📊",
    layout="centered"
)

st.title("📊 QUOTEX SIGNAL ANALYZER")
st.caption("Screenshot-Based Binary Signal Research Tool")

st.divider()

# =========================
# MARKET SETTINGS
# =========================

st.subheader("Market Settings")

asset = st.text_input(
    "Asset",
    placeholder="Example: EUR/USD, BTC/USD, GBP/JPY"
)

timeframe = st.selectbox(
    "Chart Timeframe",
    ["1 Minute", "5 Minutes", "15 Minutes", "30 Minutes", "1 Hour"]
)

expiry = st.selectbox(
    "Trade Expiry",
    ["1 Minute", "2 Minutes", "3 Minutes", "5 Minutes"]
)

st.divider()

# =========================
# RISK SETTINGS
# =========================

st.subheader("Risk Settings")

capital = st.number_input(
    "Account Capital ($)",
    min_value=1.0,
    value=5000.0,
    step=100.0
)

normal_risk = st.number_input(
    "Normal Risk ($)",
    min_value=1.0,
    value=50.0,
    step=1.0
)

max_risk = st.number_input(
    "Maximum Risk ($)",
    min_value=1.0,
    value=80.0,
    step=1.0
)

st.divider()

# =========================
# SCREENSHOT
# =========================

st.subheader("📷 Upload Quotex Screenshot")

uploaded_file = st.file_uploader(
    "Upload your chart screenshot",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded chart",
        use_container_width=True
    )

    st.divider()

    # =========================
    # ANALYZE BUTTON
    # =========================

    if st.button(
        "🔍 ANALYZE SCREENSHOT",
        use_container_width=True
    ):

        st.subheader("Signal Result")

        # Temporary result.
        # Real analysis engine will be added later.

        score = 0

        if score >= 80:

            st.success("SIGNAL")

        else:

            st.error("NO TRADE")

        st.metric(
            "Model Score",
            f"{score}/100"
        )

        st.write("**Asset:**", asset if asset else "Not specified")
        st.write("**Timeframe:**", timeframe)
        st.write("**Expiry:**", expiry)

        st.divider()

        st.write("### Two-Candle Plan")

        st.write("**Candle 1:** WAIT")
        st.write("**Candle 2:** WAIT")

        st.info(
            "The screenshot-analysis engine is not connected yet. "
            "This version only tests the website interface."
        )

else:

    st.info(
        "Upload a Quotex screenshot to begin."
    )

st.divider()

st.caption(
    "Research prototype. Signals are probabilistic and are not guaranteed."
)
