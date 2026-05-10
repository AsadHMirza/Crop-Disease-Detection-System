import streamlit as st

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Crop Disease Detection System",
    page_icon="🌱",
    layout="wide"
)

# =========================
# HIDE SIDEBAR
# =========================

st.markdown("""
<style>

[data-testid="stSidebarNav"] {
    display: none;
}

.main {
    background-color: #f8fff8;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False

# =========================
# WELCOME USER
# =========================

if "username" in st.session_state:

    st.success(
        f"Welcome {st.session_state.username} 👋"
    )

# =========================
# TOP BUTTONS
# =========================

col1, col2, col3, col4 = st.columns([3,1,1,1])

# Sign In Button
if not st.session_state.logged_in:

    with col2:

        if st.button("🔐 Sign In"):

            st.switch_page(
                "pages/SignIn.py"
            )

# Sign Up Button
if not st.session_state.logged_in:

    with col3:

        if st.button("📝 Sign Up"):

            st.switch_page(
                "pages/SignUp.py"
            )

# Contact Button
with col4:

    if st.button("📞 Contact"):

        st.switch_page(
            "pages/Contact.py"
        )

# =========================
# TITLE
# =========================

st.title(
    "🌱 Crop Disease Detection System"
)

st.subheader(
    "AI Powered Plant Disease Detection"
)

st.write("""
Detect tomato plant diseases using
Deep Learning and Artificial Intelligence.
""")

# =========================
# IMAGE
# =========================

st.image(
    "https://images.unsplash.com/photo-1501004318641-b39e6451bec6",
    caption="Smart Farming using AI",
    use_container_width=True
)

st.markdown("---")

# =========================
# FEATURES
# =========================

st.header("✨ Project Features")

c1, c2, c3 = st.columns(3)

with c1:

    st.info("""
📸 Upload crop leaf images
""")

with c2:

    st.info("""
🧠 AI based disease prediction
""")

with c3:

    st.info("""
💊 Treatment suggestions
""")

st.markdown("---")

# =========================
# PROJECT DETAILS
# =========================

st.header("📌 About Project")

st.write("""
This project uses Deep Learning and CNN
to identify tomato plant diseases from images.

The system helps farmers and users detect diseases quickly.
""")

# =========================
# START PREDICTION
# =========================

if st.session_state.logged_in:

    st.success(
        "✅ Login Successful"
    )

    if st.button(
        "🚀 Start Prediction",
        use_container_width=True
    ):

        st.switch_page(
            "pages/Prediction.py"
        )

else:

    st.warning(
        "⚠️ Please Sign In or Sign Up"
    )

st.markdown("---")

# =========================
# FOOTER
# =========================

st.caption(
    "Made with ❤️ using Streamlit, TensorFlow & MongoDB"
)
