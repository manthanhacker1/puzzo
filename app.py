
/* ===== DARK ROMANTIC THEME ===== */

:root {
    --ink: #f7edf5;
    --muted: #b7a5c0;
    --rose: #f09abb;
    --deep: #ff9ec6;
    --cream: #171321;
    --line: #403044;
}

html {
    background: #0b0912;
}

body {
    color: var(--ink);
    background:
        radial-gradient(ellipse at 5% 5%,
            rgba(139, 52, 111, .24), transparent 38%),
        radial-gradient(ellipse at 100% 55%,
            rgba(88, 55, 155, .24), transparent 38%),
        linear-gradient(145deg, #0b0912, #15101f 55%, #100c1b);
}

.app {
    color: var(--ink);
}

.topline {
    color: #c2afca;
}

.topline span {
    color: #ff8fbc;
}

.panel {
    background: rgba(24, 19, 34, .88);
    border: 1px solid rgba(241, 176, 216, .14);
    box-shadow:
        0 24px 70px rgba(0, 0, 0, .35),
        0 0 35px rgba(143, 63, 137, .08);
    backdrop-filter: blur(18px);
    -webkit-backdrop-filter: blur(18px);
}

.panel::before {
    background: rgba(160, 73, 143, .13);
}

h1, h2, .serif {
    color: #fff2fa;
}

h1 em, h2 em {
    color: #ff9fc7;
}

.sub {
    color: #bbaabe;
}

.sticker {
    background: linear-gradient(145deg, #43223f, #282043);
    color: #ffadd0;
    box-shadow: 0 10px 30px rgba(217, 90, 170, .13);
    border: 1px solid rgba(255, 166, 212, .14);
}

.tag {
    color: #ffadd0;
    background: #2e1c31;
    border: 1px solid #55304e;
}

.input-wrap input {
    color: #fff0fa;
    background: #110e19;
    border: 1px solid #463047;
}

.input-wrap input::placeholder {
    color: #8f7c98;
}

.input-wrap input:focus {
    border-color: #dc81b4;
    box-shadow: 0 0 0 4px rgba(220, 129, 180, .12);
}

.primary {
    color: white;
    background: linear-gradient(110deg, #9c397b, #d45c98);
    box-shadow: 0 8px 28px rgba(190, 66, 147, .22);
}

.primary:hover {
    box-shadow: 0 12px 34px rgba(190, 66, 147, .35);
}

.hint {
    color: #ffafd0;
    background: #2a1728;
    border-color: #64324e;
}

.small-note,
.footer {
    color: #92809d;
}

.prose {
    color: #d2c1d5;
}

.prose strong {
    color: #ffa3ca;
}

.divider {
    background: linear-gradient(
        90deg, transparent, #55334e, transparent
    );
}

.section-label {
    color: #d99bc7;
}

.memory {
    background: linear-gradient(145deg, #25192d, #201a32);
    border: 1px solid #443047;
    color: #f7eaf7;
}

.memory:hover {
    background: linear-gradient(145deg, #332039, #29203f);
    border-color: #8f497e;
}

.memory.open {
    background: #211a30;
    border-color: #b46c9e;
}

.memory .m-title {
    color: #f9eafa;
}

.memory .m-tap {
    color: #ad96b6;
}

.memory .reveal {
    color: #e3b5d3;
}

.compliment {
    background: linear-gradient(125deg, #2e1a30, #201b3b);
    border: 1px solid #54304f;
}

.compliment p {
    color: #ffd3e8;
}

.compliment small {
    color: #bca2c2;
}

.coffee {
    background: linear-gradient(145deg, #1e1729, #171321);
    border: 1px solid #493047;
}

.coffee p {
    color: #bcaabe;
}

.vibe-label {
    color: #c2a3c6;
}

.vibe {
    background: #211829;
    border: 1px solid #453047;
    color: #e4cde3;
}

.vibe:hover {
    border-color: #a05287;
}

.vibe.active {
    background: #49243f;
    color: #ffb7d8;
    border-color: #c65d9d;
    box-shadow: 0 0 16px rgba(198, 93, 157, .12);
}

#vibe-caption {
    color: #c0a9c8 !important;
}

.choice-zone {
    background: #120e1a;
    border: 1px dashed #67415f;
}

.yes {
    color: white;
    background: linear-gradient(110deg, #a13f82, #db609b);
    box-shadow: 0 6px 22px rgba(204, 66, 151, .25);
}

.yes:hover {
    box-shadow: 0 8px 30px rgba(204, 66, 151, .4);
}

.no {
    color: #e5bfdc;
    background: #251a2c;
    border: 1px solid #69405e;
}

.no:hover {
    background: #302039;
    border-color: #a75b8e;
}

.response {
    color: #f8eafb;
    background: linear-gradient(130deg, #301c34, #251b3b);
    border: 1px solid #684064;
}

.response h3 {
    color: #ffafd1;
}

.response p {
    color: #dfc9e2;
}

.footer {
    color: #95819f;
}

::selection {
    color: white;
    background: #9e4784;
}

@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: .01ms !important;
        transition-duration: .01ms !important;
    }
}
