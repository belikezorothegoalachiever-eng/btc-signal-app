
import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="BTC Signal Analyzer",
    page_icon="📈",
    layout="centered"
)

st.title("📈 BTC Signal Analyzer")
st.caption("Screenshot-Based 2-Minute Signal System")

st.divider()

# Fixed settings
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Market", "BTC/USD")

with col2:
    st.metric("Chart", "1 Minute")

with col3:
    st.metric("Expiry", "2 Minutes")

col4, col5, col6 = st.columns(3)

with col4:
    st.metric("Capital", "$5,000")

with col5:
    st.metric("Normal Risk", "$50")

with col6:
    st.metric("Max Risk", "$80")

st.divider()

st.subheader("📷 Upload Quotex Screenshot")

uploaded_file = st.file_uploader(
    "Choose a screenshot",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded BTC/USD chart",
        use_container_width=True
    )

    st.success("Screenshot received.")

    if st.button("🔍 ANALYZE SCREENSHOT", use_container_width=True):

        st.subheader("Signal Result")

        st.warning("NO TRADE")

        st.metric(
            "Model Score",
            "Not calculated yet"
        )

        st.write(
            "The screenshot-analysis engine will be connected "
            "in the next version."
        )

        st.write("**Candle 1:** WAIT")
        st.write("**Candle 2:** WAIT")

        st.info(
            "We are not generating fake signals. "
            "The real analysis engine will be added after "
            "the website interface is working."
        )

else:

    st.info(
        "Upload a BTC/USD screenshot to begin."
    )
