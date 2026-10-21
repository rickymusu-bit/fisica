(() => {
  document.querySelectorAll('[data-zoom-copy]').forEach(image => {
    image.src = image.closest('figure').querySelector('.overview img').src;
  });
  document.querySelectorAll('.image-zoom').forEach(zoom => {
    const button = zoom.querySelector('summary');
    const sync = () => {
      const label = zoom.open ? 'Rimpicciolisci l’immagine' : 'Ingrandisci l’immagine';
      button.setAttribute('aria-label', label);
      button.dataset.functionName = label;
      button.removeAttribute('title');
    };
    zoom.addEventListener('toggle', sync);
    sync();
  });
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('.gif-stage').forEach(stage => {
    const image = stage.querySelector('img');
    const button = stage.querySelector('[data-animation-toggle]');
    const animation = image.getAttribute('src'), still = image.dataset.still;
    if (!button || !still) return;
    // Il picture conserva il fermo per movimento ridotto anche senza JavaScript.
    stage.querySelectorAll('source').forEach(source => { source.media = 'not all'; });
    let playing = !reduced.matches;
    function sync() {
      image.src = playing ? animation : still;
      const label = playing ? 'Metti in pausa l’animazione' : 'Riprendi l’animazione';
      button.setAttribute('aria-label', label);
      button.dataset.functionName = label;
      button.removeAttribute('title');
      button.setAttribute('aria-pressed', String(!playing));
    }
    button.disabled = false;
    button.addEventListener('click', () => { playing = !playing; sync(); });
    reduced.addEventListener('change', () => { playing = !reduced.matches; sync(); });
    sync();
  });
})();
