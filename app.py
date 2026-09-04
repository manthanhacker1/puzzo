import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="I'm Sorry! 🥺",
    page_icon="💌",
    layout="centered"
)

# Custom CSS styling
st.markdown("""
    <style>
    .main {
        background-color: #fff0f5;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff6b81;
        color: white;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ff4757;
        color: white;
    }
    h1, h2, p {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

st.title("I'm Really Sorry... 🥺")
st.write("---")

st.markdown("""
### Hey there,

I hate that things felt off between us. I really value our connection and hate being the reason for a frown on your face.

I made a little interactive tool just to earn a second chance!
""")

st.write("")

# Interactive Apology Slider
forgiveness_level = st.slider(
    "How upset are you right now?",
    min_value=0,
    max_value=100,
    value=80,
    format="%d%%"
)

if forgiveness_level > 50:
    st.info("Okay, I deserve that... Let me try to make it up to you! 🍫")
elif forgiveness_level > 10:
    st.warning("Getting warmer! Almost back to normal? 🤞")
else:
    st.success("Yay! Glad we're good again! ✨")

st.write("")

# Interactive Options
st.markdown("#### **How can I make it right?**")
choice = st.radio(
    "Pick your preferred apology gift:",
    ["☕ A fresh cup of coffee/tea", "🍨 Ice cream & a long chat", "🍕 Pizza + movie night", "🌸 A genuine heartfelt apology call"]
)

st.write("")

# Decision Button
if st.button("Accept Apology & Redeem Gift ❤️"):
    st.balloons()
    st.success(f"Awesome choice! Redemption locked in: **{choice}**. Looking forward to it!")
    st.snow()
