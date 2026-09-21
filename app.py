import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little Surprise 🎁",
    page_icon="🎁",
    layout="centered"
)

components.html("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>

* {
    box-sizing: border-box;
}

body {
    margin: 0;
    min-height: 100vh;

    font-family:
        -apple-system,
        BlinkMacSystemFont,
        "Inter",
        "Segoe UI",
        sans-serif;

    background:
        radial-gradient(
            circle at 15% 15%,
            rgba(255, 103, 154, .18),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 85%,
            rgba(170, 100, 255, .15),
            transparent 30%
        ),
        #0b080d;

    color: white;

    display: flex;
    justify-content: center;
    align-items: center;

    padding: 18px;
}


/* CARD */

.card {

    width: min(470px, 100%);

    padding: 32px 25px;

    border-radius: 28px;

    background:
        linear-gradient(
            145deg,
            rgba(255,255,255,.075),
            rgba(255,255,255,.035)
        );

    border:
        1px solid rgba(255,255,255,.10);

    box-shadow:
        0 30px 80px rgba(0,0,0,.55);

    backdrop-filter: blur(25px);

    text-align: center;

    animation: appear .5s ease;
}

@keyframes appear {

    from {
        opacity: 0;
        transform: translateY(15px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* ICON */

.icon {

    font-size: 52px;

    margin-bottom: 12px;

    animation:
        float 3s ease-in-out infinite;
}

@keyframes float {

    50% {
        transform: translateY(-7px) rotate(2deg);
    }
}


/* TEXT */

h1 {

    margin: 5px 0 10px;

    font-size: 34px;

    letter-spacing: -1px;
}

.subtitle {

    color: #aaa1ad;

    line-height: 1.55;

    font-size: 15px;

    margin-bottom: 25px;
}

.gradient {

    background:
        linear-gradient(
            90deg,
            #ff6698,
            #ffb4ca
        );

    -webkit-background-clip: text;

    color: transparent;
}


/* INPUT */

input {

    width: 100%;

    padding: 15px;

    border-radius: 14px;

    border:
        1px solid rgba(255,255,255,.12);

    background:
        rgba(0,0,0,.25);

    color: white;

    outline: none;

    text-align: center;

    font-size: 16px;

    margin-bottom: 12px;
}

input:focus {

    border-color: #ff6799;
}


/* BUTTON */

button {

    width: 100%;

    padding: 15px;

    border: 0;

    border-radius: 14px;

    font-size: 15px;

    font-weight: 700;

    cursor: pointer;

    color: white;

    background:
        linear-gradient(
            135deg,
            #ff4c83,
            #ff719f
        );

    box-shadow:
        0 10px 30px
        rgba(255,76,131,.20);

    transition: .2s;
}

button:hover {

    transform: translateY(-2px);

}


/* MESSAGES */

.message {

    display: none;

    margin-top: 15px;

    padding: 13px;

    border-radius: 13px;

    font-size: 14px;
}

.error {

    background:
        rgba(255,60,80,.08);

    color: #ff9aaa;
}

.hint {

    background:
        rgba(255,190,80,.08);

    color: #ffd28a;
}


/* PAGES */

.page {

    display: none;
}


/* REWARD CARDS */

.rewards {

    display: grid;

    grid-template-columns:
        1fr 1fr;

    gap: 12px;

    margin: 22px 0;
}

.reward {

    padding: 20px 12px;

    border-radius: 18px;

    border:
        1px solid rgba(255,255,255,.09);

    background:
        rgba(255,255,255,.045);

    cursor: pointer;

    transition: .2s;
}

.reward:hover {

    transform: translateY(-4px);

    border-color:
        rgba(255,105,155,.5);
}

.reward.selected {

    border-color: #ff6799;

    background:
        rgba(255,103,153,.10);

    box-shadow:
        0 10px 30px
        rgba(255,80,130,.12);
}

.reward-icon {

    font-size: 32px;

    margin-bottom: 8px;
}

.reward-title {

    font-weight: 700;

    font-size: 15px;
}

.reward-desc {

    color: #918994;

    font-size: 12px;

    margin-top: 5px;

    line-height: 1.4;
}


/* RESULT */

.result {

    display: none;

    margin-top: 18px;

    padding: 18px;

    border-radius: 17px;

    background:
        rgba(255,255,255,.055);

    line-height: 1.55;

    animation: appear .4s ease;
}


/* HEARTS */

.heart {

    position: fixed;

    bottom: -30px;

    pointer-events: none;

    animation:
        fly 3s linear forwards;

    z-index: 100;
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
            translateY(-100vh)
            rotate(360deg);

        opacity: 0;
    }
}


/* SMALL TEXT */

.tiny {

    margin-top: 20px;

    font-size: 11px;

    color: #716a73;
}


@media(max-width:450px) {

    .card {
        padding: 28px 20px;
    }

}

</style>
</head>


<body>


<!-- ========================= -->
<!-- UNLOCK -->
<!-- ========================= -->

<div class="card" id="unlock">

    <div class="icon">🎁</div>

    <h1>
        You found it.
    </h1>

    <p class="subtitle">

        There's a tiny surprise waiting
        for whoever was curious enough
        to open this.

        <br><br>

        But first... prove you're the
        person I'm looking for 👀

    </p>

    <input
        id="nameInput"
        placeholder="Enter password..."
        autocomplete="off"
    >

    <button onclick="unlockPage()">
        Open surprise ✨
    </button>

    <div
        id="wrong"
        class="message error">

        Nope 😭 wrong one.

    </div>

    <div
        id="hint"
        class="message hint">

        💡 Hint: maybe try entering
        <b>your name</b>?

    </div>

</div>


<!-- ========================= -->
<!-- GIFT -->
<!-- ========================= -->

<div class="card page" id="gift">

    <div class="icon">
        🎀
    </div>

    <h1>
        A little gift for
        <span
            id="name"
            class="gradient">
        </span>
    </h1>

    <p class="subtitle">

        Nothing fancy.

        Just a tiny excuse to steal
        an hour or two from your week.

        <br><br>

        And yes...

        <b>you get to choose the reward.</b> 😌

    </p>


    <div class="rewards">

        <div
            class="reward"
            onclick="chooseReward(this,'Coffee date ☕')">

            <div class="reward-icon">
                ☕
            </div>

            <div class="reward-title">
                Coffee date
            </div>

            <div class="reward-desc">
                Coffee, conversations
                & probably too much caffeine.
            </div>

        </div>


        <div
            class="reward"
            onclick="chooseReward(this,'Food date 🍝')">

            <div class="reward-icon">
                🍝
            </div>

            <div class="reward-title">
                Food date
            </div>

            <div class="reward-desc">
                You pick the food.
                I'll handle the company.
            </div>

        </div>


        <div
            class="reward"
            onclick="chooseReward(this,'Dessert date 🍰')">

            <div class="reward-icon">
                🍰
            </div>

            <div class="reward-title">
                Dessert date
            </div>

            <div class="reward-desc">
                One sweet thing
                after another.
            </div>

        </div>


        <div
            class="reward"
            onclick="chooseReward(this,'Surprise date ✨')">

            <div class="reward-icon">
                ✨
            </div>

            <div class="reward-title">
                Surprise me
            </div>

            <div class="reward-desc">
                No spoilers.
                Just trust me.
            </div>

        </div>

    </div>


    <button onclick="confirmReward()">
        Claim my gift 💌
    </button>


    <div
        id="giftResult"
        class="result">
    </div>

</div>


<!-- ========================= -->
<!-- FINAL -->
<!-- ========================= -->

<div class="card page" id="final">

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

        Your gift is officially claimed.

        <br><br>

        There's just one tiny condition...

    </p>


    <div
        style="
        font-size:23px;
        font-weight:700;
        margin:25px 0;
        ">

        You have to let me
        take you out. 👀

    </div>


    <button onclick="sayYes()">

        Deal ❤️

    </button>


    <div
        id="finalResult"
        class="result">
    </div>

</div>


<script>


let attempts = 0;

let personName = "";

let selectedReward = "";


/* ========================= */
/* UNLOCK */
/* ========================= */

function unlockPage() {

    const input =
        document
        .getElementById("nameInput")
        .value
        .trim();


    const wrong =
        document
        .getElementById("wrong");

    const hint =
        document
        .getElementById("hint");


    if (!input) {

        wrong.style.display = "block";

        wrong.innerHTML =
            "❌ You need to enter something 😭";

        return;
    }


    /*
       FIRST ATTEMPT ALWAYS FAILS
    */

    if (attempts === 0) {

        attempts++;

        wrong.style.display = "block";

        hint.style.display = "block";

        return;
    }


    /*
       SECOND ATTEMPT:

       Whatever she enters
       becomes her name.
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


/* ========================= */
/* REWARD */
/* ========================= */

function chooseReward(element,reward) {

    document
        .querySelectorAll(".reward")
        .forEach(
            x => x.classList.remove("selected")
        );


    element.classList.add("selected");


    selectedReward = reward;

}


/* ========================= */
/* CLAIM */
/* ========================= */

function confirmReward() {

    const result =
        document
        .getElementById("giftResult");


    if (!selectedReward) {

        result.style.display = "block";

        result.innerHTML =
            "Pick your reward first 😌";

        return;
    }


    result.style.display = "block";

    result.innerHTML = `
        🎁 <b>${selectedReward}</b>
        selected.

        <br><br>

        Excellent choice,
        ${personName}. 😌

        <br><br>

        <button
            onclick="continueToDate()"
            style="margin-top:8px">

            Okay, what's the catch? 👀

        </button>
    `;

}


/* ========================= */
/* FINAL PAGE */
/* ========================= */

function continueToDate() {

    document
        .getElementById("gift")
        .style.display = "none";


    document
        .getElementById("final")
        .style.display = "block";


    document
        .getElementById("finalName")
        .textContent = personName;

}


/* ========================= */
/* YES */
/* ========================= */

function sayYes() {

    createHearts();


    const result =
        document
        .getElementById("finalResult");


    result.style.display = "block";

    result.innerHTML = `

        <div style="font-size:36px">
            🥹❤️
        </div>

        <b>
            It's a date.
        </b>

        <br><br>

        ${selectedReward}

        <br>

        I'll see you soon,
        ${personName}. ✨

    `;

}


/* ========================= */
/* HEART ANIMATION */
/* ========================= */

function createHearts() {

    for(
        let i=0;
        i<25;
        i++
    ) {

        const heart =
            document.createElement("div");


        heart.className =
            "heart";


        heart.innerHTML =
            [
                "❤️",
                "💗",
                "💕",
                "💖",
                "💘"
            ][
                Math.floor(
                    Math.random()*5
                )
            ];


        heart.style.left =
            Math.random()*100 + "vw";


        heart.style.animationDelay =
            Math.random()*.8 + "s";


        document
            .body
            .appendChild(heart);


        setTimeout(
            () => heart.remove(),
            3500
        );

    }

}


/* ENTER KEY */

document
    .getElementById("nameInput")
    .addEventListener(
        "keydown",
        function(e) {

            if(e.key === "Enter") {

                unlockPage();

            }

        }
    );

</script>

</body>
</html>
""", height=850, scrolling=False)
