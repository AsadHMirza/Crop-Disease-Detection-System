import streamlit as st
import pymongo
import random
import os
import datetime

# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="Crop Disease Detection - Sign Up",
    page_icon="🌱",
    layout="centered"
)

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

st.subheader("📝 Create Your Account")

st.write("""
Register to access AI-powered crop disease prediction and smart farming tools.
""")

st.markdown("---")

# =========================
# USER DETAILS
# =========================

name = st.text_input("👤 Full Name")

username = st.text_input("🆔 Username")

email = st.text_input("📧 Email Address")

phone = st.text_input("📱 Phone Number")

password = st.text_input(
    "🔒 Password",
    type="password"
)

confirm_password = st.text_input(
    "🔑 Confirm Password",
    type="password"
)

gender = st.radio(
    "⚧ Gender",
    ["Male", "Female"]
)

state = st.selectbox(
    "📍 State",
    [
        "Bihar",
        "Delhi",
        "Maharashtra",
        "Uttar Pradesh",
        "West Bengal",
        "Jharkhand",
        "Other"
    ]
)

farming_type = st.selectbox(
    "🌾 Farming Type",
    [
        "Vegetable Farming",
        "Fruit Farming",
        "Organic Farming",
        "Mixed Farming"
    ]
)

experience = st.slider(
    "🌱 Farming Experience (Years)",
    0,
    30,
    1
)

address = st.text_area("🏠 Address")

dob = st.date_input(
    "📅 Date of Birth",
    min_value=datetime.date(1950, 1, 1),
    max_value=datetime.date.today()
)

# =========================
# PROFILE IMAGE
# =========================

st.subheader("📸 Upload Profile Picture")

camera_image = st.camera_input(
    "Take a Picture"
)

# =========================
# SAVE IMAGE
# =========================

image_name = ""

if camera_image is not None:

    if not os.path.exists("images"):

        os.makedirs("images")

    count = random.randint(1, 10000)

    image_name = f"images/profile_{count}.png"

    with open(image_name, "wb") as f:

        f.write(camera_image.getvalue())

    st.success("✅ Image Captured Successfully")

# =========================
# REGISTER BUTTON
# =========================

register_button = st.button("🚀 Register")

# =========================
# SAVE FUNCTION
# =========================

def save_user():

    user_data = {

        "name": name,
        "username": username,
        "email": email,
        "phone": phone,
        "password": password,
        "gender": gender,
        "state": state,
        "farming_type": farming_type,
        "experience": experience,
        "address": address,
        "dob": str(dob),
        "profile_image": image_name
    }

    mycollection.insert_one(user_data)

    st.success("✅ Registration Successful")

    st.balloons()

# =========================
# BUTTON ACTION
# =========================

if register_button:

    if not name or not username or not email or not password:

        st.error("❌ Please fill all required fields")

    elif password != confirm_password:

        st.error("❌ Passwords do not match")

    else:

        save_user()

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption("Made with ❤️ using Streamlit, MongoDB & Python")
