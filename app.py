# app.py

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="A Little Something ✨",
    page_icon="💌",
    layout="wide"
)

HTML_FILE = Path(__file__).parent / "index.html"

html = HTML_FILE.read_text(encoding="utf-8")

components.html(
    html,
    height=3000,
    scrolling=True
)
