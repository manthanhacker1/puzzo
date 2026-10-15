import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little Surprise 🎁",
    page_icon="🎁",
    layout="centered",
    initial_sidebar_state="collapsed"
)

components.html(r"""
<!DOCTYPE html>
<html>
<head>

<meta charset="UTF-8">
<meta name="viewport"
      content="width=device-width,
               initial-scale=1.0,
               maximum-scale=1.0,
               user-scalable=no">

<style>

* {
    box-sizing: border-box;
    -webkit-tap-highlight-color: transparent;
}

html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100%;
}

body {
    min-height: 100svh;

    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "SF Pro Display",
        "Segoe UI",
        sans-serif;

    color: #fff;

    background:
        radial-gradient(
            circle at 15% 10%,
            rgba(255, 85, 145, .20),
            transparent 32%
        ),
        radial-gradient(
            circle at 90% 90%,
            rgba(160, 80, 255, .14),
            transparent 30%
        ),
        linear-gradient(
            160deg,
            #08070b 0%,
            #130b13 55%,
            #09070b 100%
        );

    display: flex;
    align-items: center;
    justify-content: center;

    padding:
        max(18px, env(safe-area-inset-top))
        16px
        max(18px, env(safe-area-inset-bottom))
        16px;

    overflow-x: hidden;
}


/* MAIN CARD */

.card {

    width: 100%;
    max-width: 430px;

    padding: 30px 20px 26px;

    border-radius: 30px;

    background:
        rgba(255,255,255,.055);

    border:
        1px solid rgba(255,255,255,.10);

    box-shadow:
        0 25px 70px rgba(0,0,0,.55);

    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);

    text-align: center;

    animation: enter .45s ease;

}

@keyframes enter {

    from {
        opacity: 0;
        transform: translateY(15px) scale(.98);
    }

    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }

}


/* ICON */

.icon {

    font-size: 54px;

    line-height: 1;

    margin-bottom: 18px;

    animation:
        float 3s ease-in-out infinite;

}

@keyframes float {

    50% {
        transform: translateY(-6px);
    }

}


/* TYPOGRAPHY */

h1 {

    margin: 0 0 12px;

    font-size: clamp(30px, 9vw, 38px);

    line-height: 1.08;

    letter-spacing: -1.2px;

}

.subtitle {

    color: #b8aeb9;

    font-size: 15px;

    line-height: 1.55;

    margin:
        0 auto 24px;

    max-width: 350px;

}

.gradient {

    background:
        linear-gradient(
            90deg,
            #ff5c91,
            #ffb4ca
        );

    -webkit-background-clip: text;
    background-clip: text;

    color: transparent;

}


/* PASSWORD AREA */

input {

    width: 100%;

    height: 56px;

    padding: 0 16px;

    border-radius: 16px;

    border:
        1px solid rgba(255,255,255,.13);

    background:
        rgba(0,0,0,.28);

    color: white;

    outline: none;

    font-family: inherit;

    font-size: 17px;

    text-align: center;

    -webkit-appearance: none;

    margin-bottom: 12px;

}

input:focus {

    border-color: #ff6496;

    box-shadow:
        0 0 0 3px
        rgba(255,100,150,.10);

}


/* PRIMARY BUTTON */

button {

    width: 100%;

    min-height: 56px;

    padding: 14px 18px;

    border: none;

    border-radius: 16px;

    font-family: inherit;

    font-size: 16px;

    font-weight: 750;

    color: white;

    background:
        linear-gradient(
            135deg,
            #ff477f,
            #ff709e
        );

    box-shadow:
        0 12px 28px
        rgba(255,70,125,.20);

    cursor: pointer;

    touch-action: manipulation;

    transition:
        transform .15s ease,
        opacity .15s ease;

}

button:active {

    transform: scale(.97);

}


/* ERROR */

.error {

    display: none;

    margin-top: 14px;

    padding: 12px 14px;

    border-radius: 14px;

    color: #ffadb9;

    background:
        rgba(255,70,90,.08);

    border:
        1px solid
        rgba(255,70,90,.15);

    font-size: 14px;

}


/* BIG HINT */

.hint {

    display: none;

    margin-top: 16px;

    padding: 18px 15px;

    border-radius: 18px;

    background:
        linear-gradient(
            145deg,
            rgba(255,186,70,.12),
            rgba(255,120,70,.06)
        );

    border:
        1px solid
        rgba(255,190,90,.24);

}


/* THIS IS THE IMPORTANT PART */

.hint-label {

    font-size: 12px;

    letter-spacing: 1.5px;

    color: #ffc76f;

    font-weight: 800;

    margin-bottom: 6px;

}

.hint-main {

    font-size: 24px;

    line-height: 1.15;

    font-weight: 900;

    color: #fff;

}

.hint-sub {

    margin-top: 7px;

    color: #c9bec8;

    font-size: 13px;

}


/* PAGES */

.page {

    display: none;

}


/* REWARDS */

.rewards {

    display: grid;

    grid-template-columns:
        1fr 1fr;

    gap: 10px;

    margin:
        20px 0 14px;

}

.reward {

    min-height: 125px;

    padding: 17px 10px;

    border-radius: 18px;

    border:
        1px solid
        rgba(255,255,255,.09);

    background:
        rgba(255,255,255,.045);

    display: flex;

    flex-direction: column;

    justify-content: center;

    align-items: center;

    cursor: pointer;

    touch-action: manipulation;

    transition:
        transform .15s ease,
        border-color .15s ease,
        background .15s ease;

}

.reward:active {

    transform: scale(.97);

}

.reward.selected {

    border-color:
        rgba(255,100,150,.75);

    background:
        rgba(255,90,145,.11);

    box-shadow:
        0 8px 28px
        rgba(255,80,130,.12);

}

.reward-icon {

    font-size: 31px;

    margin-bottom: 8px;

}

.reward-title {

    font-size: 14px;

    font-weight: 800;

}

.reward-desc {

    color: #918792;

    font-size: 11px;

    line-height: 1.35;

    margin-top: 5px;

}


/* RESULT */

.result {

    display: none;

    margin-top: 15px;

    padding: 16px;

    border-radius: 17px;

    background:
        rgba(255,255,255,.055);

    color: #ddd4dc;

    font-size: 14px;

    line-height: 1.55;

}


/* SMALL */

.small {

    margin-top: 18px;

    color: #756d77;

    font-size: 11px;

}


/* HEARTS */

.heart {

    position: fixed;

    bottom: -40px;

    z-index: 999;

    pointer-events: none;

    font-size: 20px;

    animation:
        fly 3s linear forwards;

}

@keyframes fly {

    0% {
        transform:
            translateY(0)
            scale(.5);
        opacity: 0;
    }

    20% {
        opacity: 1;
    }

    100% {
        transform:
            translateY(-110vh)
            rotate(360deg);
        opacity: 0;
    }

}


/* MOBILE */

@media (max-width: 380px) {

    .card {
        padding:
            25px 16px;
    }

    h1 {
        font-size: 30px;
    }

    .reward {
        min-height: 118px;
    }

}

</style>

</head>

<body>


<!-- ================================================= -->
<!-- STEP 1 — SECRET -->
<!-- ================================================= -->

<div class="card" id="unlock">

    <div class="icon">
        🎁
    </div>

    <h1>
        You found it.
    </h1>

    <p class="subtitle">

        There's a tiny surprise waiting
        for the person who opened this.

        <br><br>

        But first... one little question 👀

    </p>


    <input
        id="password"
        type="text"
        inputmode="text"
        autocomplete="off"
        autocapitalize="words"
        placeholder="Enter password"
    >


    <button onclick="checkPassword()">
        Open surprise ✨
    </button>


    <div
        id="error"
        class="error">
    </div>


    <!-- BIG CLEAR HINT -->

    <div
        id="hint"
        class="hint">

        <div class="hint-label">
            💡 ONE LAST HINT
        </div>

        <div class="hint-main">
            ENTER YOUR NAME
        </div>

        <div class="hint-sub">
            Yep... literally your name 😭
        </div>

    </div>


    <div class="small">
        No complicated password. Promise.
    </div>

</div>


<!-- ================================================= -->
<!-- STEP 2 — GIFT -->
<!-- ================================================= -->

<div
    class="card page"
    id="gift">

    <div class="icon">
        🎀
    </div>

    <h1>
        A little something
        for
        <span
            id="name"
            class="gradient">
        </span>
    </h1>


    <p class="subtitle">

        You unlocked your gift.

        <br><br>

        Now you get to choose
        what I owe you. 😌

    </p>


    <div class="rewards">


        <div
            class="reward"
            onclick="
                chooseReward(
                    this,
                    'Coffee date ☕'
                )
            ">

            <div class="reward-icon">
                ☕
            </div>

            <div class="reward-title">
                Coffee date
            </div>

            <div class="reward-desc">
                Coffee + good conversation.
            </div>

        </div>


        <div
            class="reward"
            onclick="
                chooseReward(
                    this,
                    'Food date 🍝'
                )
            ">

            <div class="reward-icon">
                🍝
            </div>

            <div class="reward-title">
                Food date
            </div>

            <div class="reward-desc">
                You choose what we eat.
            </div>

        </div>


        <div
            class="reward"
            onclick="
                chooseReward(
                    this,
                    'Dessert date 🍰'
                )
            ">

            <div class="reward-icon">
                🍰
            </div>

            <div class="reward-title">
                Dessert date
            </div>

            <div class="reward-desc">
                Something sweet. Obviously.
            </div>

        </div>


        <div
            class="reward"
            onclick="
                chooseReward(
                    this,
                    'Surprise date ✨'
                )
            ">

            <div class="reward-icon">
                ✨
            </div>

            <div class="reward-title">
                Surprise me
            </div>

            <div class="reward-desc">
                I'll plan it. No spoilers.
            </div>

        </div>


    </div>


    <button onclick="claimGift()">
        Claim my gift 💌
    </button>


    <div
        id="giftResult"
        class="result">
    </div>

</div>


<!-- ================================================= -->
<!-- STEP 3 — DATE -->
<!-- ================================================= -->

<div
    class="card page"
    id="final">

    <div class="icon">
        💌
    </div>


    <h1>

        Okay,
        <span
            id="finalName"
            class="gradient">
        </span>...

    </h1>


    <p class="subtitle">

        Your
        <span id="finalReward">
        </span>
        is officially claimed.

        <br><br>

        Now there's just one tiny thing
        left to decide...

    </p>


    <div
        style="
        font-size:23px;
        line-height:1.3;
        font-weight:800;
        margin:25px 0;
        ">

        Should we actually
        make this happen? 👀

    </div>


    <button onclick="yesDate()">
        Let's do it ❤️
    </button>


    <div
        id="finalResult"
        class="result">
    </div>


    <div class="small">
        No pressure. Just a cute excuse to meet. ✨
    </div>

</div>


<script>


/* ================================================= */
/* STATE */
/* ================================================= */

let attempts = 0;

let personName = "";

let selectedReward = "";


/* ================================================= */
/* NAME VALIDATION */
/* ================================================= */

/*
   Accept:

   Sarah
   Priya
   Mary Jane
   Anne-Marie
   O'Connor

   Reject:

   12345
   abc123
   !!!
   123
*/

function validName(name) {

    const cleaned =
        name.trim();


    if (cleaned.length < 2) {
        return false;
    }


    /*
       At least TWO letters.
    */

    const letters =
        cleaned.match(/[A-Za-z]/g);


    if (!letters || letters.length < 2) {
        return false;
    }


    /*
       Only normal name characters.
    */

    const validCharacters =
        /^[A-Za-zÀ-ÖØ-öø-ÿ' -]+$/;


    if (
        !validCharacters.test(cleaned)
    ) {
        return false;
    }


    return true;

}


/* ================================================= */
/* UNLOCK */
/* ================================================= */

function checkPassword() {

    const input =
        document
        .getElementById("password")
        .value
        .trim();


    const error =
        document
        .getElementById("error");


    const hint =
        document
        .getElementById("hint");


    error.style.display = "none";


    if (!input) {

        error.style.display = "block";

        error.innerHTML =
            "❌ Enter something first 😭";

        return;

    }


    /*
       FIRST ATTEMPT:

       ALWAYS WRONG.

       This gives the intended
       password → hint experience.
    */

    if (attempts === 0) {

        attempts++;

        error.style.display =
            "block";

        error.innerHTML =
            "❌ Nope... that's not it 😭";

        hint.style.display =
            "block";

        return;

    }


    /*
       SECOND+ ATTEMPTS:

       NOW ACTUALLY VALIDATE
       THAT IT LOOKS LIKE A NAME.
    */

    if (!validName(input)) {

        error.style.display =
            "block";

        error.innerHTML =
            "❌ That's not a name 😭<br>" +
            "Use your actual first name.";

        hint.style.display =
            "block";

        document
            .getElementById("password")
            .select();

        return;

    }


    /*
       VALID NAME
    */

    personName = input;


    document
        .getElementById("unlock")
        .style.display = "none";


    document
        .getElementById("gift")
        .style.display = "block";


    document
        .getElementById("name")
        .textContent = personName;

}


/* ================================================= */
/* REWARD */
/* ================================================= */

function chooseReward(
    element,
    reward
) {

    document
        .querySelectorAll(".reward")
        .forEach(
            function(item) {

                item.classList
                    .remove("selected");

            }
        );


    element.classList
        .add("selected");


    selectedReward =
        reward;

}


/* ================================================= */
/* CLAIM */
/* ================================================= */

function claimGift() {

    const result =
        document
        .getElementById("giftResult");


    if (!selectedReward) {

        result.style.display =
            "block";

        result.innerHTML =
            "Pick your gift first 😌";

        return;

    }


    result.style.display =
        "block";


    result.innerHTML = `

        🎁

        <br>

        <b>
            ${selectedReward}
        </b>

        <br><br>

        Good choice,
        ${escapeHTML(personName)} 😌

        <br><br>

        <button
            onclick="openFinal()"
            style="
                margin-top:4px;
            ">

            Okay, what's next? 👀

        </button>

    `;

}


/* ================================================= */
/* FINAL */
/* ================================================= */

function openFinal() {

    document
        .getElementById("gift")
        .style.display = "none";


    document
        .getElementById("final")
        .style.display = "block";


    document
        .getElementById("finalName")
        .textContent =
            personName;


    document
        .getElementById("finalReward")
        .textContent =
            selectedReward;

}


/* ================================================= */
/* YES */
/* ================================================= */

function yesDate() {

    createHearts();


    const result =
        document
        .getElementById("finalResult");


    result.style.display =
        "block";


    result.innerHTML = `

        <div style="
            font-size:38px;
            margin-bottom:8px;
        ">
            🥹❤️
        </div>

        <b>
            It's a date.
        </b>

        <br><br>

        ${selectedReward}

        <br><br>

        I'll see you soon,
        ${escapeHTML(personName)}. ✨

    `;

}


/* ================================================= */
/* HEARTS */
/* ================================================= */

function createHearts() {

    const emojis =
        [
            "❤️",
            "💗",
            "💕",
            "💖",
            "💘"
        ];


    for (
        let i = 0;
        i < 25;
        i++
    ) {

        const heart =
            document
            .createElement("div");


        heart.className =
            "heart";


        heart.innerHTML =
            emojis[
                Math.floor(
                    Math.random() *
                    emojis.length
                )
            ];


        heart.style.left =
            Math.random() *
            100 +
            "vw";


        heart.style.animationDelay =
            Math.random() *
            .8 +
            "s";


        document
            .body
            .appendChild(heart);


        setTimeout(
            function() {
                heart.remove();
            },
            3500
        );

    }

}


/* ================================================= */
/* BASIC HTML ESCAPING */
/* ================================================= */

function escapeHTML(text) {

    const div =
        document
        .createElement("div");

    div.textContent = text;

    return div.innerHTML;

}


/* ================================================= */
/* ENTER KEY */
/* ================================================= */

document
    .getElementById("password")
    .addEventListener(
        "keydown",
        function(event) {

            if (
                event.key === "Enter"
            ) {

                checkPassword();

            }

        }
    );

</script>

</body>
</html>
""", height=900, scrolling=False)
