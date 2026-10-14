import streamlit as st

st.set_page_config(
    page_title="A little note for Mitali",
    page_icon="🌙",
    layout="centered",
)

for key, default in {
    "unlocked": False,
    "show_hint": False,
    "coffee_response": "",
}.items():
    if key not in st.session_state:
        st.session_state[key] = default

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,500;0,700;1,500&family=Quicksand:wght@400;600;700&display=swap');

:root {
    --bg1: #120a12;
    --bg2: #241224;
    --card: rgba(38, 20, 36, 0.78);
    --ink: #fbeef3;
    --muted: #c9a6b6;
    --rose: #ff7fa8;
    --rose-soft: #ffb3c9;
    --plum: #7a2f56;
    --line: rgba(255, 143, 180, 0.22);
}

.stApp {
    background:
        radial-gradient(circle at 15% 15%, rgba(255,127,168,.18) 0, transparent 35%),
        radial-gradient(circle at 85% 80%, rgba(160,90,255,.18) 0, transparent 35%),
        linear-gradient(160deg, var(--bg1), var(--bg2));
    color: var(--ink);
    font-family: 'Quicksand', sans-serif;
}
[data-testid="stHeader"] { background: transparent; }
.block-container { max-width: 640px; padding-top: 2.2rem; padding-bottom: 3rem; }

/* floating hearts in the background */
.hearts { position: fixed; inset: 0; pointer-events: none; z-index: 0; overflow: hidden; }
.heart {
    position: absolute; bottom: -40px; color: rgba(255,143,180,.35);
    animation: rise linear infinite;
}
@keyframes rise {
    to { transform: translateY(-110vh) rotate(25deg); opacity: 0; }
}

.eyebrow {
    color: var(--rose-soft); text-align: center; text-transform: uppercase;
    letter-spacing: .24em; font-size: .7rem; margin-bottom: 1rem; opacity: .85;
}

[data-testid="stVerticalBlockBorderWrapper"] {
    background: var(--card) !important;
    border: 1px solid var(--line) !important;
    border-radius: 28px !important;
    box-shadow: 0 25px 70px rgba(0,0,0,.45), inset 0 1px 0 rgba(255,255,255,.04);
    backdrop-filter: blur(10px);
    animation: float-in .9s ease both;
}
@keyframes float-in {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
}

