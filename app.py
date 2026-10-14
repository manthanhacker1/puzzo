```python
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little Note ♡",
    page_icon="♡",
    layout="centered"
)

APP_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    background: #100d14;
    color: #fff4f5;
    font-family: Arial, sans-serif;
}

.page {
    max-width: 520px;
    margin: auto;
    padding: 22px 16px 40px;
}

.card {
    background: linear-gradient(145deg, #241724, #19131d);
    border: 1px solid #4b3044;
    border-radius: 23px;
    padding: 25px 20px;
    margin-bottom: 18px;
    box-shadow: 0 10px 35px #0003;
}

.center {
    text-align: center;
}

.heart {
    color: #ff8fa3;
    font-size: 40px;
    animation: pulse 1.8s infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.13); }
}

h1 {
    font-size: 29px;
    line-height: 1.25;
    margin: 12px 0;
}

h2 {
    font-size: 21px;
    margin-top: 0;
}

p {
    color: #e0cdd9;
    font-size: 15px;
    line-height: 1.8;
}

.small {
    color: #bda9bd;
    font-size: 12px;
}

button {
    font-size: 15px;
    font-weight: bold;
    border: none;
    border-radius: 13px;
    padding: 14px 18px;
    cursor: pointer;
    transition: transform 0.2s, opacity 0.2s;
}

button:active {
    transform: scale(0.96);
}

.primary {
    color: #351523;
    background: linear-gradient(135deg, #ffb1c0, #ff8ca8);
    width: 100%;
}

.secondary {
    color: #f6dce8;
    background: #342337;
    border: 1px solid #60445d;
}

.field {
    display: flex;
    gap: 9px;
    flex-wrap: wrap;
    justify-content: center;
}

.choice {
    flex: 1 1 125px;
    background: #302132;
    color: #f8dce8;
    border: 1px solid #60445d;
}

.choice.selected {
    background: #f8a6ba;
    color: #321322;
    border-color: #f8a6ba;
}

.hidden {
    display: none !important;
}

#gate {
    padding-top: 30px;
}

input {
    width: 100%;
    padding: 14px;
    margin: 12px 0;
    border-radius: 12px;
    border: 1px solid #60445d;
    background: #17111b;
    color: white;
    font-size: 16px;
    outline: none;
}

#error {
    color: #ff9eb2;
    font-size: 13px;
    min-height: 18px;
}

.buttons {
    position: relative;
    min-height: 125px;
    margin-top: 18px;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    gap: 13px;
    flex-wrap: wrap;
}

#yesBtn {
    background: linear-gradient(135deg, #ffb1c0, #ff8ca8);
    color: #351523;
    min-width: 135px;
}

#noBtn {
    background: #342337;
    color: #f6dce8;
    border: 1px solid #60445d;
    min-width: 135px;
    position: relative;
}

#yes-response {
    margin-top: 20px;
    padding: 20px;
    background: #352035;
    border: 1px solid #8e5475;
    border-radius: 18px;
}

#yes-response h2 {
    color: #ffb1c0;
}

.floating-heart {
    position: fixed;
    bottom: -30px;
    z-index: 9999;
    pointer-events: none;
    animation: floatUp 3s ease-out forwards;
}

@keyframes floatUp {
    0% {
        transform: translateY(0) rotate(0deg);
        opacity: 0;
    }
    15% { opacity: 1; }
    100% {
        transform: translateY(-100vh) rotate(35deg);
        opacity: 0;
    }
}

.footer {
    text-align: center;
    color: #9e889e;
    font-size: 12px;
    padding: 8px;
}
</style>
</head>

<body>
<div class="page">

    <section class="card center" id="gate">
        <div class="heart">♡</div>
        <h1>A little note for you</h1>
        <p>There's something I wanted to share with you.</p>
        <p class="small">A tiny hint: try entering your name ♡</p>

        <input
            id="password"
            type="password"
            placeholder="Enter the password..."
            autocomplete="off"
        >

        <button class="primary" onclick="unlock()">
            Open my note ♡
        </button>

        <div id="error"></div>
    </section>

    <main id="content" class="hidden">

        <section class="card center">
            <div class="heart">♡</div>
            <h1>Hey, Mitali</h1>
            <p>
                I know things haven't always been perfect, and I just
                wanted to say I'm sorry for my part in things.
            </p>
            <p>
                I don't want to put any pressure on you. I just thought
                it would be nice to talk once, calmly, and maybe have
                a coffee together.
            </p>
            <p>
                No big expectations. Just a little time together
                and a chance to talk. :)
            </p>
            <p class="small">I made this little page just for you ♡</p>
        </section>

        <section class="card">
            <h2 class="center">If we ever meet...</h2>
            <p class="center">What kind of coffee vibe would you pick?</p>

            <div class="field">
                <button class="choice selected"
                    onclick="pickVibe(this, 'Coffee')">
                    ☕ Coffee
                </button>

                <button class="choice"
                    onclick="pickVibe(this, 'Cold coffee')">
                    🧋 Cold coffee
                </button>

                <button class="choice"
                    onclick="pickVibe(this, 'A simple walk')">
                    🌙 A walk
                </button>
            </div>

            <p class="center small" id="vibeText">
                Coffee sounds nice ☕
            </p>
        </section>

        <section class="card center">
            <h2>So, what do you think? ♡</h2>
            <p>
                Would you be comfortable meeting for a coffee
                sometime? Only if you want to.
            </p>

            <div class="buttons" id="buttonArea">
                <button id="yesBtn" onclick="answer('yes')">
                    Yes, let's do it ♡
                </button>

                <button id="noBtn" onclick="answer('no')">
                    No 🙈
                </button>
            </div>

            <!-- No rejection or goodbye message is shown. -->
            <div id="yes-response" class="hidden">
                <div class="heart">♡</div>
                <h2>Yay! ☕</h2>
                <p id="yes-text">
                    That made me smile! Let's figure out a time
                    whenever you're comfortable. ♡
                </p>
                <p class="small">One coffee, one conversation. No pressure.</p>
            </div>
        </section>

        <div class="footer">
            Made with a little courage and a lot of heart ♡
        </div>

    </main>
</div>

<script>
let vibe = "Coffee";
let noMoves = 0;

function unlock() {
    const password = document.getElementById("password")
        .value.trim().toLowerCase();

    if (password === "mitali") {
        document.getElementById("gate").classList.add("hidden");
        document.getElementById("content").classList.remove("hidden");
        hearts(5);
    } else {
        document.getElementById("error").textContent =
            "Not quite 🙈 Try again!";
    }
}

document.getElementById("password").addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        unlock();
    }
});

function pickVibe(button, selectedVibe) {
    vibe = selectedVibe;

    document.querySelectorAll(".choice").forEach(function(item) {
        item.classList.remove("selected");
    });

    button.classList.add("selected");

    document.getElementById("vibeText").textContent =
        selectedVibe + " sounds nice ♡";
}

function moveNoButton() {
    const button = document.getElementById("noBtn");
    const area = document.getElementById("buttonArea");

    if (noMoves >= 3) {
        return;
    }

    noMoves++;

    const maxX = Math.max(0, area.clientWidth - button.offsetWidth);
    const maxY = 65;

    button.style.position = "absolute";
    button.style.left = Math.floor(Math.random() * maxX) + "px";
    button.style.top = Math.floor(Math.random() * maxY) + "px";
}

document.getElementById("noBtn").addEventListener("mouseenter", function() {
    moveNoButton();
});

document.getElementById("noBtn").addEventListener("touchstart", function() {
    if (noMoves < 3) {
        moveNoButton();
    }
}, { passive: true });

function answer(choice) {
    const response = document.getElementById("yes-response");

    if (choice === "no") {
        // No goodbye screen or rejection message.
        response.classList.add("hidden");
        return;
    }

    response.classList.remove("hidden");

    document.getElementById("yes-text").textContent =
        "That made me smile! Let's figure out " +
        vibe.toLowerCase() +
        " together whenever you're comfortable. ♡";

    hearts(22);

    setTimeout(function() {
        response.scrollIntoView({
            behavior: "smooth",
            block: "nearest"
        });
    }, 60);
}

function hearts(count) {
    const symbols = ["♡", "♥", "💕", "💗"];

    for (let i = 0; i < count; i++) {
        const heart = document.createElement("div");

        heart.className = "floating-heart";
        heart.textContent = symbols[
            Math.floor(Math.random() * symbols.length)
        ];

        heart.style.left = Math.random() * 100 + "vw";
        heart.style.fontSize = (16 + Math.random() * 20) + "px";
        heart.style.animationDuration = (2 + Math.random() * 2) + "s";

        document.body.appendChild(heart);

        setTimeout(function() {
            heart.remove();
        }, 4200);
    }
}
</script>
</body>
</html>
"""

components.html(APP_HTML, height=1800, scrolling=True)
```

