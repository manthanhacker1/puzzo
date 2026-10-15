<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Secret Vibe Check 🔒✨</title>
  <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Plus Jakarta Sans', sans-serif;
    }
    body {
      background: linear-gradient(135deg, #a1c4fd 0%, #c2e9fb 100%);
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 20px;
    }
    .card {
      background: rgba(255, 255, 255, 0.9);
      backdrop-filter: blur(16px);
      border: 1px solid rgba(255, 255, 255, 0.8);
      padding: 35px 25px;
      border-radius: 28px;
      box-shadow: 0 20px 40px rgba(161, 196, 253, 0.35);
      text-align: center;
      max-width: 380px;
      width: 100%;
      animation: fadeIn 0.4s ease-out;
    }
    .screen {
      display: none;
    }
    .screen.active {
      display: block;
    }
    .badge {
      font-size: 54px;
      margin-bottom: 12px;
      display: inline-block;
      animation: float 3s ease-in-out infinite;
    }
    h2 {
      color: #1e293b;
      font-weight: 800;
      font-size: 22px;
      line-height: 1.35;
      margin-bottom: 8px;
    }
    p.subtext {
      color: #64748b;
      font-size: 14px;
      margin-bottom: 20px;
    }
    .input-box {
      margin: 15px 0;
      text-align: left;
    }
    input[type="password"], input[type="text"] {
      width: 100%;
      padding: 12px 16px;
      border: 2px solid #e2e8f0;
      border-radius: 14px;
      outline: none;
      font-size: 15px;
      text-align: center;
      font-weight: 600;
      color: #1e293b;
      transition: border-color 0.2s;
    }
    input:focus {
      border-color: #8b5cf6;
    }
    .error-container {
      display: none;
      margin-top: 10px;
      text-align: center;
    }
    .error-msg {
      color: #ef4444;
      font-size: 13px;
      font-weight: 700;
    }
    .hint-text {
      font-size: 12px;
      color: #8b5cf6;
      font-weight: 600;
      margin-top: 4px;
    }
    .btn-group {
      display: flex;
      justify-content: center;
      gap: 12px;
      margin-top: 20px;
      position: relative;
    }
    button {
      background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
      color: white;
      border: none;
      padding: 12px 28px;
      border-radius: 16px;
      font-size: 15px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 0 8px 15px rgba(99, 102, 241, 0.3);
      transition: all 0.2s ease;
    }
    button:hover {
      transform: translateY(-2px);
      box-shadow: 0 12px 20px rgba(99, 102, 241, 0.4);
    }
    #noBtn {
      background: #e2e8f0;
      color: #475569;
      box-shadow: none;
      position: relative;
    }
    .grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 10px;
      margin: 15px 0;
    }
    .option-card {
      background: white;
      border: 2px solid #e2e8f0;
      border-radius: 16px;
      padding: 14px 16px;
      cursor: pointer;
      font-weight: 600;
      font-size: 14px;
      color: #334155;
      text-align: left;
      display: flex;
      align-items: center;
      gap: 12px;
      transition: all 0.2s ease;
    }
    .option-card:hover, .option-card.selected {
      border-color: #8b5cf6;
      background: #f5f3ff;
      color: #7c3aed;
      transform: scale(1.02);
    }
    .result-box {
      background: #f5f3ff;
      border: 2px dashed #8b5cf6;
      border-radius: 20px;
      padding: 20px;
      margin: 20px 0;
    }
    .score-title {
      font-size: 13px;
      color: #6d28d9;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    .score-val {
      font-size: 32px;
      font-weight: 800;
      color: #7c3aed;
      margin: 6px 0;
    }
    .ps-text {
      font-size: 12px;
      color: #94a3b8;
      margin-top: 16px;
      font-style: italic;
    }
    @keyframes float {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-8px); }
    }
    @keyframes fadeIn {
      from { opacity: 0; transform: scale(0.95); }
      to { opacity: 1; transform: scale(1); }
    }
  </style>
