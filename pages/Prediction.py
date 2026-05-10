import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="Crop Disease Detection",
    page_icon="🌱",
    layout="wide"
)

# =========================
# TOP BUTTONS
# =========================

col1, col2, col3 = st.columns([4,1,1])

with col2:

    if st.button("🏠 Home"):

        st.switch_page("app.py")

with col3:

    if st.button("🔐 Logout"):

        st.switch_page("pages/SignIn.py")

# =========================
# LOAD MODEL
# =========================

model = tf.keras.models.load_model(
    "model/plant_disease_model.h5"
)

# =========================
# CLASS NAMES
# =========================

class_names = [

    "Tomato Early Blight",

    "Tomato Healthy",

    "Tomato Late Blight"
]

# =========================
# TITLE
# =========================

st.title("🌱 Crop Disease Detection System")

st.subheader("AI Powered Tomato Disease Detection")

st.write("""
Upload a tomato leaf image to detect disease using AI & Deep Learning.
""")

# =========================
# SUPPORTED CLASSES
# =========================

st.info("""
Supported Classes:

• Tomato Early Blight

• Tomato Healthy

• Tomato Late Blight
""")

st.markdown("---")

# =========================
# IMAGE UPLOAD
# =========================

uploaded_file = st.file_uploader(
    "📸 Upload Tomato Leaf Image",
    type=["jpg", "jpeg", "png"]
)

# =========================
# PREDICTION
# =========================

if uploaded_file is not None:

    # Open image
    img = Image.open(uploaded_file)

    # Convert to RGB
    img = img.convert("RGB")

    # Display image
    st.image(
    img,
    caption="Uploaded Image",
    width=250
    )

    # Resize image
    img = img.resize((128,128))

    # Convert image to array
    img_array = np.array(img)

    # Normalize image
    img_array = img_array / 255.0

    # Expand dimensions
    img_array = np.expand_dims(
        img_array,
        axis=0
    )

    # Predict
    prediction = model.predict(img_array)

    # Probabilities
    probabilities = prediction[0]

    # Highest prediction index
    predicted_index = np.argmax(
        probabilities
    )

    # Confidence
    confidence = (
        probabilities[predicted_index]
        * 100
    )

    # Final prediction
    if confidence < 70:

        predicted_class = (
            "Unknown Disease"
        )

    else:

        if predicted_index < len(class_names):

            predicted_class = (
                class_names[predicted_index]
            )

        else:

            predicted_class = (
                "Unknown Disease"
            )

    st.markdown("---")

    # =========================
    # RESULT
    # =========================

    st.subheader(
        "🩺 Prediction Result"
    )

    st.success(
        f"Disease: {predicted_class}"
    )

    st.write(
        f"🎯 Accuracy: {confidence:.2f}%"
    )

    st.markdown("---")

    # =========================
    # PROBABILITIES
    # =========================

    st.subheader(
        "📊 Prediction Probabilities"
    )

    for i, prob in enumerate(probabilities):

        if i < len(class_names):

            if prob > 0.01:

                st.progress(float(prob))

                st.write(
                    f"{class_names[i]} : "
                    f"{prob * 100:.2f}%"
                )

    st.markdown("---")

    # =========================
    # TREATMENT
    # =========================

    if predicted_class == (
        "Tomato Early Blight"
    ):

        st.warning("""
### 💊 Treatment Suggestions

- Remove infected leaves

- Use fungicide spray

- Avoid overwatering

- Improve air circulation
""")

    elif predicted_class == (
        "Tomato Late Blight"
    ):

        st.warning("""
### 💊 Treatment Suggestions

- Use copper fungicide

- Remove affected plants

- Reduce humidity

- Avoid water on leaves
""")

    elif predicted_class == (
        "Tomato Healthy"
    ):

        st.success("""
### 🌿 Plant is Healthy

- Maintain proper watering

- Provide sunlight

- Use balanced fertilizer

- Monitor leaves regularly
""")

    else:

        st.error("""
### ⚠️ Unknown Disease

The uploaded image does not match
the trained tomato disease classes.

Please upload a clear tomato leaf image.
""")

# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "Made with ❤️ using "
    "Streamlit, TensorFlow "
    "& Deep Learning"
)
