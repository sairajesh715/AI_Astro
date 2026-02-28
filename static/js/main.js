/* ═══════════════════════════════════════════
   CELESTIA — main.js
   Starfield canvas + form UX
════════════════════════════════════════════ */

// ── Starfield ────────────────────────────────
(function initStarfield() {
  const canvas = document.getElementById('starfield');
  if (!canvas) return;
  const ctx = canvas.getContext('2d');

  let W, H, stars = [];

  function resize() {
    W = canvas.width  = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  function createStars(count) {
    stars = [];
    for (let i = 0; i < count; i++) {
      stars.push({
        x: Math.random() * W,
        y: Math.random() * H,
        r: Math.random() * 1.4 + 0.2,
        alpha: Math.random() * 0.6 + 0.1,
        speed: Math.random() * 0.012 + 0.003,
        phase: Math.random() * Math.PI * 2,
      });
    }
  }

  let frame = 0;

  function draw() {
    ctx.clearRect(0, 0, W, H);
    frame += 0.008;

    for (const s of stars) {
      const a = s.alpha * (0.6 + 0.4 * Math.sin(frame * s.speed * 60 + s.phase));
      ctx.beginPath();
      ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(255,255,255,${a})`;
      ctx.fill();
    }

    requestAnimationFrame(draw);
  }

  resize();
  createStars(220);
  draw();

  window.addEventListener('resize', () => { resize(); createStars(220); });
})();


// ── Form Submit Loading ───────────────────────
(function initForm() {
  const form    = document.getElementById('birthForm');
  const overlay = document.getElementById('loadingOverlay');
  const btn     = document.getElementById('submitBtn');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    // Basic client-side validation
    const name  = form.querySelector('#name').value.trim();
    const dob   = form.querySelector('#dob').value.trim();
    const time  = form.querySelector('#birth_time').value.trim();
    const place = form.querySelector('#birth_place').value.trim();

    if (!name || !dob || !time || !place) return; // let server handle

    if (overlay) overlay.classList.remove('hidden');
    if (btn)     btn.disabled = true;
  });
})();


// ── Animate form field focus glow ─────────────
document.querySelectorAll('input').forEach(inp => {
  inp.addEventListener('focus', () => inp.closest('.field-group')?.classList.add('focused'));
  inp.addEventListener('blur',  () => inp.closest('.field-group')?.classList.remove('focused'));
});
