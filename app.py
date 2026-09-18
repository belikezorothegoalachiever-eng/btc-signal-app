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
# MARKET
# =========================

st.subheader("Market")

asset = st.text_input(
    "Asset",
    placeholder="Example: NZD/JPY"
)

asset_type = st.selectbox(
    "Asset Type",
    ["Regular", "OTC"]
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
# PATTERN INFORMATION
# =========================

st.subheader("🧠 Pattern Information")

pattern_name = st.text_input(
    "Pattern Name",
    placeholder="Example: Support Rejection"
)

pattern_notes = st.text_area(
    "Describe the pattern you see",
    placeholder="Describe what happened before the signal..."
)

st.divider()

# =========================
# SCREENSHOT
# =========================

st.subheader("📷 Chart Screenshot")

uploaded_file = st.file_uploader(
    "Upload Quotex screenshot",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Quotex chart",
        use_container_width=True
    )

    st.success("Screenshot uploaded.")

    st.divider()

    # =========================
    # ANALYSIS
    # =========================

    if st.button(
        "🔍 ANALYZE",
        use_container_width=True
    ):

        st.subheader("Signal Result")

        st.warning("NO TRADE")

        st.metric(
            "Model Score",
            "Not calculated yet"
        )

        st.write("**Asset:**", asset)
        st.write("**Type:**", asset_type)
        st.write("**Timeframe:**", timeframe)
        st.write("**Expiry:**", expiry)

        st.divider()

        st.write("### Two-Candle Plan")

        st.write("**Candle 1:** WAIT")
        st.write("**Candle 2:** WAIT")

        st.info(
            "The analysis engine will be connected after "
            "the data collection system is ready."
        )

    st.divider()

    # =========================
    # RESULT RECORDING
    # =========================

    st.subheader("📝 Record Actual Result")

    result = st.selectbox(
        "Candle 1 Result",
        ["Not recorded", "WIN", "LOSS"]
    )

    if result == "LOSS":

        candle2_result = st.selectbox(
            "Candle 2 Result",
            ["Not recorded", "WIN", "LOSS"]
        )

    else:

        candle2_result = "Not required"

    if st.button(
        "💾 SAVE RESULT",
        use_container_width=True
    ):

        st.success(
            "Result recorded for this setup."
        )

else:

    st.info(
        "Upload a screenshot to begin."
    )

st.divider()

st.caption(
    "Research prototype. Signals are probabilistic and are not guaranteed."
)
