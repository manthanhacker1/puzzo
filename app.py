        <p class="bodycopy">First, <strong>I'm genuinely sorry</strong> for the ways I hurt you or made you feel misunderstood. I'm not saying this to erase anything. I just wish I'd understood it sooner.</p>
        <p class="bodycopy">Tujhyasobat ghalavlela time majhyasathi kharach special hota. Tujha smile, tuzhi way of talking, ani tu agdi normal moments pan special karaychis — those little things are still with me.</p>
        <p class="bodycopy">I always admired how you could be so completely <strong>you</strong>. There's something about your presence that made ordinary days feel different. I don't expect one page to change the past; I just didn't want to pretend those memories meant nothing to me.</p>
      </section>

      <section class="paper">
        <p class="section-label">02 / tiny memory lane</p>
        <h2>Tap a card. Pick a little smile. ✨</h2>
        <p class="bodycopy">Three tiny reminders of the kind of details that tend to stay with someone.</p>
        <div class="cards">
          <article class="memory" tabindex="0" role="button" aria-expanded="false">
            <span class="emoji">🌷</span><h3>Your vibe</h3><p class="reveal">There's a softness in the way you are that makes you memorable without even trying.</p><span class="tap">tap to open ↗</span>
          </article>
          <article class="memory" tabindex="0" role="button" aria-expanded="false">
            <span class="emoji">☁️</span><h3>Little things</h3><p class="reveal">It's rarely the big moments only. It's the random talks and silly little things that stick.</p><span class="tap">tap to open ↗</span>
          </article>
          <article class="memory" tabindex="0" role="button" aria-expanded="false">
            <span class="emoji">💗</span><h3>What I admire</h3><p class="reveal">You have your own way of making an impression. You don't need to try to be anyone else.</p><span class="tap">tap to open ↗</span>
          </article>
        </div>
      </section>

      <section class="paper invite" id="coffee">
        <span class="coffee">☕</span>
        <p class="section-label">03 / the actual question</p>
        <h2>Can I borrow you for a coffee sometime?</h2>
        <p class="bodycopy">No heavy conversation agenda. Just coffee, a little catch-up, and seeing how it feels to talk in person. You can pick the place.</p>
        <div class="vibe-title">Choose the coffee vibe (optional)</div>
        <div class="vibes">
          <button class="vibe" type="button">☕ Cozy café</button>
          <button class="vibe" type="button">🧋 Something cold</button>
          <button class="vibe" type="button">🌆 Evening walk</button>
        </div>
        <div class="actions" id="actions">
          <button class="yes-btn" id="yesBtn" type="button">Okay, let's have coffee ♡</button>
          <button class="no-btn" id="noBtn" type="button">No 🙈</button>
        </div>
        <div class="response" id="yesResponse" aria-live="polite">
          <div class="big">🥹💗☕</div><h3>Wait, really?</h3>
          <p>Okay, this made me smile. Text me whenever you're comfortable and we can figure out a time and place together. No rush. ♡</p>
        </div>
        <div class="response" id="noResponse" aria-live="polite">
          <div class="big">🌷</div><h3>Okay, I hear you.</h3>
          <p>Thank you for reading this far. You can be honest with me; I won't push you. I hope life treats you kindly, Mitali. ♡</p>
        </div>
        <p class="note-after" id="playNote">P.S. The “No” button is a little shy. It may run away once or twice. 😭</p>
      </section>
      <div class="footer">made with care &nbsp;·&nbsp; no pressure, just honesty &nbsp;♡<br>whatever you choose, thank you for being part of my story.</div>
    </section>
  </main>
</div>
<script>
const form=document.getElementById('passForm');
const password=document.getElementById('password');
const hint=document.getElementById('hint');
form.addEventListener('submit',function(e){
  e.preventDefault();
  if(password.value.trim().toLowerCase()==='mitali'){
    document.getElementById('gate').style.display='none';
    document.getElementById('main').style.display='block';
    window.scrollTo({top:0,behavior:'smooth'});
    burst(window.innerWidth/2,180);
  } else {
    hint.textContent='Not quite… hint: try entering your name 😉';
    password.value='';
    password.focus();
  }
});
// Tap-to-reveal memory cards
function revealCard(card){card.classList.toggle('revealed');card.setAttribute('aria-expanded',card.classList.contains('revealed')?'true':'false');}
document.querySelectorAll('.memory').forEach(card=>{
  card.addEventListener('click',()=>revealCard(card));
  card.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();revealCard(card);}});
});
// Coffee-vibe selection
let pickedVibe='';
document.querySelectorAll('.vibe').forEach(btn=>btn.addEventListener('click',()=>{
  document.querySelectorAll('.vibe').forEach(b=>b.classList.remove('selected'));
  btn.classList.add('selected');pickedVibe=btn.textContent.trim();
}));
function burst(x,y){
  const bits=['♡','💗','✦','🌷','✨'];
  for(let i=0;i<15;i++){
    const el=document.createElement('span');el.className='heart';el.textContent=bits[Math.floor(Math.random()*bits.length)];
    el.style.left=(x+(Math.random()-.5)*220)+'px';el.style.top=(y+(Math.random()-.5)*60)+'px';el.style.animationDelay=(Math.random()*.25)+'s';
    document.body.appendChild(el);setTimeout(()=>el.remove(),1800);
  }
}
const yesBtn=document.getElementById('yesBtn'),noBtn=document.getElementById('noBtn');
const actions=document.getElementById('actions');let dodges=0,settled=false;
function dodgeNo(){
  if(settled)return;
  dodges++;
  if(dodges>=4){
    noBtn.textContent='Okay, honestly no';
    noBtn.style.transform='none';noBtn.style.position='static';
    document.getElementById('playNote').textContent='Okay okay 😭 no more running. Choose whatever feels right.';
    return;
  }
  const area=actions.getBoundingClientRect();
  const maxX=Math.max(8,area.width-noBtn.offsetWidth-8);
  const maxY=46;
  noBtn.style.position='absolute';
  noBtn.style.left=(Math.random()*maxX)+'px';
  noBtn.style.top=((Math.random()-.5)*maxY)+'px';
  noBtn.style.transform='rotate('+(Math.random()*12-6)+'deg)';
  document.getElementById('playNote').textContent=['Oops, too slow 🙈','She said: catch me if you can 😭','Okay this button is dramatic.'][Math.min(dodges-1,2)];
}
noBtn.addEventListener('pointerenter',dodgeNo);
noBtn.addEventListener('click',()=>{
  if(dodges<4){dodgeNo();return;}
  settled=true;
  document.getElementById('yesResponse').classList.remove('show');
  document.getElementById('noResponse').classList.add('show');
  document.getElementById('playNote').textContent='Thank you for being honest. ♡';
  burst(window.innerWidth/2,window.scrollY+window.innerHeight*.65);
  document.getElementById('noResponse').scrollIntoView({behavior:'smooth',block:'center'});
});
yesBtn.addEventListener('click',()=>{
  settled=true;
  document.getElementById('noResponse').classList.remove('show');
  const response=document.getElementById('yesResponse');
  response.classList.add('show');
  const p=response.querySelector('p');
  p.textContent='Okay, this made me smile. '+(pickedVibe?'You picked '+pickedVibe+'. ':'')+'Text me whenever you\'re comfortable and we can figure out a time and place together. No rush. ♡';
  document.getElementById('playNote').textContent='One little yes just made this whole page worth it. 💗';
  burst(window.innerWidth/2,window.scrollY+window.innerHeight*.65);
  response.scrollIntoView({behavior:'smooth',block:'center'});
