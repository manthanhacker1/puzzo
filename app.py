import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="A Little Something 💌",
    page_icon="💗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Google Drive image
PHOTO_URL = (
    "https://drive.google.com/uc?"
    "export=view&id=1pwDLBt6uJrZo0rJSB0HHisuuWUEyL3OZ"
)

html = f"""
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>

* {{
    box-sizing: border-box;
}}

html {{
    scroll-behavior: smooth;
}}

body {{
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
                 Roboto, Helvetica, Arial, sans-serif;
    background:
        radial-gradient(circle at top left, #fff7f8, transparent 35%),
        linear-gradient(135deg, #fff5f7, #fce7ed);
    color: #302126;
}}

.page {{
    max-width: 1100px;
    margin: auto;
    padding: 55px 22px 80px;
}}

/* HERO */

.hero {{
    text-align: center;
    margin-bottom: 45px;
}}

.eyebrow {{
    font-size: 12px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: #a76b7c;
    margin-bottom: 15px;
}}

.hero h1 {{
    margin: 0;
    font-family: Georgia, "Times New Roman", serif;
    font-size: clamp(45px, 8vw, 78px);
    font-weight: 400;
    line-height: 1.05;
}}

.hero p {{
    margin-top: 18px;
    color: #765963;
    font-size: 17px;
}}

/* PRODUCT */

.product {{
    display: grid;
    grid-template-columns: 1fr 1fr;
    overflow: hidden;
    border-radius: 30px;
    background: rgba(255,255,255,0.82);
    box-shadow: 0 25px 80px rgba(86, 39, 52, 0.15);
}}

.photo {{
    position: relative;
    min-height: 620px;
    background: #f2dce2;
}}

.photo img {{
    width: 100%;
    height: 100%;
    min-height: 620px;
    object-fit: cover;
    display: block;
}}

.badge {{
    position: absolute;
    top: 22px;
    left: 22px;
    padding: 10px 16px;
    background: rgba(255,255,255,0.94);
    border-radius: 50px;
    font-size: 11px;
    letter-spacing: 1.5px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.10);
}}

/* DETAILS */

.details {{
    padding: 55px 48px;
}}

.details h2 {{
    margin: 0;
    font-family: Georgia, "Times New Roman", serif;
    font-weight: 400;
    font-size: 45px;
}}

.subtitle {{
    color: #a06d7c;
    margin-top: 8px;
    margin-bottom: 32px;
    font-size: 15px;
}}

.features {{
    border-top: 1px solid #ead6dc;
}}

.feature {{
    display: flex;
    justify-content: space-between;
    gap: 20px;
    padding: 16px 0;
    border-bottom: 1px solid #ead6dc;
    font-size: 14px;
}}

.feature .label {{
    color: #91737c;
}}

.feature .value {{
    font-weight: 600;
    text-align: right;
}}

.price {{
    margin-top: 35px;
    color: #8c6872;
    font-size: 14px;
}}

.price strong {{
    display: block;
    margin-top: 5px;
    color: #302126;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 28px;
    font-weight: 400;
}}

/* BUTTON */

button {{
    width: 100%;
    margin-top: 25px;
    padding: 17px 20px;
    border: none;
    border-radius: 15px;
    background: #302126;
    color: white;
    font-size: 15px;
    cursor: pointer;
    transition: all .25s ease;
}}

button:hover {{
    transform: translateY(-3px);
    box-shadow: 0 14px 30px rgba(48,33,38,.22);
}}

/* CHECKOUT */

.hidden {{
    display: none !important;
}}

.checkout {{
    max-width: 800px;
    margin: 40px auto 0;
    padding: 45px 35px;
    border-radius: 28px;
    background: rgba(255,255,255,.9);
    text-align: center;
    box-shadow: 0 20px 60px rgba(86,39,52,.12);
    animation: appear .6s ease;
}}

.checkout h2 {{
    margin-top: 0;
    font-family: Georgia, "Times New Roman", serif;
    font-size: 38px;
    font-weight: 400;
}}

.checkout p {{
    color: #715861;
    line-height: 1.8;
    font-size: 16px;
}}

/* FINAL */

.final {{
    max-width: 800px;
    margin: 30px auto 0;
    padding: 50px 35px;
    border-radius: 28px;
    background: #302126;
    color: white;
    text-align: center;
    animation: appear .6s ease;
}}

.final h2 {{
    font-family: Georgia, "Times New Roman", serif;
    font-size: 40px;
    font-weight: 400;
}}

.final p {{
    color: #eadcdf;
    line-height: 1.8;
    font-size: 17px;
}}

.heart {{
    font-size: 48px;
    margin-top: 20px;
}}

/* FOOTER */

.footer {{
    text-align: center;
    margin-top: 45px;
    color: #a47d87;
    font-size: 13px;
}}

/* ANIMATION */

@keyframes appear {{
    from {{
        opacity: 0;
        transform: translateY(20px);
    }}
    to {{
        opacity: 1;
        transform: translateY(0);
    }}
}}

/* MOBILE */

@media (max-width: 760px) {{

    .page {{
        padding: 35px 15px 60px;
    }}

    .product {{
        grid-template-columns: 1fr;
    }}

    .photo,
    .photo img {{
        min-height: 470px;
    }}

    .details {{
        padding: 38px 28px;
    }}

    .details h2 {{
        font-size: 38px;
    }}

    .feature {{
        font-size: 13px;
    }}

}}

</style>
</head>

<body>

<div class="page">

    <!-- HERO -->

    <div class="hero">

        <div class="eyebrow">
            A very questionable purchase 💌
        </div>

        <h1>
            A Little Something
        </h1>

        <p>
            I found something I thought you might like.
        </p>

    </div>


    <!-- PRODUCT -->

    <div class="product">

        <div class="photo">

            <img
                src="{PHOTO_URL}"
                alt="Something special"
            >

            <div class="badge">
                ONLY ONE AVAILABLE
            </div>

        </div>


        <div class="details">

            <h2>
                Her. ✨
            </h2>

            <div class="subtitle">
                Limited edition. Extremely difficult to replace.
            </div>


            <div class="features">

                <div class="feature">
                    <span class="label">Availability</span>
                    <span class="value">Extremely rare</span>
                </div>

                <div class="feature">
                    <span class="label">Eyes</span>
                    <span class="value">A little distracting</span>
                </div>

                <div class="feature">
                    <span class="label">Smile</span>
                    <span class="value">Honestly unfair</span>
                </div>

                <div class="feature">
                    <span class="label">Lip Gloss</span>
                    <span class="value">Dangerous combination</span>
                </div>

                <div class="feature">
                    <span class="label">Personality</span>
                    <span class="value">Still discovering 😌</span>
                </div>

                <div class="feature">
                    <span class="label">Delivery</span>
                    <span class="value">In person only</span>
                </div>

            </div>


            <div class="price">

                Estimated value

                <strong>
                    One good date ❤️
                </strong>

            </div>


            <button onclick="addToCart()">
                Add to cart 💗
            </button>

        </div>

    </div>


    <!-- CHECKOUT -->

    <div id="checkout" class="checkout hidden">

        <h2>
            Order Confirmed... 👀
        </h2>

        <p>
            Your order has successfully been added to the cart.
        </p>

        <p>
            There is just one tiny problem with your order.
        </p>

        <p>
            This particular gift isn't available for delivery.
        </p>

        <p>
            Because you're not something I want to put in a cart.
            <br>
            You're someone I actually want to spend time with.
        </p>

        <button onclick="upgradeOrder()">
            Upgrade the order ☕🍰
        </button>

    </div>


    <!-- FINAL MESSAGE -->

    <div id="final" class="final hidden">

        <h2>
            Okay, here's the actual order. 😌
        </h2>

        <p>
            Basque + cheese tiramisu.
        </p>

        <p>
            Good food, good conversation,
            <br>
            and hopefully a little trouble.
        </p>

        <p>
            Consider this my actual order. ❤️
        </p>

        <div class="heart">
            ♡
        </div>

    </div>


    <div class="footer">
        No refunds. No exchanges. One very specific customer. :)
    </div>

</div>


<script>

function addToCart() {{

    const checkout = document.getElementById("checkout");

    checkout.classList.remove("hidden");

    setTimeout(() => {{

        checkout.scrollIntoView({{
            behavior: "smooth",
            block: "center"
        }});

    }}, 100);

}}


function upgradeOrder() {{

    const final = document.getElementById("final");

    final.classList.remove("hidden");

    setTimeout(() => {{

        final.scrollIntoView({{
            behavior: "smooth",
            block: "center"
        }});

    }}, 100);

}}

</script>

</body>
</html>
"""

components.html(
    html,
    height=1550,
    scrolling=True
)
