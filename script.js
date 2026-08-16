let currentLevel = 1;

function nextLevel(choice) {
  const title = document.getElementById("title");
  const description = document.getElementById("description");
  const area = document.getElementById("interactive-area");
  const feedback = document.getElementById("feedback");

  if (currentLevel === 1) {
    if (choice === 1) {
      currentLevel = 2;
      title.innerText = "Level 2: Priorities Check";
      description.innerText = "What is the official protocol for a lazy weekend?";
      area.innerHTML = `
        <button onclick="nextLevel(1)">Option A: Good food, coffee, & zero alarms</button>
        <button onclick="nextLevel(0)">Option B: Waking up at 6 AM to do chores</button>
      `;
      feedback.style.color = "#3fb950";
      feedback.innerText = "Correct. Passed Level 1!";
    } else {
      feedback.style.color = "#f85149";
      feedback.innerText = "Incorrect choice. Try again!";
    }
  } 
  else if (currentLevel === 2) {
    if (choice === 1) {
      currentLevel = 3;
      document.getElementById("badge").innerText = "ACCESS GRANTED";
      document.getElementById("badge").style.background = "#8957e5";
      
      title.innerText = "Verification Complete 🏆";
      description.innerText = "Congratulations! You passed all security levels.";
      area.innerHTML = `
        <div style="background: #0d1117; padding: 15px; border-radius: 8px; border: 1px solid #30363d; text-align: left;">
          <strong style="color: #f0f6fc;">Unlocked Voucher:</strong><br>
          <span style="color: #8b949e; font-size: 0.9rem;">1x Coffee / Cheesecake Date on me.</span><br><br>
          <em style="color: #58a6ff; font-size: 0.85rem;">*Claimable whenever you decide to stop playing hard to get.*</em>
        </div>
      `;
      feedback.style.color = "#3fb950";
      feedback.innerText = "100% Vibe Match.";
    } else {
      feedback.style.color = "#f85149";
      feedback.innerText = "Wrong protocol. Who wakes up early on weekends?";
    }
  }
}
