# app.py

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="Special Delivery 💌",
    page_icon="💌",
    layout="wide"
)

BASE = Path(__file__).parent

html = (BASE / "index.html").read_text(
    encoding="utf-8"
)

components.html(
    html,
    height=2600,
    scrolling=True
)