.hero { text-align: center; padding: .6rem .2rem 1rem; }
.seal {
    width: 78px; height: 78px; display: grid; place-items: center; margin: 0 auto 1.1rem;
    border-radius: 50%; font-size: 2.2rem;
    background: radial-gradient(circle, #ff8fb3, #b03a6b);
    box-shadow: 0 0 0 8px rgba(255,127,168,.12), 0 0 40px rgba(255,127,168,.45);
    animation: pulse 2.4s ease-in-out infinite;
}
@keyframes pulse {
    0%,100% { transform: scale(1); }
    50%     { transform: scale(1.07); }
}
.hero h1, .note-title {
    font-family: 'Fraunces', Georgia, serif; font-weight: 700;
    font-size: clamp(2.1rem, 7vw, 2.9rem); letter-spacing: -.02em;
    color: var(--ink); margin: .2rem 0 .5rem;
}
.hero h1 span { color: var(--rose); font-style: italic; }
.hero-copy { color: var(--muted); line-height: 1.7; max-width: 380px; margin: 0 auto; }

.note-pill {
    display: inline-block; color: #120a12; background: var(--rose-soft);
    border-radius: 999px; padding: .4rem .85rem; font-size: .72rem;
    font-weight: 700; letter-spacing: .08em; margin-bottom: .8rem;
}
.letter { color: #efd7e1; font-size: 1rem; line-height: 1.85; }
.letter p { margin: 0 0 1rem; }
.letter strong { color: var(--rose-soft); }

.divider {
    display: flex; align-items: center; gap: 12px;
    color: var(--rose-soft); margin: 1.5rem 0 1rem; font-size: .8rem; letter-spacing: .1em;
}
.divider:before, .divider:after { content: ''; height: 1px; background: var(--line); flex: 1; }

.question {
    text-align: center; padding: 1.4rem 1rem;
    background: linear-gradient(135deg, rgba(255,127,168,.14), rgba(160,90,255,.12));
    border: 1px solid var(--line); border-radius: 22px;
}
.question-title {
    font-family: 'Fraunces', Georgia, serif; font-size: 1.6rem;
    font-style: italic; color: var(--ink); margin: 0 0 .4rem;
}
.question-sub { color: var(--muted); font-size: .9rem; margin: 0; }

.hint {
    color: var(--rose-soft); background: rgba(255,127,168,.1);
    border: 1px dashed var(--rose); border-radius: 14px;
    padding: .75rem .9rem; text-align: center; font-size: .9rem; margin-top: .8rem;
}
.tiny, .footer { color: #9a7f8e; text-align: center; font-size: .78rem; line-height: 1.6; }

div[data-testid="stTextInput"] input {
    background: rgba(18,10,18,.7) !important; color: var(--ink) !important;
    border: 1px solid var(--line) !important; border-radius: 16px !important;
    min-height: 3rem;
}
div[data-testid="stTextInput"] input:focus { border-color: var(--rose) !important; box-shadow: 0 0 0 3px rgba(255,127,168,.2) !important; }

div.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    width: 100%; min-height: 3rem; border-radius: 16px; font-weight: 700;
    transition: transform .15s ease, box-shadow .2s ease;
}
div[data-testid="stFormSubmitButton"] > button {
    background: linear-gradient(135deg, #ff7fa8, #b03a6b); color: white; border: none;
}
div.stButton > button[kind="primary"] {
    background: linear-gradient(135deg, #ff7fa8, #b03a6b); color: white; border: none;
}
div.stButton > button[kind="secondary"] {
    background: rgba(255,255,255,.06); color: var(--ink); border: 1px solid var(--line);
}
div.stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
    transform: translateY(-2px); box-shadow: 0 10px 25px rgba(255,127,168,.3);
}

div[data-testid="stAlert"] { border-radius: 16px; }

@media (max-width: 480px) {
    .block-container { padding: 1.2rem 1rem 2rem; }
}
</style>

<div class="hearts">
    <span class="heart" style="left:8%; font-size:18px; animation-duration:14s;">♡</span>
    <span class="heart" style="left:22%; font-size:26px; animation-duration:19s; animation-delay:-4s;">♡</span>
    <span class="heart" style="left:45%; font-size:14px; animation-duration:12s; animation-delay:-7s;">♡</span>
    <span class="heart" style="left:63%; font-size:30px; animation-duration:22s; animation-delay:-2s;">♡</span>
    <span class="heart" style="left:82%; font-size:20px; animation-duration:16s; animation-delay:-9s;">♡</span>
    <span class="heart" style="left:93%; font-size:12px; animation-duration:11s; animation-delay:-5s;">♡</span>
</div>
<div class="eyebrow">✦ a small note, made with care ✦</div>
""", unsafe_allow_html=True)

if not st.session_state.unlocked:
    with st.container(border=True):
        st.markdown("""
        <div class="hero">
            <div class="seal">♡</div>
            <h1>Hey, <span>Mitali.</span></h1>
            <p class="hero-copy">
            There's something I wanted to say properly, without making it a long text.
            This little page is just for you. ✨
            </p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("password_form"):
            entered_password = st.text_input(
                "A tiny password to open it",
                placeholder="hint: it's your name 🌸",
                type="password",
            )
            submitted = st.form_submit_button("Open the note 💌", use_container_width=True)

        if submitted:
            if entered_password.strip().casefold() == "mitali":
                st.session_state.unlocked = True
                st.session_state.show_hint = False
                st.balloons()
                st.rerun()
            else:
                st.session_state.show_hint = True

        if st.session_state.show_hint:
            st.markdown(
                '<div class="hint">Almost! 🙈 Try the name of the person this note is for.</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown('<p class="tiny">Nothing complicated, promise.</p>', unsafe_allow_html=True)

else:
    with st.container(border=True):
        st.markdown("""
        <div class="note-pill">✦ JUST BEING HONEST ✦</div>
        <h1 class="note-title">One thing I wanted you to know.</h1>
        <div class="letter">
            <p>Hey Mitali,</p>
            <p>First, <strong>I'm genuinely sorry</strong> for the ways I may have hurt you
            or made you feel misunderstood. I can't undo what happened, and I'm not expecting
            an apology to fix everything. I just wanted to say it honestly. 🫶</p>
            <p>Tujhyasobat ghalavlela every single moment majhyasathi special hota. Tujha smile,
            tu bolnyachi style, ani agdi simple moments pan memorable karaychi tuzhi way,
            these are things I still remember. You have a warmth that made ordinary days
            feel different, and I'm really glad I got to know you. 🌙</p>
            <p>I don't want to pressure you or make things awkward. You mattered to me,
            and the good memories still mean something to me.</p>
        </div>
        <div class="divider">✦ one simple question ✦</div>
        <div class="question">
            <p class="question-title">Would you be open to coffee sometime? ☕</p>
            <p class="question-sub">Just a calm conversation. Whatever you pick, I'm okay with it.</p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        yes_col, no_col = st.columns(2)

        with yes_col:
            if st.button("Yes, I'd like that ☕", key="yes_coffee", type="primary", use_container_width=True):
                st.session_state.coffee_response = "yes"
                st.balloons()

        with no_col:
            if st.button("Not right now 🌿", key="no_coffee", type="secondary", use_container_width=True):
                st.session_state.coffee_response = "no"

        if st.session_state.coffee_response == "yes":
            st.success(
                "That makes me really happy. ☕ Text me whenever you're comfortable, "
                "and you pick the time and place. We'll keep it simple."
            )
        elif st.session_state.coffee_response == "no":
            st.info(
                "That's completely okay, and thank you for reading this. "
                "I respect your answer and won't push. 🌿"
            )

st.markdown(
    '<p class="footer">Made with care. Your answer is yours to choose, and either one will be respected. 🌙</p>',
    unsafe_allow_html=True,
)
