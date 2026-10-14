
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
    background: #0b0912;
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

<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;1,500&display=swap" rel="stylesheet">

<style>
* { box-sizing: border-box; }

:root {
    --ink: #f7edf5;
    --muted: #b7a5c0;
    --pink: #ff9fc7;
    --deep: #f06cae;
    --line: #403044;
}

html {
    scroll-behavior: smooth;
    background: #0b0912;
}

body {
    margin: 0;
    min-height: 100vh;
    color: var(--ink);
    font-family: 'DM Sans', sans-serif;
    background:
        radial-gradient(ellipse at 5% 5%,
            rgba(139, 52, 111, .24), transparent 38%),
        radial-gradient(ellipse at 100% 55%,
            rgba(88, 55, 155, .24), transparent 38%),
        linear-gradient(145deg, #0b0912, #15101f 55%, #100c1b);
}

button, input { font: inherit; }
button { cursor: pointer; -webkit-tap-highlight-color: transparent; }

.app {
    width: 100%;
    max-width: 720px;
    margin: auto;
    padding: 28px 16px 44px;
}

.topline {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 9px;
    color: #c2afca;
    font-size: 10px;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 25px;
}

.topline span {
    color: #ff8fbc;
    font-size: 19px;
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
    background: rgba(24, 19, 34, .94);
    border: 1px solid rgba(241, 176, 216, .14);
    border-radius: 28px;
    padding: clamp(21px, 5vw, 40px);
    box-shadow:
        0 24px 70px rgba(0, 0, 0, .35),
        0 0 35px rgba(143, 63, 137, .08);
    backdrop-filter: blur(18px);
}

.panel::before {
    content: "";
    position: absolute;
    width: 190px;
    height: 190px;
    right: -95px;
    top: -110px;
    background: rgba(160, 73, 143, .13);
    border-radius: 50%;
    pointer-events: none;
}

.center { text-align: center; }

.sticker {
    width: 72px;
    height: 72px;
    display: grid;
    place-items: center;
    margin: 5px auto 21px;
    border-radius: 23px;
    font-size: 34px;
    background: linear-gradient(145deg, #43223f, #282043);
    border: 1px solid rgba(255, 166, 212, .14);
    box-shadow: 0 10px 30px rgba(217, 90, 170, .13);
    transform: rotate(-5deg);
}

h1, h2, h3 {
    font-family: 'Playfair Display', Georgia, serif;
    font-weight: 500;
}

h1 {
    color: #fff2fa;
    font-size: clamp(35px, 8vw, 56px);
    line-height: 1.13;
    letter-spacing: -1.5px;
    margin: 0 0 15px;
}

h1 em, h2 em {
    color: var(--pink);
    font-weight: 500;
}

.sub {
    color: var(--muted);
    font-size: 14px;
    line-height: 1.9;
    max-width: 420px;
    margin: 0 auto 26px;
}

.tag {
    display: inline-block;
    padding: 8px 13px;
    border-radius: 50px;
    background: #2e1c31;
    color: #ffadd0;
    border: 1px solid #55304e;
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
    width: 100%;
    display: block;
    padding: 16px;
    margin-bottom: 12px;
    border-radius: 14px;
    border: 1px solid #463047;
    background: #110e19;
    color: white;
    text-align: center;
    font-size: 15px;
    outline: none;
}

.input-wrap input::placeholder { color: #8f7c98; }

.input-wrap input:focus {
    border-color: #dc81b4;
    box-shadow: 0 0 0 4px rgba(220, 129, 180, .12);
}

button:focus-visible, input:focus-visible {
    outline: 2px solid #ff9fc7;
    outline-offset: 3px;
}

.primary {
    width: 100%;
    border: none;
    border-radius: 14px;
    padding: 16px;
    color: white;
    background: linear-gradient(110deg, #9c397b, #d45c98);
    font-size: 14px;
    font-weight: 700;
    box-shadow: 0 8px 28px rgba(190, 66, 147, .22);
    transition: transform .2s, box-shadow .2s;
}

.primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 34px rgba(190, 66, 147, .35);
}

.hint {
    display: none;
    max-width: 390px;
    margin: 13px auto 0;
    padding: 12px;
    border-radius: 12px;
    color: #ffafd0;
    background: #2a1728;
    border: 1px solid #64324e;
    font-size: 13px;
    text-align: center;
}

.small-note, .footer {
    color: #92809d;
    text-align: center;
    font-size: 11px;
    line-height: 1.8;
}

.small-note { margin-top: 22px; }

#letter { display: none; }

.intro {
    text-align: center;
    padding: 8px 0 20px;
}

h2 {
    font-size: clamp(29px, 7vw, 42px);
    line-height: 1.25;
    letter-spacing: -.7px;
    color: #fff2fa;
    margin: 0 0 15px;
}

.prose {
    color: #d2c1d5;
    font-size: 14px;
    line-height: 2;
}

.prose p { margin: 0 0 17px; }
.prose strong { color: #ffa3ca; }

.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #55334e, transparent);
    margin: 28px 0;
}

.section-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-weight: 700;
    color: #d99bc7;
    margin-bottom: 16px;
    text-align: center;
}

.memory-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 9px;
}

.memory {
    min-width: 0;
    min-height: 145px;
    padding: 14px 8px;
    background: linear-gradient(145deg, #25192d, #201a32);
    border: 1px solid #443047;
    border-radius: 18px;
    color: #f7eaf7;
    text-align: center;
    transition: transform .25s, border-color .25s;
}

.memory:hover {
    transform: translateY(-3px);
    border-color: #8f497e;
}

.memory.open {
    background: #211a30;
    border-color: #b46c9e;
}

.memory .emoji {
    display: block;
    font-size: 25px;
    margin-bottom: 10px;
}

.memory .m-title {
    display: block;
    font-weight: 700;
    font-size: 11px;
}

.memory .m-tap {
    display: block;
    color: #ad96b6;
    font-size: 10px;
    margin-top: 9px;
}

.memory .reveal {
    display: none;
    margin-top: 10px;
    color: #e3b5d3;
    font-size: 10px;
    line-height: 1.7;
}

.memory.open .reveal { display: block; }
.memory.open .m-tap { display: none; }

.compliment {
    text-align: center;
    padding: 23px 16px;
    background: linear-gradient(125deg, #2e1a30, #201b3b);
    border: 1px solid #54304f;
    border-radius: 22px;
}

.compliment .big-heart { font-size: 25px; }

.compliment p {
    font-family: 'Playfair Display', Georgia, serif;
    font-size: clamp(18px, 4vw, 23px);
    line-height: 1.65;
    color: #ffd3e8;
    margin: 12px 0 7px;
}

.compliment small { color: #bca2c2; font-size: 11px; }

.coffee {
    background: linear-gradient(145deg, #1e1729, #171321);
    border: 1px solid #493047;
    border-radius: 23px;
    padding: 24px 15px;
    text-align: center;
}

.coffee-cup {
    font-size: 39px;
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0%, 100% { transform: translateY(0) rotate(-3deg); }
    50% { transform: translateY(-7px) rotate(3deg); }
}

.coffee h2 {
    font-size: clamp(28px, 6vw, 38px);
    margin-top: 12px;
}

.coffee p {
    color: #bcaabe;
    font-size: 13px;
    line-height: 1.8;
    max-width: 410px;
    margin: 0 auto 17px;
}

.vibe-label {
    font-size: 10px;
    text-transform: uppercase;
    letter-spacing: 1.4px;
    color: #c2a3c6;
    font-weight: 700;
    margin: 20px 0 10px;
}

.vibes {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 8px;
}

.vibe {
    padding: 10px 12px;
    border: 1px solid #453047;
    background: #211829;
    color: #e4cde3;
    border-radius: 100px;
    font-size: 11px;
    transition: .2s;
}

.vibe.active {
    background: #49243f;
    color: #ffb7d8;
    border-color: #c65d9d;
    box-shadow: 0 0 16px rgba(198, 93, 157, .12);
}

#vibe-caption { color: #c0a9c8 !important; }

.choice-zone {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    min-height: 93px;
    margin-top: 15px;
    padding: 10px;
    border-radius: 19px;
    background: #120e1a;
    border: 1px dashed #67415f;
}

.choice {
    flex: 1;
    max-width: 220px;
    min-height: 49px;
    padding: 14px 10px;
    border-radius: 14px;
    font-weight: 700;
    font-size: 12px;
}

.yes {
    color: white;
    border: 0;
    background: linear-gradient(110deg, #a13f82, #db609b);
    box-shadow: 0 6px 22px rgba(204, 66, 151, .25);
    animation: yesPulse 2s infinite;
    transition: transform .2s, box-shadow .2s;
}

.yes:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 8px 32px rgba(204, 66, 151, .45);
}

@keyframes yesPulse {
    0%, 100% {
        box-shadow: 0 0 12px rgba(255, 105, 173, .18);
    }
    50% {
        box-shadow: 0 0 26px rgba(255, 105, 173, .46);
    }
}

.no {
    color: #e5bfdc;
    background: #251a2c;
    border: 1px solid #69405e;
    transition: background .2s, border-color .2s;
}

.no:hover {
    background: #302039;
    border-color: #a75b8e;
}

.response {
    display: none;
    margin-top: 20px;
    padding: 20px 15px;
    border-radius: 18px;
    background: linear-gradient(130deg, #301c34, #251b3b);
    border: 1px solid #684064;
    text-align: center;
    animation: appear .4s ease;
}

.response h3 {
    font-size: 25px;
    color: #ffafd1;
    margin: 8px 0 10px;
}

.response p {
    color: #dfc9e2;
    font-size: 13px;
    line-height: 1.8;
    margin: 0;
}

.r-emoji { font-size: 29px; }

.footer {
    color: #95819f;
    margin-top: 25px;
}

.float-heart {
    position: fixed;
    z-index: 20;
    pointer-events: none;
    animation: rise 2.4s ease-out forwards;
}

@keyframes rise {
    0% { opacity: 0; transform: translateY(0) scale(.6); }
    15% { opacity: 1; }
    100% {
        opacity: 0;
        transform: translateY(-240px) scale(1.3) rotate(25deg);
    }
}

@keyframes appear {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}

@media(max-width: 450px) {
    .app { padding: 20px 10px 30px; }
    .panel { padding: 22px 14px; border-radius: 23px; }
    .memory-grid { gap: 6px; }
    .memory { padding: 12px 4px; min-height: 140px; }
    .memory .m-title { font-size: 10px; }
    .choice { padding: 13px 5px; font-size: 11px; }
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

    <div class="topline">
        <span>♡</span> a tiny little something <span>♡</span>
    </div>

    <!-- PASSWORD SCREEN -->
    <section id="gate" class="panel">
        <div class="center">
            <div class="sticker">💌</div>
            <div class="tag">not a boring text, promise</div>
            <h1>Hey, <em>Mitali.</em></h1>
            <p class="sub">
                I made you a little something instead of sending
                another long message. There's a tiny note inside.
                Open it whenever you're ready. 🌷
            </p>
        </div>

        <form id="password-form" class="input-wrap">
            <input id="password"
                   type="password"
                   placeholder="Your secret password..."
                   autocomplete="off"
                   aria-label="Password">

            <button class="primary" type="submit">
                Open your little surprise ♡
            </button>
        </form>

        <div id="hint" class="hint">
            Hmm, not that one 🙈 Hint: try entering your name.
        </div>

        <p class="small-note">
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
                No fancy speeches. Just a few things I wanted
                to tell you properly. ♡
            </p>
        </div>

        <div class="divider"></div>

        <div class="prose">
            <p>Hey Mitali,</p>

            <p>
                First of all, <strong>I'm genuinely sorry</strong>
                for the ways I hurt you or made you feel
                misunderstood. I can't change the past, but I
                wish I'd understood things better at the time.
                I'm not asking you to forget anything.
            </p>

            <p>
                Tujhyasobat ghalavlela every single moment
                majhyasathi special hota. Even the smallest
                things still mean something to me. Some memories
                stay with us even when life changes.
            </p>

            <p>
                There's something genuinely special about you.
                Tujha smile, tu bolnyachi style, tujhya little
                expressions, ani tu simple moments pan memorable
                banavtes. It's your vibe, your personality,
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
            <button class="memory"
                    onclick="toggleMemory(this)"
                    aria-expanded="false">
                <span class="emoji">🌸</span>
                <span class="m-title">Your vibe</span>
                <span class="m-tap">tap to open ↗</span>
                <span class="reveal">
                    You have a way of making ordinary moments
                    feel a little more special.
                </span>
            </button>

            <button class="memory"
                    onclick="toggleMemory(this)"
                    aria-expanded="false">
                <span class="emoji">✨</span>
                <span class="m-title">Your smile</span>
                <span class="m-tap">tap to open ↗</span>
                <span class="reveal">
                    It's one of those little things that makes
                    a memory stick around.
                </span>
            </button>

            <button class="memory"
                    onclick="toggleMemory(this)"
                    aria-expanded="false">
                <span class="emoji">🫶</span>
                <span class="m-title">Little things</span>
                <span class="m-tap">tap to open ↗</span>
                <span class="reveal">
                    Sometimes the smallest moments end up
                    meaning the most.
                </span>
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
                No dramatic expectations and no pressure.
                We can just talk, if you're comfortable.
            </p>

            <div class="vibe-label">Choose the vibe ☁️</div>

            <div class="vibes">
                <button class="vibe active"
                        onclick="chooseVibe(this, 'A cozy café')">
                    ☕ Cozy café
                </button>
                <button class="vibe"
                        onclick="chooseVibe(this, 'Something cold')">
                    🧋 Something cold
                </button>
                <button class="vibe"
                        onclick="chooseVibe(this, 'An evening walk')">
                    🌇 Evening walk
                </button>
            </div>

            <p id="vibe-caption"
               style="font-size:11px;margin-top:12px;margin-bottom:4px;">
                Current vibe: A cozy café ♡
            </p>

            <div class="choice-zone">
                <button class="choice yes"
                        onclick="answer('yes')">
                    YES, let's go ♡
                </button>

                <button class="choice no"
                        onclick="answer('no')">
                    No, thank you
                </button>
            </div>

            <div class="response" id="yes-response">
                <div class="r-emoji">🥹☕💗</div>
                <h3>Wait, really? ♡</h3>
                <p id="yes-message">
                    Okay, that made me smile. Let's figure out
                    a day and place together whenever you're
                    comfortable. No rush at all.
                </p>
            </div>

            <div class="response" id="no-response">
                <div class="r-emoji">🌷</div>
                <h3>That's okay.</h3>
                <p>
                    Thank you for reading my little note.
                    I respect your answer. Take care. ♡
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
        launchHearts(7);
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
    if (isOpen) launchHearts(2);
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

function answer(choice) {
    const yesResponse = document.getElementById("yes-response");
    const noResponse = document.getElementById("no-response");

    yesResponse.style.display = "none";
    noResponse.style.display = "none";

    if (choice === "yes") {
        document.getElementById("yes-message").textContent =
            "Okay, that made me smile. Let's figure out " +
            selectedVibe.toLowerCase() +
            " together whenever you're comfortable. No rush at all.";

        yesResponse.style.display = "block";
        launchHearts(24);
    } else {
        noResponse.style.display = "block";
    }

    const response = choice === "yes" ? yesResponse : noResponse;

    setTimeout(function() {
        response.scrollIntoView({
            behavior: "smooth",
            block: "nearest"
        });
    }, 80);
}

function launchHearts(count) {
    const symbols = ["♡", "♥", "✿", "💕", "✨"];

    for (let i = 0; i < count; i++) {
        setTimeout(function() {
            const heart = document.createElement("span");
            heart.className = "float-heart";

            heart.textContent =
                symbols[Math.floor(Math.random() * symbols.length)];

            heart.style.left = (8 + Math.random() * 84) + "vw";
            heart.style.top = (55 + Math.random() * 38) + "vh";

            heart.style.color = [
                "#ff9fc7", "#dca0f0", "#f49ac4"
            ][Math.floor(Math.random() * 3)];

            heart.style.fontSize = (14 + Math.random() * 18) + "px";

            document.body.appendChild(heart);

            setTimeout(function() {
                heart.remove();
            }, 2500);
        }, i * 65);
    }
}
</script>

</body>
</html>
"""

components.html(APP_HTML, height=2600, scrolling=True)
