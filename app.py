# app.py

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64

st.set_page_config(
    page_title="A Little Something 💌",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE = Path(__file__).parent

HTML_FILE = BASE / "index.html"
IMAGE_FILE = BASE / "photo.jpeg"

# Convert the uploaded/local photo to base64.
# This avoids Google Drive embedding problems completely.
with open(IMAGE_FILE, "rb") as f:
    image_data = base64.b64encode(f.read()).decode("utf-8")

image_src = f"data:image/jpeg;base64,{image_data}"

html = HTML_FILE.read_text(encoding="utf-8")

html = html.replace(
    "PHOTO_PLACEHOLDER",
    image_src
)

components.html(
    html,
    height=3000,
    scrolling=True
)
