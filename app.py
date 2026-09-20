import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="🔐 Secret",
    page_icon="💌",
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
        "Segoe UI",
        sans-serif;

    background:
        radial-gradient(
            circle at 20% 20%,
            rgba(255, 70, 130, .25),
            transparent 35%
        ),
        radial-gradient(
            circle at 80% 80%,
            rgba(150, 70, 255, .22),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #09070c,
            #1b0c19,
            #09070c
        );

    color: white;

    display: flex;
    justify-content: center;
    align-items: center;

    padding: 20px;
}

.card {
    width: min(500px, 100%);

    padding: 40px 28px;

    text-align: center;

    background: rgba(255,255,255,.07);

    border: 1px solid rgba(255,255,255,.12);

    border-radius: 30px;

    backdrop-filter: blur(25px);

    box-shadow:
        0 30px 80px rgba(0,0,0,.5);
}

.icon {
    font-size: 60px;

    margin-bottom: 15px;

    animation: float 3s ease-in-out infinite;
}

@keyframes float {

    50% {
        transform: translateY(-8px);
    }

}

h1 {

    font-size: 38px;

    margin: 5px 0 12px;

    letter-spacing: -1px;
}

.subtitle {

    color: #bdb4c0;

    line-height: 1.6;

    margin-bottom: 28px;
}

input {

    width: 100%;

    padding: 16px;

    border-radius: 15px;

    border: 1px solid
        rgba(255,255,255,.15);

    background:
        rgba(0,0,0,.25);

    color: white;

    outline: none;

    font-size: 16px;

    text-align: center;

    margin-bottom: 12px;
}

input:focus {

    border-color: #ff5d91;

    box-shadow:
        0 0 20px rgba(255,93,145,.15);
}

button {

    width: 100%;

    padding: 16px;

    border: none;

    border-radius: 15px;

    cursor: pointer;

    font-size: 16px;

    font-weight: 700;

    color: white;

    background:
        linear-gradient(
            135deg,
            #ff477e,
            #ff6a9a
        );

    transition: .2s;

    box-shadow:
        0 10px 30px
        rgba(255,71,126,.25);
}

button:hover {

    transform: translateY(-2px);

}

.message {

    margin-top: 18px;

    padding: 14px;

    border-radius: 14px;

    display: none;

    line-height: 1.5;
}

.error {

    background:
        rgba(255,60,80,.10);

    border:
        1px solid rgba(255,60,80,.2);

    color: #ff9bab;
}

.hint {

    background:
        rgba(255,180,80,.10);

    border:
        1px solid rgba(255,180,80,.2);

    color: #ffd28a;
}

.hidden {

    display: none;
}


/* DATE PAGE */

.date-page {

    display: none;
}

.heart {

    font-size: 65px;

    margin-bottom: 10px;
}

.name {

    background:
        linear-gradient(
            90deg,
            #ff6b9a,
            #ffb2ca
        );

    -webkit-background-clip: text;

    color: transparent;
}

.question {

    font-size: 25px;

    font-weight: 700;

    margin: 25px 0;
}

.buttons {

    display: flex;

    gap: 12px;
}

.yes {

    background:
        linear-gradient(
            135deg,
            #ff477e,
            #ff6a9a
        );
}

.maybe {

    background:
        rgba(255,255,255,.09);

    border:
        1px solid rgba(255,255,255,.15);

    box-shadow: none;
}

.result {

    display: none;

    margin-top: 22px;

    padding: 20px;

    border-radius: 18px;

    background:
        rgba(255,255,255,.07);

    line-height: 1.6;
}

.heart-fly {

    position: fixed;

    bottom: -30px;

    pointer-events: none;

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
            translateY(-100vh)
            rotate(360deg);

        opacity: 0;
    }
}

.small {

    margin-top: 25px;

    color: #8f8790;

    font-size: 12px;
}

@media(max-width:500px) {

    .card {

        padding: 35px 22px;
    }

    .buttons {

        flex-direction: column;
    }

}

</style>

</head>

<body>


<!-- PASSWORD SCREEN -->

<div class="card" id="login">

    <div class="icon">
        🔐
    </div>

    <h1>
        Secret Question
    </h1>

    <p class="subtitle">
        This page is protected.<br>
        Enter the password to continue 👀
    </p>

    <input
        id="password"
        type="password"
        placeholder="Enter password..."
        autocomplete="off"
    >

    <button onclick="checkPassword()">
        Unlock 🔓
    </button>

    <div
        id="error"
        class="message error">
        ❌ Nope... wrong password.
    </div>

    <div
        id="hint"
        class="message hint">
        💡 Hint: Try entering <b>your name</b> 😉
    </div>

    <div class="small">
        You only get one hint... maybe.
    </div>

</div>


<!-- DATE PAGE -->

<div class="card date-page" id="datePage">

    <div class="heart">
        💌
    </div>

    <h1>
        Hey
        <span
            class="name"
            id="girlName">
        </span> 👋
    </h1>

    <p class="subtitle">

        So you somehow managed
        to unlock this...

        which means I have something
        important to ask you.

    </p>

    <div class="question">

        Would you go on a date with me? 👀❤️

    </div>

    <div class="buttons">

        <button
            class="yes"
            onclick="yes()">

            Yes ❤️

        </button>

        <button
            class="maybe"
            onclick="maybe()">

            Maybe 😌

        </button>

    </div>

    <div
        id="result"
        class="result">
    </div>

    <div class="small">

        No pressure.
        Just say what's on your mind. ✨

    </div>

</div>


<script>


let attempts = 0;


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


    if (!input) {

        error.style.display = "block";

        error.innerHTML =
            "❌ You forgot to enter something 😭";

        return;
    }


    /*
       FIRST ATTEMPT:

       Always reject it.

       This creates the
       "wrong password" moment.
    */

    if (attempts === 0) {

        attempts++;

        error.style.display = "block";

        hint.style.display = "block";

        return;
    }


    /*
       SECOND ATTEMPT:

       Any non-empty input
       is treated as her name.
    */

    unlock(input);

}


function unlock(name) {

    document
        .getElementById("login")
        .style.display = "none";


    document
        .getElementById("datePage")
        .style.display = "block";


    document
        .getElementById("girlName")
        .textContent = name;


    document
        .getElementById("password")
        .value = "";


    document
        .getElementById("result")
        .style.display = "none";

}


function hearts() {

    for (
        let i = 0;
        i < 25;
        i++
    ) {

        const h =
            document.createElement("div");

        h.className = "heart-fly";

        h.innerHTML =
            ["❤️","💗","💕","💖","💘"]
            [
                Math.floor(
                    Math.random() * 5
                )
            ];

        h.style.left =
            Math.random() * 100 + "vw";

        h.style.animationDelay =
            Math.random() * .8 + "s";

        document.body.appendChild(h);

        setTimeout(
            () => h.remove(),
            3500
        );
    }

}


function yes() {

    hearts();

    const result =
        document.getElementById("result");

    result.style.display = "block";

    result.innerHTML = `
        <div style="font-size:35px">
            🥹❤️
        </div>

        <strong>
            I knew you had good taste.
        </strong>

        <br><br>

        Okay, now we just need
        to pick a day. 😌
    `;

}


function maybe() {

    const result =
        document.getElementById("result");

    result.style.display = "block";

    result.innerHTML = `
        <div style="font-size:35px">
            😌
        </div>

        <strong>
            I'll accept a "maybe".
        </strong>

        <br><br>

        What would turn it into a yes? 👀
    `;

}


/* ENTER KEY */

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
""", height=850, scrolling=False)
