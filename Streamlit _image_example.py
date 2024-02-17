# image example
import streamlit as st
from PIL import Image

# Title
st.title("Display Image Example")

# Load image
image = Image.open("New1.jpg")

# Display image
st.image(image, caption='Example Image', use_column_width=True)
