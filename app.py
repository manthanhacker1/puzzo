import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little Question 💌",
    page_icon="💌",
    layout="centered"
)

html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;
    font-family: -apple-system, BlinkMacSystemFont, "Inter", sans-serif;
    background:
        radial-gradient(circle at 20% 20%, rgba(255,91,135,.25), transparent 30%),
        radial-gradient(circle at 80% 80%, rgba(139,92,246,.22), transparent 30%),
        linear-gradient(135deg,#0b0710,#180c19,#0b0710);
    color: white;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.card {
    width: min(520px,100%);
    padding: 42px 30px;
    text-align: center;
    border: 1px solid rgba(255,255,255,.12);
    border-radius: 30px;
    background: rgba(255,255,255,.07);
    backdrop-filter: blur(25px);
    box-shadow: 0 30px 80px rgba(0,0,0,.45);
}

.emoji {
    font-size: 58px;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    50% { transform: translateY(-8px); }
}

h1 {
    font-size: clamp(32px,8vw,48px);
    letter-spacing: -1.5px;
    margin: 18px 0 12px;
}

.gradient {
    background: linear-gradient(90deg,#ff6b9a,#ffb1c8);
    -webkit-background-clip: text;
    color: transparent;
}

.subtitle {
    color: #cfc5d0;
    font-size: 17px;
    line-height: 1.6;
}

.question {
    font-size: 24px;
    font-weight: 700;
    margin: 28px 0 24px;
}

.buttons {
    display: flex;
    gap: 14px;
    justify-content: center;
}

button {
    border: 0;
    cursor: pointer;
    font-size: 16px;
    font-weight: 700;
    padding: 15px 28px;
    border-radius: 999px;
    transition: .2s;
}

button:hover {
    transform: translateY(-3px);
}

.yes {
    color: white;
    background: linear-gradient(135deg,#ff477e,#ff6a9a);
    box-shadow: 0 10px 30px rgba(255,71,126,.3);
}

.no {
    color: #ddd;
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.12);
}

.message-box {
    display: none;
    margin-top: 25px;
}

textarea {
    width: 100%;
    height: 110px;
    resize: none;
    border: 1px solid rgba(255,255,255,.12);
    background: rgba(0,0,0,.25);
    color: white;
    border-radius: 18px;
    padding: 15px;
    outline: none;
    font: inherit;
}

.send {
    width: 100%;
    margin-top: 12px;
    background: white;
    color: #171018;
}

.response {
    display: none;
    margin-top: 22px;
    padding: 18px;
    border-radius: 18px;
    background: rgba(255,255,255,.08);
    line-height: 1.5;
}

.heart {
    position: fixed;
    pointer-events: none;
    animation: fly 2.5s linear forwards;
    font-size: 20px;
}

@keyframes fly {
    0% {
        transform: translateY(0) scale(.5);
        opacity: 0;
    }

    20% {
        opacity: 1;
    }

    100% {
        transform: translateY(-100vh) rotate(360deg);
        opacity: 0;
    }
}

.small {
    color: #9f96a1;
    font-size: 13px;
    margin-top: 25px;
}

@media(max-width:480px) {
    .buttons {
        flex-direction: column;
    }

    button {
        width: 100%;
    }
}
</style>
</head>

<body>

<div class="card">

    <div class="emoji">💌</div>

    <h1>
        Okay... I have a
        <span class="gradient">question.</span>
    </h1>

    <p class="subtitle">
        We've matched, we've talked...
        so I think it's time I ask you something slightly more important.
    </p>

    <div class="question">
        Would you go on a date with me? 👀
    </div>

    <div class="buttons">

        <button class="yes" onclick="yesClicked()">
            Yes, let's go ❤️
        </button>

        <button class="no" onclick="maybeClicked()">
            Hmm... maybe 😌
        </button>

    </div>

    <div id="messageBox" class="message-box">

        <textarea
            id="message"
            placeholder="Tell me what you're thinking... 💭">
        </textarea>

        <button class="send" onclick="sendMessage()">
            Send it 💌
        </button>

    </div>

    <div id="response" class="response"></div>

    <div class="small">
        No pressure. Just two people potentially having a dangerously good time. ✨
    </div>

</div>


<script>

function hearts() {

    for(let i = 0; i < 20; i++) {

        const h = document.createElement("div");

        h.className = "heart";

        h.innerHTML =
            ["❤️","💗","💕","💖"][Math.floor(Math.random()*4)];

        h.style.left = Math.random()*100 + "vw";
        h.style.bottom = "-30px";

        document.body.appendChild(h);

        setTimeout(() => h.remove(), 3000);
    }
}


function showMessage() {

    document.getElementById("messageBox").style.display = "block";

    document.getElementById("message").focus();
}


function yesClicked() {

    hearts();

    showMessage();

    const r = document.getElementById("response");

    r.style.display = "block";

    r.innerHTML = `
        <div style="font-size:30px">🥹❤️</div>
        <strong>Okay, that's a YES!</strong><br>
        Now tell me what kind of date you're imagining...
    `;
}


function maybeClicked() {

    showMessage();

    const r = document.getElementById("response");

    r.style.display = "block";

    r.innerHTML = `
        <div style="font-size:30px">😌</div>
        <strong>I'll take "maybe"...</strong><br>
        What would convince you?
    `;
}


function sendMessage() {

    const msg =
        document.getElementById("message").value.trim();

    if(!msg) {

        alert("Write something first 😭");

        return;
    }

    hearts();

    const r = document.getElementById("response");

    r.style.display = "block";

    r.innerHTML = `
        <div style="font-size:30px">💌</div>
        <strong>Message received.</strong><br><br>
        "${msg}"
        <br><br>
        <span style="color:#aaa">
            Now we just need to pick a day 😉
        </span>
    `;
}

</script>

</body>
</html>
"""

components.html(html, height=800, scrolling=False)
