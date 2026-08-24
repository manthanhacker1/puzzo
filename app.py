import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Date Invitation", page_icon="🌸", layout="centered")

# Hide default Streamlit padding & headers
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0rem;}
    </style>
""", unsafe_allow_html=True)

# Read your HTML file
with open("indexx.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Render HTML inside Streamlit
components.html(html_data, height=700, scrolling=True)
