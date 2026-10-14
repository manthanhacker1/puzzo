
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
.stApp { background: #0b0912; }
[data-testid="stMainBlockContainer"] {
    padding: 0 !important;
    max-width: 100% !important;
}
iframe { border: none !important; }
</style>
""", unsafe_allow_html=True)

APP_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:ital,wght@0,500;0,600;1,500&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box}
:root{--ink:#f7edf5;--muted:#b7a5c0;--pink:#f09abb;--deep:#ff9ec6}
body{
 margin:0;color:var(--ink);font-family:'DM Sans',sans-serif;
 background:radial-gradient(ellipse at 5% 5%,#51203f55,transparent 40%),
 radial-gradient(ellipse at 100% 60%,#49317c44,transparent 40%),#0b0912
}
button,input{font:inherit}
button{cursor:pointer;-webkit-tap-highlight-color:transparent}
.app{max-width:720px;margin:auto;padding:25px 14px 40px}
.topline{text-align:center;color:#c2afca;font-size:10px;letter-spacing:2px;margin:4px 0 24px}
.panel{
 background:rgba(24,19,34,.94);border:1px solid #ffffff13;
 border-radius:26px;padding:clamp(20px,5vw,38px);
 box-shadow:0 24px 70px #0007,0 0 30px #a53e8210;
}
.center{text-align:center}
.sticker{
 width:70px;height:70px;display:grid;place-items:center;margin:8px auto 20px;
 border-radius:23px;background:linear-gradient(145deg,#43223f,#282043);
 font-size:33px;transform:rotate(-5deg)
}
h1,h2,h3{font-family:'Playfair Display',Georgia,serif;font-weight:500}
h1{font-size:clamp(36px,8vw,55px);line-height:1.15;letter-spacing:-1px;margin:0 0 15px}
h1 em,h2 em{color:#ff9fc7}
h2{font-size:clamp(28px,6vw,40px);line-height:1.2}
.sub{color:var(--muted);font-size:14px;line-height:1.9;max-width:440px;margin:0 auto 25px}
.tag{display:inline-block;padding:8px 13px;border-radius:50px;background:#2e1c31;color:#ffadd0;border:1px solid #55304e;letter-spacing:1px;font-size:10px;font-weight:700;margin-bottom:18px}
.input-wrap{max-width:390px;margin:auto}
input{
 width:100%;padding:16px;border:1px solid #463047;border-radius:14px;
 background:#110e19;color:#fff0fa;text-align:center;margin-bottom:12px
}
.primary,.yes{
 width:100%;padding:15px;border:0;border-radius:14px;color:white;font-weight:700;
 background:linear-gradient(110deg,#9c397b,#e05c9e);
 box-shadow:0 0 22px #ff69ad35;transition:.2s
}
.primary:hover,.yes:hover{transform:translateY(-2px);box-shadow:0 0 28px #ff69ad70}
.hint{display:none;margin:12px auto;color:#ffafd0;background:#2a1728;border:1px solid #64324e;border-radius:12px;padding:12px;font-size:13px}
#letter{display:none}
.prose{font-size:14px;line-height:2;color:#d2c1d5}
.prose strong{color:#ffa3ca}
.divider{height:1px;background:linear-gradient(90deg,transparent,#55334e,transparent);margin:27px 0}
.label{text-align:center;font-size:10px;text-transform:uppercase;letter-spacing:2px;color:#d99bc7;margin-bottom:15px}
.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:9px}
.memory{
 min-width:0;min-height:130px;padding:12px 6px;border-radius:17px;
 background:linear-gradient(145deg,#25192d,#201a32);border:1px solid #443047;color:#f7eaf7
}
.memory .emoji{display:block;font-size:24px;margin-bottom:9px}
.memory .title{display:block;font-size:11px;font-weight:700}
.memory .tap{display:block;color:#ad96b6;font-size:10px;margin-top:9px}
.memory .reveal{display:none;color:#e3b5d3;font-size:10px;line-height:1.6;margin-top:9px}
.memory.open .reveal{display:block}
.memory.open .tap{display:none}
.compliment,.coffee{
 text-align:center;padding:22px 15px;border-radius:21px;
 background:linear-gradient(125deg,#2e1a30,#201b3b);border:1px solid #54304f
}
.compliment p{font-family:'Playfair Display',Georgia,serif;color:#ffd3e8;font-size:21px;line-height:1.6}
.compliment small{color:#bca2c2}
.coffee p{color:#bcaabe;font-size:13px;line-height:1.8;max-width:440px;margin:12px auto}
.cup{font-size:37px;animation:float 3s ease-in-out infinite}
@keyframes float{50%{transform:translateY(-7px) rotate(3deg)}}
.vibes{display:flex;justify-content:center;flex-wrap:wrap;gap:8px;margin:12px 0}
.vibe{padding:10px 12px;border-radius:30px;background:#211829;border:1px solid #453047;color:#e4cde3;font-size:11px}
.vibe.active{background:#49243f;color:#ffb7d8;border-color:#c65d9d}
.caption{font-size:11px!important;color:#c0a9c8!important}
.zone{
 position:relative;display:flex;align-items:center;justify-content:center;gap:12px;
 height:112px;margin-top:17px;overflow:hidden;border-radius:18px;
 background:#120e1a;border:1px dashed #67415f
}
.choice{width:45%;max-width:180px;padding:14px 6px;border-radius:13px;font-weight:700;font-size:12px}
.yes{animation:pulse 2s infinite}
@keyframes pulse{50%{box-shadow:0 0 27px #ff69ad70}}
.no{background:#251a2c;border:1px solid #69405e;color:#e5bfdc}
.response{display:none;margin-top:18px;padding:18px;border-radius:16px;background:#301c34;border:1px solid #684064;text-align:center}
.response h3{color:#ffafd1;font-size:25px;margin:8px 0}
.response p{color:#dfc9e2;font-size:13px;line-height:1.8}
.footer{text-align:center;color:#95819f;font-size:10px;line-height:1.8;margin-top:23px}
.heart{position:fixed;pointer-events:none;z-index:10;animation:rise 2.5s ease-out forwards}
@keyframes rise{0%{opacity:0;transform:translateY(0) scale(.6)}15%{opacity:1}100%{opacity:0;transform:translateY(-230px) scale(1.3) rotate(20deg)}}
@media(max-width:420px){
 .app{padding:18px 10px 28px}
 .panel{padding:21px 15px}
 .grid{gap:6px}
 .memory{min-height:135px}
 .choice{font-size:11px}
}
</style>
</head>
<body>
<div class="app">
 <div class="topline">♡ &nbsp; A LITTLE SOMETHING FOR YOU &nbsp; ♡</div>

 <section id="gate" class="panel center">
  <div class="sticker">💌</div>
  <div class="tag">NOT A BORING TEXT, PROMISE</div>
  <h1>Hey, <em>Mitali.</em></h1>
  <p class="sub">I made you a little something instead of sending another long message. There's a note inside. 🌷</p>
  <form id="password-form" class="input-wrap">
   <input id="password" type="password" placeholder="Your secret password..." autocomplete="off">
   <button class="primary" type="submit">Open your little surprise ♡</button>
  </form>
  <div id="hint" class="hint">Not quite 🙈 Hint: try entering your name.</div>
  <p style="color:#95819f;font-size:10px;margin-top:22px">made with a little courage & a lot of thought ✿</p>
 </section>

 <section id="letter" class="panel">
  <div class="center">
   <div class="sticker">🌷</div>
   <div class="tag">FROM MY HEART, HONESTLY</div>
   <h1>A little note<br>for <em>you.</em></h1>
   <p class="sub">No fancy speeches. Just a few things I wanted to tell you properly. ♡</p>
  </div>

  <div class="divider"></div>
  <div class="prose">
   <p>Hey Mitali,</p>
   <p>First of all, <strong>I'm genuinely sorry</strong> for the ways I hurt you or made you feel misunderstood. I can't change the past, but I wish I had understood things better. I'm not asking you to forget anything.</p>
   <p>Tujhyasobat ghalavlela every single moment majhyasathi special hota. Even the smallest things still mean something to me. Some memories stay with us even when life changes.</p>
   <p>And honestly, there's something special about you. Tujha smile, tu bolnyachi style, tujhya little expressions, ani tu agdi simple moments pan memorable banavtes. It's your vibe, your personality, and the person you are. I genuinely admire that.</p>
   <p>I know one message can't fix everything. I just wanted you to know that the good memories were real to me, and so was the care I had for you.</p>
  </div>

  <div class="divider"></div>
  <div class="label">♡ THREE TINY REMINDERS</div>
  <div class="grid">
   <button class="memory" onclick="toggleMemory(this)">
    <span class="emoji">🌸</span><span class="title">Your vibe</span><span class="tap">tap to open ↗</span>
    <span class="reveal">You have a way of making ordinary moments feel special.</span>
   </button>
   <button class="memory" onclick="toggleMemory(this)">
    <span class="emoji">✨</span><span class="title">Your smile</span><span class="tap">tap to open ↗</span>
    <span class="reveal">It's one of those little things that makes a memory stick around.</span>
   </button>
   <button class="memory" onclick="toggleMemory(this)">
    <span class="emoji">🫶</span><span class="title">Little things</span><span class="tap">tap to open ↗</span>
    <span class="reveal">Sometimes the smallest moments end up meaning the most.</span>
   </button>
  </div>

  <div class="divider"></div>
  <div class="compliment">
   <div style="font-size:25px">♡</div>
   <p>"You don't have to try to be special. There's already something lovely about the way you are."</p>
   <small style="color:#bca2c2;font-size:11px">just something I wanted you to know 🌷</small>
  </div>

  <div class="divider"></div>
  <section class="coffee">
   <div class="cup">☕</div>
   <div class="tag">ONE LITTLE QUESTION</div>
   <h2>Can I steal you<br>for <em>one coffee?</em></h2>
   <p>Just a simple coffee and a calm conversation. No dramatic expectations, no pressure. We can just talk, if you're comfortable.</p>
   <div class="label" style="margin-top:20px">CHOOSE THE VIBE ☁️</div>
   <div class="vibes">
    <button class="vibe active" onclick="chooseVibe(this,'A cozy café')">☕ Cozy café</button>
    <button class="vibe" onclick="chooseVibe(this,'Something cold')">🧋 Something cold</button>
    <button class="vibe" onclick="chooseVibe(this,'An evening walk')">🌇 Evening walk</button>
   </div>
   <p id="caption" class="caption">Current vibe: a cozy café ♡</p>

   <div id="zone" class="zone">
    <button id="yes" class="choice yes" onclick="answer('yes')">YES, LET'S GO ♡</button>
    <button id="no" class="choice no" onclick="answer('no')">No, thank you</button>
   </div>
   <p style="font-size:10px;margin-top:12px">P.S. One button is a little shy 🙈</p>

   <div id="yes-response" class="response">
    <div style="font-size:30px">🥹☕💗</div>
    <h3>Wait, really? ♡</h3>
    <p id="yes-text">That made me smile! Let's figure out a day and place together whenever you're comfortable. No rush.</p>
   </div>
   <div id="no-response" class="response">
    <div style="font-size:27px">🌷</div>
    <h3>That's okay.</h3>
    <p>Thanks for reading my note. I respect your choice. Take care. ♡</p>
   </div>
  </section>
  <div class="footer">made with care, just for this little moment ♡<br>Your choice matters. Always.</div>
 </section>
</div>

<script>
const form = document.getElementById("password-form");
form.addEventListener("submit", function(e) {
 e.preventDefault();
 const input = document.getElementById("password");
 if (input.value.trim().toLowerCase() === "mitali") {
  document.getElementById("gate").style.display = "none";
  document.getElementById("letter").style.display = "block";
  window.scrollTo({top:0,behavior:"smooth"});
  hearts(7);
 } else {
  document.getElementById("hint").style.display = "block";
  input.value = "";
  input.placeholder = "Try again 😉";
 }
});

function toggleMemory(card) {
 card.classList.toggle("open");
 if(card.classList.contains("open")) hearts(2);
}

let vibe = "A cozy café";
function chooseVibe(button, value) {
 vibe = value;
 document.querySelectorAll(".vibe").forEach(b=>b.classList.remove("active"));
 button.classList.add("active");
 document.getElementById("caption").textContent = "Current vibe: " + value + " ♡";
}

let moves = 0;
const noButton = document.getElementById("no");
const zone = document.getElementById("zone");

function dodgeNo() {
 if (moves >= 3) return;
 moves++;
 const maxX = Math.max(0, zone.clientWidth - noButton.offsetWidth - 8);
 const maxY = Math.max(0, zone.clientHeight - noButton.offsetHeight - 8);
 const positions = [[0.55,0.05],[0.04,0.55],[0.52,0.52]];
 const p = positions[moves-1];
 noButton.style.position = "absolute";
 noButton.style.left = Math.max(4,maxX*p[0]) + "px";
 noButton.style.top = Math.max(4,maxY*p[1]) + "px";
 if (moves >= 3) noButton.title = "Now you can choose either option.";
}

noButton.addEventListener("pointerenter", e=>{
 if(e.pointerType === "mouse" && moves < 3) dodgeNo();
});
noButton.addEventListener("pointerdown", e=>{
 if(e.pointerType !== "mouse" && moves < 3) {
  e.preventDefault();
  dodgeNo();
 }
});

function answer(choice) {
 const yes = document.getElementById("yes-response");
 const no = document.getElementById("no-response");
 yes.style.display = choice === "yes" ? "block" : "none";
 no.style.display = choice === "no" ? "block" : "none";
 if(choice === "yes") {
  document.getElementById("yes-text").textContent =
   "That made me smile! Let's figure out " + vibe.toLowerCase() +
   " together whenever you're comfortable. No rush. ♡";
  hearts(22);
 }
 setTimeout(()=>document.getElementById(
  choice === "yes" ? "yes-response" : "no-response"
 ).scrollIntoView({behavior:"smooth",block:"nearest"}),60);
}

function hearts(count) {
 const symbols = ["♡","♥","✿","💕","✨"];
 for(let i=0;i<count;i++) {
  setTimeout(()=>{
   const el = document.createElement("span");
   el.className = "heart";
   el.textContent = symbols[Math.floor(Math.random()*symbols.length)];
   el.style.left = (5+Math.random()*90)+"vw";
   el.style.top = (55+Math.random()*35)+"vh";
   el.style.fontSize = (14+Math.random()*17)+"px";
   el.style.color = ["#d483b4","#b474d5","#ffa3ca"][Math.floor(Math.random()*3)];
   document.body.appendChild(el);
   setTimeout(()=>el.remove(),2600);
  },i*65);
 }
}
</script>
</body>
</html>
"""

components.html(APP_HTML, height=1800, scrolling=True)
