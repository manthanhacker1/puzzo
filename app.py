
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little Something for Mitali ♡",
    page_icon="💌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    #MainMenu, footer, header, [data-testid="stToolbar"],
    [data-testid="stDecoration"], [data-testid="stStatusWidget"] {
        display: none !important;
    }
    .stApp {
        background: #fff8f6;
    }
    [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        max-width: 100% !important;
    }
    iframe {
        border: none !important;
    }
</style>
""", unsafe_allow_html=True)

APP_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>A little something ♡</title>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;1,500;1,600&display=swap" rel="stylesheet">

<style>
* { box-sizing: border-box; }

:root {
    --ink: #422c38;
    --muted: #947783;
    --pink: #db8ca2;
    --deep: #a44e6c;
    --cream: #fffaf5;
    --line: #f0dce3;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    min-height: 100vh;
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
    background:
        radial-gradient(ellipse at 0% 8%,
            rgba(255,214,222,.70), transparent 32%),
        radial-gradient(ellipse at 100% 58%,
            rgba(230,207,242,.48), transparent 35%),
        linear-gradient(145deg, #fffaf6, #fff2f3 60%, #faf2ff);
}

button, input {
    font: inherit;
}

button {
    cursor: pointer;
    -webkit-tap-highlight-color: transparent;
}

button:focus-visible, input:focus-visible {
    outline: 3px solid #dfa0b3;
    outline-offset: 3px;
}

.app {
    width: 100%;
    max-width: 720px;
    margin: auto;
    padding: 32px 18px 44px;
}

.topline {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 9px;
    color: var(--muted);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 2.2px;
    text-transform: uppercase;
    margin-bottom: 27px;
}

.topline span {
    color: var(--pink);
    font-size: 18px;
    animation: heartbeat 1.8s infinite;
}

@keyframes heartbeat {
    0%, 100% { transform: scale(1); }
    15% { transform: scale(1.18); }
    30% { transform: scale(1); }
    45% { transform: scale(1.12); }
}

.panel {
    position: relative;
    overflow: hidden;
    background: rgba(255, 252, 249, .88);
    border: 1px solid rgba(255,255,255,.95);
    border-radius: 30px;
    padding: clamp(22px, 5vw, 42px);
    box-shadow: 0 22px 65px rgba(113, 62, 83, .10);
}

.panel::before {
    content: "";
    position: absolute;
    width: 190px;
    height: 190px;
    right: -90px;
    top: -105px;
    background: rgba(250, 209, 221, .45);
    border-radius: 50%;
    pointer-events: none;
}

.center { text-align: center; }

.sticker {
    width: 76px;
    height: 76px;
    border-radius: 25px;
    display: grid;
    place-items: center;
    margin: 5px auto 22px;
    font-size: 35px;
    background: linear-gradient(145deg, #ffe4e9, #f9d6e9);
    box-shadow: 0 10px 25px rgba(183,91,125,.12);
    transform: rotate(-5deg);
}

h1, h2, .serif {
    font-family: 'Playfair Display', Georgia, serif;
    font-weight: 500;
}

h1 {
    font-size: clamp(36px, 8vw, 57px);
    line-height: 1.12;
    letter-spacing: -1.8px;
    margin: 0 0 16px;
}

h1 em, h2 em {
    color: var(--deep);
    font-weight: 500;
}

.sub {
    color: var(--muted);
    font-size: 14px;
    line-height: 1.9;
    max-width: 410px;
    margin: 0 auto 27px;
}

.tag {
    display: inline-block;
    padding: 8px 13px;
    border-radius: 50px;
    background: #fff0f3;
    color: #a44e6c;
    border: 1px solid #f9dce5;
    text-transform: uppercase;
    letter-spacing: 1.3px;
    font-size: 10px;
    font-weight: 700;
    margin-bottom: 18px;
}

.input-wrap {
    max-width: 390px;
    margin: 0 auto;
}

.input-wrap input {
    display: block;
    width: 100%;
    border: 1px solid var(--line);
    background: #fff;
    color: var(--ink);
    border-radius: 15px;
    padding: 17px;
    outline: none;
    margin-bottom: 12px;
    text-align: center;
    font-size: 15px;
    transition: .2s;
}

.input-wrap input:focus {
    border-color: #d88da5;
    box-shadow: 0 0 0 4px rgba(216,141,165,.12);
}

.primary {
    width: 100%;
    border: none;
    border-radius: 15px;
    padding: 16px 18px;
    background: linear-gradient(105deg, #b25b79, #d58da6);
    color: white;
    font-size: 14px;
    font-weight: 700;
    box-shadow: 0 10px 22px rgba(173,81,115,.20);
    transition: transform .2s, box-shadow .2s;
}

.primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 25px rgba(173,81,115,.25);
}

.hint {
    display: none;
    max-width: 390px;
    margin: 13px auto 0;
    color: #984664;
    background: #fff0f3;
    border: 1px solid #f5d9e2;
    border-radius: 13px;
    padding: 12px;
    font-size: 13px;
    animation: appear .3s ease;
}

.small-note {
    margin: 23px 0 0;
    font-size: 11px;
    line-height: 1.8;
    color: #b09ba4;
}

#letter { display: none; }

.intro {
    text-align: center;
    padding: 8px 0 22px;
}

h2 {
    font-size: clamp(31px, 7vw, 44px);
    line-height: 1.22;
    letter-spacing: -1px;
    margin: 0 0 17px;
}

.prose {
    font-size: 14px;
    line-height: 2;
    color: #6d5561;
}

.prose p { margin: 0 0 17px; }

.prose strong {
    color: #a44e6c;
    font-weight: 700;
}

.section-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-weight: 700;
    color: #ae8293;
    margin-bottom: 17px;
    text-align: center;
}

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #efd8e0, transparent);
    margin: 29px 0;
}

.memory-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 10px;
}

.memory {
    position: relative;
    min-height: 140px;
    padding: 15px 9px;
    background: linear-gradient(145deg, #fff5f4, #f9e9f5);
    border: 1px solid #f4e0e8;
    border-radius: 20px;
    color: var(--ink);
    text-align: center;
    transition: transform .25s, background .25s;
}

.memory:hover { transform: translateY(-4px) rotate(-1deg); }
.memory .emoji { display: block; font-size: 25px; margin-bottom: 11px; }
.memory .m-title { display: block; font-weight: 700; font-size: 12px; }
.memory .m-tap { display: block; font-size: 10px; color: var(--muted); margin-top: 9px; }

.memory .reveal {
    display: none;
    font-size: 11px;
    line-height: 1.7;
    color: #91506a;
    margin-top: 10px;
}

.memory.open {
    background: #fff;
    border-color: #eac5d2;
}

.memory.open .reveal { display: block; }
.memory.open .m-tap { display: none; }

.compliment {
    text-align: center;
    padding: 23px 16px;
    background: linear-gradient(125deg, #fff0f3, #f7eefb);
    border: 1px solid #f6dfe8;
    border-radius: 22px;
}

.compliment .big-heart { font-size: 24px; }
.compliment p {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(18px, 4vw, 23px);
    line-height: 1.65;
    color: #75485d;
    margin: 12px 0 6px;
}
.compliment small { color: var(--muted); font-size: 11px; }

.coffee {
    background: white;
    border: 1px solid #f0dce3;
    border-radius: 24px;
    padding: 25px 17px;
    text-align: center;
}
.coffee-cup {
    font-size: 38px;
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0%,100% { transform: translateY(0) rotate(-3deg); }
    50% { transform: translateY(-7px) rotate(3deg); }
}
.coffee h2 { font-size: clamp(28px, 6vw, 37px); margin-top: 13px; }
.coffee p {
    color: var(--muted);
    font-size: 13px;
    line-height: 1.8;
    max-width: 390px;
    margin: 0 auto 17px;
}

.vibe-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    color: #a08491;
    font-weight: 700;
    margin: 18px 0 10px;
}

.vibes {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 8px;
}

.vibe {
    padding: 10px 12px;
    border: 1px solid #ead9e1;
    background: #fffafc;
    color: #725461;
    border-radius: 100px;
    font-size: 11px;
    transition: .2s;
}
.vibe.active {
    background: #f8dfe8;
    color: #93445f;
    border-color: #dea1b5;
    box-shadow: 0 3px 9px rgba(173,81,115,.10);
}

.choice-zone {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    height: 105px;
    margin: 12px 0 0;
    overflow: hidden;
    border-radius: 20px;
    background: #fffafd;
    border: 1px dashed #ecd4de;
}

.choice {
    min-width: 130px;
    padding: 14px 15px;
    border-radius: 14px;
    font-weight: 700;
    font-size: 12px;
    transition: left .18s ease, top .18s ease, transform .18s ease;
}

.yes {
    color: white;
    background: linear-gradient(110deg,#ad5574,#d68da6);
    border: 0;
    box-shadow: 0 7px 17px rgba(173,81,115,.19);
}
.yes:hover { transform: translateY(-2px); }

.no {
    color: #9b6479;
    background: white;
    border: 1px solid #eed4df;
}

.response {
    display: none;
    margin-top: 20px;
    padding: 19px;
    border-radius: 18px;
    background: #fff0f5;
    border: 1px solid #f2d5e0;
    text-align: center;
    animation: appear .45s ease;
}

.response h3 {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: 25px;
    color: #964b67;
    margin: 5px 0 10px;
    font-weight: 500;
}
.response p {
    color: #7c5b69;
    font-size: 13px;
    line-height: 1.8;
    margin: 0;
}
.response .r-emoji { font-size: 29px; }

.footer {
    text-align: center;
    font-size: 10px;
    color: #a8929c;
    line-height: 1.8;
    margin-top: 25px;
}

.float-heart {
    position: fixed;
    z-index: 20;
    pointer-events: none;
    animation: rise 2.4s ease-out forwards;
}
@keyframes rise {
    0% { opacity: 0; transform: translateY(0) scale(.6) rotate(0); }
    15% { opacity: 1; }
    100% { opacity: 0; transform: translateY(-240px) scale(1.3) rotate(25deg); }
}
@keyframes appear {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}

@media(max-width: 520px) {
    .app { padding: 22px 12px 30px; }
    .panel { padding: 23px 17px; border-radius: 24px; }
    .memory-grid { gap: 7px; }
    .memory { padding: 13px 5px; min-height: 135px; }
    .memory .m-title { font-size: 11px; }
    .memory .reveal { font-size: 10px; }
    .choice { min-width: 0; width: 45%; padding: 13px 5px; font-size: 11px; }
    .choice-zone { height: 110px; }
}
@media(prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        transition-duration: .01ms !important;
    }
}
</style>
</head>

<body>
<div class="app">

    <div class="topline"><span>♡</span> a tiny little something <span>♡</span></div>

    <!-- PASSWORD SCREEN -->
    <section id="gate" class="panel">
        <div class="center">
            <div class="sticker">💌</div>
            <div class="tag">not a boring text, promise</div>
            <h1>Hey, <em>Mitali.</em></h1>
            <p class="sub">
                I made you a tiny something instead of sending
                another long message. There's a little note inside.
                Open it whenever you're ready. 🌷
            </p>
        </div>

        <form id="password-form" class="input-wrap">
            <input
                id="password"
                type="password"
                placeholder="Your secret password..."
                autocomplete="off"
                aria-label="Password"
            >
            <button class="primary" type="submit">
                Open your little surprise ♡
            </button>
        </form>

        <div id="hint" class="hint">
            Hmm, not that one 🙈 Hint: try entering your name.
        </div>

        <p class="small-note center">
            made with a little courage & a lot of thought ✿
        </p>
    </section>

    <!-- MAIN PAGE -->
    <section id="letter" class="panel">

        <div class="intro">
            <div class="sticker">🌷</div>
            <div class="tag">from my heart, honestly</div>
            <h1>A little note<br>for <em>you.</em></h1>
            <p class="sub">
                Okay, no fancy speeches. Just a few things
                I wanted to tell you properly. ♡
            </p>
        </div>

        <div class="divider"></div>

        <div class="prose">
            <p>Hey Mitali,</p>

            <p>
                First of all, <strong>I'm genuinely sorry</strong>
                for the ways I hurt you or made you feel
                misunderstood. I can't change the past, but I
                wish I had understood things better at the time.
                I'm not asking you to forget anything.
            </p>

            <p>
                Tujhyasobat ghalavlela every single moment
                majhyasathi special hota. Even the smallest
                things still mean something to me. I think
                that's why some memories stay with us even
                when life changes.
            </p>

            <p>
                And honestly, there's something really special
                about you. Tujha smile, tu bolnyachi style,
                tujhya little expressions, ani tu agdi simple
                moments pan memorable banavtes. It's not just
                how you look — it's your vibe, your personality,
                and the person you are. I genuinely admire that.
            </p>

            <p>
                I know one message can't fix everything.
                I'm not expecting it to. I just wanted you to
                know that the good memories were real to me,
                and so was the care I had for you.
            </p>
        </div>

        <div class="divider"></div>

        <div class="section-label">♡ three tiny reminders</div>
        <div class="memory-grid">
            <button class="memory" onclick="toggleMemory(this)" aria-expanded="false">
                <span class="emoji">🌸</span>
                <span class="m-title">Your vibe</span>
                <span class="m-tap">tap to open ↗</span>
                <span class="reveal">Some people have a way of making ordinary moments feel a little more special. You do that.</span>
            </button>
            <button class="memory" onclick="toggleMemory(this)" aria-expanded="false">
                <span class="emoji">✨</span>
                <span class="m-title">Your smile</span>
                <span class="m-tap">tap to open ↗</span>
                <span class="reveal">It's one of those little things that can make a memory stick around much longer than expected.</span>
            </button>
            <button class="memory" onclick="toggleMemory(this)" aria-expanded="false">
                <span class="emoji">🫶</span>
                <span class="m-title">The little things</span>
                <span class="m-tap">tap to open ↗</span>
                <span class="reveal">Sometimes it's not the big moments, but the smallest things that end up meaning the most.</span>
            </button>
        </div>

        <div class="divider"></div>

        <div class="compliment">
            <div class="big-heart">♡</div>
            <p>
                "You don't have to try to be special.
                There's already something lovely about
                the way you are."
            </p>
            <small>just something I wanted you to know 🌷</small>
        </div>

        <div class="divider"></div>

        <section class="coffee">
            <div class="coffee-cup">☕</div>
            <div class="tag">one little question</div>
            <h2>Can I steal you<br>for <em>one coffee?</em></h2>

            <p>
                Just a simple coffee and a calm conversation.
                No dramatic expectations, no pressure to fix
                everything. We can just talk, if you're comfortable.
            </p>

            <div class="vibe-label">Choose the vibe ☁️</div>
            <div class="vibes">
                <button class="vibe active" onclick="chooseVibe(this, 'A cozy café')">☕ Cozy café</button>
                <button class="vibe" onclick="chooseVibe(this, 'Something cold')">🧋 Something cold</button>
                <button class="vibe" onclick="chooseVibe(this, 'An evening walk')">🌇 Evening walk</button>
            </div>

            <p id="vibe-caption" style="font-size:11px;margin-top:11px;margin-bottom:3px;">
                Current vibe: a cozy café ☕
            </p>

            <div class="choice-zone" id="choice-zone">
                <button id="yes-button" class="choice yes" onclick="answer('yes')">
                    YES, let's go ♡
                </button>
                <button id="no-button" class="choice no" onclick="answer('no')">
                    No, thank you
                </button>
            </div>

            <p style="font-size:10px;margin:12px 0 0;">
                P.S. The No button is a little shy 🙈
            </p>

            <div class="response" id="yes-response">
                <div class="r-emoji">🥹☕💗</div>
                <h3>Wait, really? ♡</h3>
                <p>
                    Okay, that made me smile. You can text me
                    whenever you're comfortable and we can
                    figure out a day and place together.
                    No rush at all.
                </p>
            </div>

            <div class="response" id="no-response">
                <div class="r-emoji">🌷</div>
                <h3>That's okay.</h3>
                <p>
                    Thank you for reading my little note.
                    I respect your answer, and you don't
                    need to explain anything. Take care. ♡
                </p>
            </div>
        </section>

        <p class="footer">
            made with care, just for this little moment ♡<br>
            Your choice matters. Always.
        </p>
    </section>
</div>

<script>
const form = document.getElementById("password-form");
const passwordInput = document.getElementById("password");
const hint = document.getElementById("hint");
const gate = document.getElementById("gate");
const letter = document.getElementById("letter");

form.addEventListener("submit", function(event) {
    event.preventDefault();

    if (passwordInput.value.trim().toLowerCase() === "mitali") {
        gate.style.display = "none";
        letter.style.display = "block";
        window.scrollTo({top: 0, behavior: "smooth"});
        launchHearts(5);
    } else {
        hint.style.display = "block";
        passwordInput.value = "";
        passwordInput.placeholder = "Try again 😉";
        passwordInput.focus();
    }
});

function toggleMemory(card) {
    const isOpen = card.classList.toggle("open");
    card.setAttribute("aria-expanded", String(isOpen));
    if (isOpen) launchHearts(1);
}

let selectedVibe = "A cozy café";

function chooseVibe(button, vibe) {
    selectedVibe = vibe;
    document.querySelectorAll(".vibe").forEach(function(item) {
        item.classList.remove("active");
    });
    button.classList.add("active");
    document.getElementById("vibe-caption").textContent =
        "Current vibe: " + vibe + " ♡";
}

let noMoves = 0;
const maxMoves = 3;
const noButton = document.getElementById("no-button");
const zone = document.getElementById("choice-zone");

function dodgeNo() {
    if (noMoves >= maxMoves) return;

    noMoves++;

    const zoneRect = zone.getBoundingClientRect();
    const buttonWidth = noButton.offsetWidth;
    const buttonHeight = noButton.offsetHeight;

    // Keep the button inside the visible choice area.
    const maxLeft = Math.max(5, zoneRect.width - buttonWidth - 8);
    const maxTop = Math.max(5, zoneRect.height - buttonHeight - 8);

    // Use a few playful, predictable hops instead of trapping the user.
    const spots = [
        [0.56, 0.12],
        [0.08, 0.58],
        [0.54, 0.58]
    ];

    const spot = spots[Math.min(noMoves - 1, spots.length - 1)];

    noButton.style.position = "absolute";
    noButton.style.left = Math.min(maxLeft, Math.max(5, maxLeft * spot[0])) + "px";
    noButton.style.top = Math.min(maxTop, Math.max(5, maxTop * spot[1])) + "px";
    noButton.style.width = Math.min(buttonWidth, zoneRect.width * 0.45) + "px";

    if (noMoves >= maxMoves) {
        noButton.style.transform = "none";
        noButton.textContent = "No, thank you";
        noButton.title = "You can choose this option.";
    }
}

noButton.addEventListener("pointerenter", function(event) {
    if (event.pointerType === "mouse" && noMoves < maxMoves) {
        dodgeNo();
    }
});

noButton.addEventListener("pointerdown", function(event) {
    if (event.pointerType !== "mouse" && noMoves < maxMoves) {
        event.preventDefault();
        dodgeNo();
    }
});

function answer(choice) {
    document.getElementById("yes-response").style.display =
        choice === "yes" ? "block" : "none";

    document.getElementById("no-response").style.display =
        choice === "no" ? "block" : "none";

    if (choice === "yes") {
        document.getElementById("yes-response").querySelector("p").textContent =
            "Okay, that made me smile. You can text me whenever you're comfortable and we can figure out " +
            selectedVibe.toLowerCase() +
            " together. No rush at all.";
        launchHearts(18);
    }

    setTimeout(function() {
        const response = document.getElementById(
            choice === "yes" ? "yes-response" : "no-response"
        );
        response.scrollIntoView({behavior: "smooth", block: "nearest"});
    }, 60);
}

function launchHearts(count) {
    const symbols = ["♡", "♥", "✿", "💕", "✨"];

    for (let i = 0; i < count; i++) {
        setTimeout(function() {
            const heart = document.createElement("span");
            heart.className = "float-heart";
            heart.textContent = symbols[Math.floor(Math.random() * symbols.length)];
            heart.style.left = (8 + Math.random() * 84) + "vw";
            heart.style.top = (55 + Math.random() * 38) + "vh";
            heart.style.color = ["#d4839e", "#b474b5", "#e8a3b7"][Math.floor(Math.random() * 3)];
            heart.style.fontSize = (14 + Math.random() * 18) + "px";
            document.body.appendChild(heart);
            setTimeout(function() { heart.remove(); }, 2500);
        }, i * 70);
    }
}
</script>
</body>
</html>
"""

components.html(APP_HTML, height=1450, scrolling=True)
