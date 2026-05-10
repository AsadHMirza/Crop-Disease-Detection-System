import streamlit as st
import pymongo
import time

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="Crop Disease Detection - Sign In",
    page_icon="🌱",
    layout="centered"
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
    background-color: #f5fff5;
}

</style>
""", unsafe_allow_html=True)

# =========================
# MONGODB CONNECTION
# =========================

myclient = pymongo.MongoClient(
    "mongodb://127.0.0.1:27017/"
)

mydb = myclient["crop_disease_project"]

mycollection = mydb["users"]

# =========================
# TITLE
# =========================

st.title("🌱 Crop Disease Detection System")

st.subheader("🔐 User Login")

st.write("""
Login to access AI-powered crop disease prediction.
""")

st.markdown("---")

# =========================
# LOGIN FORM
# =========================

with st.container():

    st.markdown("### 👤 Enter Login Details")

    email = st.text_input(
        "📧 Email Address"
    )

    password = st.text_input(
        "🔒 Password",
        type="password"
    )

    st.markdown("")

    login_button = st.button(
        "🚀 Login",
        use_container_width=True
    )

# =========================
# LOGIN LOGIC
# =========================

if login_button:

    # Search User
    user = mycollection.find_one({

        "email": email,

        "password": password
    })

    # Valid Login
    if user:

        with st.spinner(
            "🔄 Logging in... Please wait"
        ):

            time.sleep(3)

        st.success(
            "✅ Login Successful"
        )

        st.balloons()

        # Session State
        st.session_state.logged_in = True

        st.session_state.username = user["name"]

        # User Details
        st.markdown("---")

        st.subheader(
            "👤 User Details"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.info(
                f"👤 Name: {user['name']}"
            )

            st.info(
                f"📧 Email: {user['email']}"
            )

        with col2:

            st.info(
                f"⚧ Gender: {user['gender']}"
            )

            st.info(
                f"📍 State: {user['state']}"
            )

        time.sleep(2)

        # Redirect
        st.switch_page("main.py")

    # Invalid Login
    else:

        st.error(
            "❌ Invalid Email or Password"
        )

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "Made with ❤️ using Streamlit, MongoDB & Python"
)