</head>
<body>

  <div class="card">
    
    <!-- Screen 0: Password Lock Screen -->
    <div id="screen0" class="screen active">
      <div class="badge">🔒✨</div>
      <h2>Secret Vault Access</h2>
      <p class="subtext">Enter password to unlock this quiz</p>
      
      <div class="input-box">
        <input type="password" id="passInput" placeholder="Enter password...">
        <div id="errorContainer" class="error-container">
          <p class="error-msg">Wrong password! Try again 😉</p>
          <p class="hint-text">💡 Hint: Try your name</p>
        </div>
      </div>

      <button style="width: 100%; margin-top: 10px;" onclick="checkPassword()">Unlock Quiz 🔑</button>
    </div>

    <!-- Screen 1: The Main Question -->
    <div id="screen1" class="screen">
      <div class="badge">👀💖</div>
      <h2>Hey Janvi! Do you agree we have the best chemistry?</h2>
      <p class="subtext">Honest answers only! No backing out 😎</p>
      <div class="btn-group">
        <button id="yesBtn">YES, ALWAYS 💥</button>
        <button id="noBtn">NOPE 😜</button>
      </div>
    </div>

    <!-- Screen 2: Vibe Selector -->
    <div id="screen2" class="screen">
      <div class="badge">🔥⚡</div>
      <h2>Knew it! Now pick our main energy:</h2>
      <p class="subtext">What describes us best?</p>
      <div class="grid">
        <div class="option-card" onclick="selectVibe(this, 'Unstoppable Chaos 🌪️')">
          <span style="font-size: 22px;">🌪️</span> Unstoppable Chaos
        </div>
        <div class="option-card" onclick="selectVibe(this, 'Late Night Talks & Snacks 🍕')">
          <span style="font-size: 22px;">🍕</span> Late Night Talks & Food
        </div>
        <div class="option-card" onclick="selectVibe(this, 'Telepathic Understanding 🧠')">
          <span style="font-size: 22px;">🧠</span> Just Eye Contact & Laughing
        </div>
      </div>
      <button style="width: 100%; margin-top: 10px;" onclick="showFinal()">Calculate Vibe Score 🚀</button>
    </div>

    <!-- Screen 3: Final Verification Screen -->
    <div id="screen3" class="screen">
      <div class="badge">👑💯</div>
      <h2>Official Vibe Verification</h2>
      
      <div class="result-box">
        <div class="score-title">Compatibility Match</div>
        <div class="score-val">100% MATCH</div>
        <p id="vibeTag" style="color: #4c1d95; font-size: 14px; font-weight: 600;"></p>
      </div>

      <button style="width: 100%;" onclick="confetti({ particleCount: 150, spread: 90 })">Certified Top Pair! 🎉</button>
      <p class="ps-text">P.S. Code built specially for Janvi ✨</p>
    </div>

  </div>

  <script>
    let chosenVibe = 'Unstoppable Chaos 🌪️';

    function checkPassword() {
      const inputVal = document.getElementById('passInput').value.trim().toLowerCase();
      const errorContainer = document.getElementById('errorContainer');

      if (inputVal === 'janvi') {
        errorContainer.style.display = 'none';
        confetti({ particleCount: 80, spread: 60 });
        nextScreen(1);
      } else {
        errorContainer.style.display = 'block';
      }
    }

    function nextScreen(n) {
      document.querySelectorAll('.screen').forEach(s => s.classList.remove('active'));
      document.getElementById('screen' + n).classList.add('active');
    }

    document.getElementById('yesBtn').addEventListener('click', () => {
      confetti({
        particleCount: 120,
        spread: 80,
        origin: { y: 0.6 }
      });
      nextScreen(2);
    });

    const noBtn = document.getElementById('noBtn');
    noBtn.addEventListener('mouseover', () => {
      const x = Math.random() * 160 - 80;
      const y = Math.random() * 160 - 80;
      noBtn.style.transform = `translate(${x}px, ${y}px)`;
    });

    function selectVibe(el, vibe) {
      document.querySelectorAll('.option-card').forEach(i => i.classList.remove('selected'));
      el.classList.add('selected');
      chosenVibe = vibe;
    }

    function showFinal() {
      document.getElementById('vibeTag').innerText = `Vibe: ${chosenVibe}`;
      nextScreen(3);
      confetti({ particleCount: 120, spread: 80 });
    }
  </script>
</body>
</html>
