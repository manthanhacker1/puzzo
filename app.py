
import streamlit as st

st.set_page_config(
    page_title="A little note for Mitali",
    page_icon="♡",
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
:root {
    --ink: #382631;
    --muted: #806b76;
    --rose: #bd7188;
    --dark: #9d4c67;
    --line: #ead8dc;
}
.stApp {
    background: radial-gradient(ellipse at 12% 10%,
    #fffaf7 0, transparent 38%),
    radial-gradient(ellipse at 90% 85%,
    #efdde5 0, transparent 38%), #f7f0eb;
    color: var(--ink);
}
[data-testid="stHeader"] { background: transparent; }
.block-container {
    max-width: 620px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.eyebrow {
    color: var(--muted);
    text-align: center;
    text-transform: uppercase;
    letter-spacing: .18em;
    font-size: .68rem;
    margin-bottom: 1rem;
}
.hero { text-align: center; padding: .4rem .2rem .8rem; }
.seal {
    width: 64px; height: 64px; display: grid;
    place-items: center; margin: 0 auto 1.1rem;
    border-radius: 22px; background: #f5e5e9;
    color: var(--dark); font-size: 1.8rem;
}
.hero h1, .note-title {
    color: var(--ink);
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(2rem, 7vw, 2.7rem);
    font-weight: 500; letter-spacing: -.035em;
}
.hero-copy {
    color: var(--muted); line-height: 1.7;
    max-width: 355px; margin: 0 auto 1rem;
}
.note-pill {
    display: inline-block; color: var(--dark);
    background: #f5e5e9; border-radius: 999px;
    padding: .42rem .75rem; font-size: .7rem;
    font-weight: 700; letter-spacing: .05em;
    margin-bottom: 1rem;
}
.note-title { font-size: clamp(2rem, 7vw, 2.6rem); }
.letter { color: #5b4651; font-size: .97rem; line-height: 1.85; }
.letter p { margin: 0 0 1rem; }
.letter strong { color: #8f3f5a; }
.divider {
    display: flex; align-items: center; gap: 12px;
    color: #b98b99; margin: 1.4rem 0 1rem;
    font-size: .78rem;
}
.divider:before, .divider:after {
    content: ''; height: 1px; background: var(--line); flex: 1;
}
.question {
    text-align: center; background: #fff5f5;
    border: 1px solid #f0dce2; border-radius: 20px;
    padding: 1.15rem 1rem;
}
.question-title {
    color: var(--ink);
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1.45rem; line-height: 1.3;
}
.question-sub { color: var(--muted); font-size: .86rem; }
.hint {
    color: #8f3f5a; background: #fff0f3;
    border: 1px solid #f0dce2; border-radius: 12px;
    padding: .75rem .9rem; text-align: center;
    font-size: .88rem; margin-top: .8rem;
}
.tiny, .footer {
    color: #9c8791; text-align: center;
    font-size: .74rem; line-height: 1.6;
}
div[data-testid="stTextInput"] input {
    border: 1px solid var(--line);
    border-radius: 14px; background: white;
    min-height: 3rem;
}
div.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    width: 100%; min-height: 2.9rem;
    border-radius: 13px; font-weight: 650;
}
div[data-testid="stFormSubmitButton"] > button {
    background: var(--dark); color: white;
    border: 1px solid var(--dark);
}
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,250,246,.9);
    border-color: rgba(234,216,220,.95) !important;
    border-radius: 25px !important;
    box-shadow: 0 18px 55px rgba(91,52,68,.09);
}
@media(max-width:480px) {
    .block-container { padding: 1.2rem 1rem 2rem; }
}
</style>
<div class="eyebrow">a small note · made with care</div>
""", unsafe_allow_html=True)

if not st.session_state.unlocked:
    with st.container(border=True):
        st.markdown("""
        <div class="hero">
            <div class="seal">♡</div>
            <h1>Hey, Mitali.</h1>
            <p class="hero-copy">
            There's something I wanted to say properly,
            without making it a long text.
            This little page is just for you.
            </p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("password_form"):
            entered_password = st.text_input(
                "A tiny password to open it",
                placeholder="Enter password",
                type="password",
            )
            submitted = st.form_submit_button(
                "Open note", use_container_width=True
            )

        if submitted:
            if entered_password.strip().casefold() == "mitali":
                st.session_state.unlocked = True
                st.session_state.show_hint = False
                st.rerun()
            else:
                st.session_state.show_hint = True

        if st.session_state.show_hint:
            st.markdown(
                '<div class="hint">Not quite — '
                'try entering your name 😉</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<p class="tiny">A little personal, '
                'nothing complicated.</p>',
                unsafe_allow_html=True,
            )

else:
    with st.container(border=True):
        st.markdown("""
        <div class="note-pill">JUST BEING HONEST</div>
        <h1 class="note-title">
            One thing I wanted you to know.
        </h1>
        <div class="letter">
            <p>Hey Mitali,</p>
            <p>First, <strong>I'm genuinely sorry</strong>
            for the ways I may have hurt you or made you feel
            misunderstood. I can't change what happened, and
            I'm not expecting a sorry to fix everything.
            I just wanted to say it honestly.</p>
            <p>Tujhyasobat ghalavlela every single moment
            majhyasathi special hota. Tujha smile, tu bolnyachi
            style, ani agdi simple moments pan memorable
            karaychi tuzhi way — these are things I still
            remember. You have a warmth and a presence that
            made ordinary days feel different, and I'm
            genuinely glad I got to know you.</p>
            <p>I don't want to put pressure on you or make
            things awkward. I just didn't want to leave
            these words unsaid. You mattered to me, and
            the good memories still mean something to me.</p>
        </div>
        <div class="divider">one simple question</div>
        <div class="question">
            <p class="question-title">
                Would you be open to coffee sometime? ☕
            </p>
            <p class="question-sub">
                Just a calm conversation, no pressure
                and no expectations.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        yes_col, no_col = st.columns(2)

        with yes_col:
            if st.button(
                "Yes, coffee sounds okay",
                key="yes_coffee",
                use_container_width=True,
            ):
                st.session_state.coffee_response = "yes"

        with no_col:
            if st.button(
                "No, thank you",
                key="no_coffee",
                use_container_width=True,
            ):
                st.session_state.coffee_response = "no"

        if st.session_state.coffee_response == "yes":
            st.success(
                "That would be nice. ☕ Text me whenever "
                "you're comfortable, and you can choose "
                "the time and place. We can keep it simple."
            )
        elif st.session_state.coffee_response == "no":
            st.info(
                "That's completely okay. Thank you for "
                "reading this. I respect your answer "
                "and won't push."
            )

st.markdown(
    '<p class="footer">Made with care. Your answer is yours '
    'to choose, and either answer will be respected.</p>',
    unsafe_allow_html=True,
)
import streamlit as st

st.set_page_config(
    page_title="A little note for Mitali",
    page_icon="♡",
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
:root {
    --ink: #382631;
    --muted: #806b76;
    --rose: #bd7188;
    --dark: #9d4c67;
    --line: #ead8dc;
}
.stApp {
    background: radial-gradient(ellipse at 12% 10%,
    #fffaf7 0, transparent 38%),
    radial-gradient(ellipse at 90% 85%,
    #efdde5 0, transparent 38%), #f7f0eb;
    color: var(--ink);
}
[data-testid="stHeader"] { background: transparent; }
.block-container {
    max-width: 620px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.eyebrow {
    color: var(--muted);
    text-align: center;
    text-transform: uppercase;
    letter-spacing: .18em;
    font-size: .68rem;
    margin-bottom: 1rem;
}
.hero { text-align: center; padding: .4rem .2rem .8rem; }
.seal {
    width: 64px; height: 64px; display: grid;
    place-items: center; margin: 0 auto 1.1rem;
    border-radius: 22px; background: #f5e5e9;
    color: var(--dark); font-size: 1.8rem;
}
.hero h1, .note-title {
    color: var(--ink);
    font-family: Georgia, 'Times New Roman', serif;
    font-size: clamp(2rem, 7vw, 2.7rem);
    font-weight: 500; letter-spacing: -.035em;
}
.hero-copy {
    color: var(--muted); line-height: 1.7;
    max-width: 355px; margin: 0 auto 1rem;
}
.note-pill {
    display: inline-block; color: var(--dark);
    background: #f5e5e9; border-radius: 999px;
    padding: .42rem .75rem; font-size: .7rem;
    font-weight: 700; letter-spacing: .05em;
    margin-bottom: 1rem;
}
.note-title { font-size: clamp(2rem, 7vw, 2.6rem); }
.letter { color: #5b4651; font-size: .97rem; line-height: 1.85; }
.letter p { margin: 0 0 1rem; }
.letter strong { color: #8f3f5a; }
.divider {
    display: flex; align-items: center; gap: 12px;
    color: #b98b99; margin: 1.4rem 0 1rem;
    font-size: .78rem;
}
.divider:before, .divider:after {
    content: ''; height: 1px; background: var(--line); flex: 1;
}
.question {
    text-align: center; background: #fff5f5;
    border: 1px solid #f0dce2; border-radius: 20px;
    padding: 1.15rem 1rem;
}
.question-title {
    color: var(--ink);
    font-family: Georgia, 'Times New Roman', serif;
    font-size: 1.45rem; line-height: 1.3;
}
.question-sub { color: var(--muted); font-size: .86rem; }
.hint {
    color: #8f3f5a; background: #fff0f3;
    border: 1px solid #f0dce2; border-radius: 12px;
    padding: .75rem .9rem; text-align: center;
    font-size: .88rem; margin-top: .8rem;
}
.tiny, .footer {
    color: #9c8791; text-align: center;
    font-size: .74rem; line-height: 1.6;
}
div[data-testid="stTextInput"] input {
    border: 1px solid var(--line);
    border-radius: 14px; background: white;
    min-height: 3rem;
}
div.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    width: 100%; min-height: 2.9rem;
    border-radius: 13px; font-weight: 650;
}
div[data-testid="stFormSubmitButton"] > button {
    background: var(--dark); color: white;
    border: 1px solid var(--dark);
}
[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(255,250,246,.9);
    border-color: rgba(234,216,220,.95) !important;
    border-radius: 25px !important;
    box-shadow: 0 18px 55px rgba(91,52,68,.09);
}
@media(max-width:480px) {
    .block-container { padding: 1.2rem 1rem 2rem; }
}
</style>
<div class="eyebrow">a small note · made with care</div>
""", unsafe_allow_html=True)

if not st.session_state.unlocked:
    with st.container(border=True):
        st.markdown("""
        <div class="hero">
            <div class="seal">♡</div>
            <h1>Hey, Mitali.</h1>
            <p class="hero-copy">
            There's something I wanted to say properly,
            without making it a long text.
            This little page is just for you.
            </p>
        </div>
        """, unsafe_allow_html=True)

        with st.form("password_form"):
            entered_password = st.text_input(
                "A tiny password to open it",
                placeholder="Enter password",
                type="password",
            )
            submitted = st.form_submit_button(
                "Open note", use_container_width=True
            )

        if submitted:
            if entered_password.strip().casefold() == "mitali":
                st.session_state.unlocked = True
                st.session_state.show_hint = False
                st.rerun()
            else:
                st.session_state.show_hint = True

        if st.session_state.show_hint:
            st.markdown(
                '<div class="hint">Not quite — '
                'try entering your name 😉</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<p class="tiny">A little personal, '
                'nothing complicated.</p>',
                unsafe_allow_html=True,
            )

else:
    with st.container(border=True):
        st.markdown("""
        <div class="note-pill">JUST BEING HONEST</div>
        <h1 class="note-title">
            One thing I wanted you to know.
        </h1>
        <div class="letter">
            <p>Hey Mitali,</p>
            <p>First, <strong>I'm genuinely sorry</strong>
            for the ways I may have hurt you or made you feel
            misunderstood. I can't change what happened, and
            I'm not expecting a sorry to fix everything.
            I just wanted to say it honestly.</p>
            <p>Tujhyasobat ghalavlela every single moment
            majhyasathi special hota. Tujha smile, tu bolnyachi
            style, ani agdi simple moments pan memorable
            karaychi tuzhi way — these are things I still
            remember. You have a warmth and a presence that
            made ordinary days feel different, and I'm
            genuinely glad I got to know you.</p>
            <p>I don't want to put pressure on you or make
            things awkward. I just didn't want to leave
            these words unsaid. You mattered to me, and
            the good memories still mean something to me.</p>
        </div>
        <div class="divider">one simple question</div>
        <div class="question">
            <p class="question-title">
                Would you be open to coffee sometime? ☕
            </p>
            <p class="question-sub">
                Just a calm conversation, no pressure
                and no expectations.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        yes_col, no_col = st.columns(2)

        with yes_col:
            if st.button(
                "Yes, coffee sounds okay",
                key="yes_coffee",
                use_container_width=True,
            ):
                st.session_state.coffee_response = "yes"

        with no_col:
            if st.button(
                "No, thank you",
                key="no_coffee",
                use_container_width=True,
            ):
                st.session_state.coffee_response = "no"

        if st.session_state.coffee_response == "yes":
            st.success(
                "That would be nice. ☕ Text me whenever "
                "you're comfortable, and you can choose "
                "the time and place. We can keep it simple."
            )
        elif st.session_state.coffee_response == "no":
            st.info(
                "That's completely okay. Thank you for "
                "reading this. I respect your answer "
                "and won't push."
            )

st.markdown(
    '<p class="footer">Made with care. Your answer is yours '
    'to choose, and either answer will be respected.</p>',
    unsafe_allow_html=True,
)
