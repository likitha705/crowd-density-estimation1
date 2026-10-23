
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(
    page_title="Crowd Density Estimation",
    page_icon="👥",
    layout="wide"
)

st.title("👥 Crowd Density Estimation")
st.write("CNN-Based Crowd Counting and Density Map Analysis")

st.sidebar.header("Project Details")
st.sidebar.write("Domain: Deep Learning & Computer Vision")
st.sidebar.write("Model: CNN Density Map Regression")

uploaded_file = st.file_uploader(
    "Upload a crowd image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("Uploaded Image")
    st.image(image, use_container_width=True)

    st.info(
        "Image uploaded successfully. Uploading an image alone "
        "does not produce a verified crowd count."
    )

    st.warning(
        "Train and integrate your CNN density-map model "
        "to enable actual crowd-count predictions."
    )
else:
    st.info("Please upload a crowd image to get started.")

st.divider()
st.caption("Final Year Project | Crowd Safety Monitoring")
