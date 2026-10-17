(() => {
  function createStateAnimation(canvasId, mode) {
    const canvas = document.getElementById(canvasId);
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const W = canvas.width, H = canvas.height;
    const left = 18, top = 18, width = W - 36, height = H - 36;
    const particles = [];
    const gridSize = 34;
    function rand(a, b) { return a + Math.random() * (b - a); }
    function clamp(v, a, b) { return Math.max(a, Math.min(b, v)); }

    if (mode === 'solid') {
      const cols = 6, rows = 6, gapX = 34, gapY = 26;
      const startX = 58, startY = 52;
      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
          const tx = startX + c * gapX;
          const ty = startY + r * gapY;
          particles.push({ x: tx + rand(-2, 2), y: ty + rand(-2, 2), vx: rand(-0.2, 0.2), vy: rand(-0.2, 0.2), tx, ty, cellX: 0, cellY: 0 });
        }
      }
    } else if (mode === 'liquid') {
      for (let i = 0; i < 38; i++) {
        particles.push({ x: rand(50, W - 50), y: rand(H - 95, H - 40), vx: rand(-0.7, 0.7), vy: rand(-0.7, 0.7), tx: rand(60, W - 60), ty: rand(H - 90, H - 50), cellX: 0, cellY: 0 });
      }
    } else {
      for (let i = 0; i < 28; i++) {
        particles.push({ x: rand(42, W - 42), y: rand(42, H - 42), vx: rand(-1.4, 1.4), vy: rand(-1.4, 1.4), tx: 0, ty: 0, cellX: 0, cellY: 0 });
      }
    }

    function buildGrid() {
      const map = new Map();
      for (const p of particles) {
        p.cellX = Math.floor((p.x - left) / gridSize);
        p.cellY = Math.floor((p.y - top) / gridSize);
        const key = p.cellX + ',' + p.cellY;
        if (!map.has(key)) map.set(key, []);
        map.get(key).push(p);
      }
      return map;
    }

    function drawBox() {
      ctx.clearRect(0, 0, W, H);
      ctx.fillStyle = '#eef2ff';
      ctx.fillRect(0, 0, W, H);
      ctx.strokeStyle = '#c8d1e8';
      ctx.lineWidth = 2;
      ctx.strokeRect(left, top, width, height);
      if (mode === 'liquid') {
        ctx.fillStyle = 'rgba(123,151,255,.10)';
        ctx.fillRect(left + 2, H - 100, width - 4, 82);
      }
    }

    function animate() {
      drawBox();
      const grid = buildGrid();
      const connect = mode !== 'gas';
      const radius = mode === 'solid' ? 42 : mode === 'liquid' ? 30 : 0;

      if (connect) {
        for (const p of particles) {
          for (let gx = p.cellX - 1; gx <= p.cellX + 1; gx++) {
            for (let gy = p.cellY - 1; gy <= p.cellY + 1; gy++) {
              const bucket = grid.get(gx + ',' + gy);
              if (!bucket) continue;
              for (const q of bucket) {
                if (q === p) continue;
                const dx = q.x - p.x, dy = q.y - p.y;
                const d2 = dx * dx + dy * dy;
                if (d2 === 0 || d2 > radius * radius) continue;
                const d = Math.sqrt(d2);
                ctx.strokeStyle = mode === 'solid' ? 'rgba(183,191,214,.38)' : 'rgba(183,191,214,.18)';
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.moveTo(p.x, p.y);
                ctx.lineTo(q.x, q.y);
                ctx.stroke();
                if (d < 11) {
                  const push = (11 - d) * 0.015;
                  p.vx -= dx / d * push;
                  p.vy -= dy / d * push;
                }
              }
            }
          }
        }
      }

      for (const p of particles) {
        if (mode === 'solid') {
          p.vx += (p.tx - p.x) * 0.03 + rand(-0.05, 0.05);
          p.vy += (p.ty - p.y) * 0.03 + rand(-0.05, 0.05);
          p.vx *= 0.88; p.vy *= 0.88;
        } else if (mode === 'liquid') {
          p.vx += rand(-0.14, 0.14) + (p.tx - p.x) * 0.0008;
          p.vy += rand(-0.14, 0.14) + (p.ty - p.y) * 0.0008;
          p.vx *= 0.96; p.vy *= 0.96;
          if (Math.random() < 0.01) { p.tx = rand(60, W - 60); p.ty = rand(H - 92, H - 52); }
        } else {
          p.vx += rand(-0.10, 0.10);
          p.vy += rand(-0.10, 0.10);
          p.vx *= 0.998; p.vy *= 0.998;
        }

        p.x += p.vx; p.y += p.vy;
        let minY = mode === 'liquid' ? H - 102 : top + 10;
        let maxY = H - 20;
        if (mode === 'solid') maxY = H - 30;
        if (mode === 'gas') maxY = top + height - 6; // particle radius 4.7 plus 1.3px clearance inside border
        if (p.x < left + 10) { p.x = left + 10; p.vx *= -1; }
        if (p.x > W - 28) { p.x = W - 28; p.vx *= -1; }
        if (p.y < minY) { p.y = minY; p.vy *= -1; }
        if (p.y > maxY) { p.y = maxY; p.vy *= -1; }

        ctx.beginPath();
        ctx.fillStyle = '#5b6fb8';
        ctx.arc(p.x, p.y, 4.7, 0, Math.PI * 2);
        ctx.fill();
      }
      requestAnimationFrame(animate);
    }
    animate();
  }

  createStateAnimation('solidMotion', 'solid');
  createStateAnimation('liquidMotion', 'liquid');
  createStateAnimation('gasMotion', 'gas');
})();