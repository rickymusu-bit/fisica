(() => {
  document.querySelectorAll('[data-logo-toggle]').forEach(button => {
    const logo = button.querySelector('svg');
    if (!logo || typeof logo.pauseAnimations !== 'function') return;
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
    let playing = !reduced.matches;
    function sync() {
      if (playing) logo.unpauseAnimations();
      else logo.pauseAnimations();
      const label = playing ? 'Metti in pausa l’animazione del logo' : 'Riprendi l’animazione del logo';
      button.setAttribute('aria-label', label);
      button.dataset.functionName = label;
      button.removeAttribute('title');
      button.setAttribute('aria-pressed', String(!playing));
    }
    button.disabled = false;
    button.addEventListener('click', () => {
      logo.setAttribute('data-motion', 'manual');
      playing = !playing;
      sync();
    });
    reduced.addEventListener('change', () => {
      logo.removeAttribute('data-motion');
      playing = !reduced.matches;
      sync();
    });
    sync();
  });
})();
