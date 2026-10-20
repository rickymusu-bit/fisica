(() => {
  window.stringheTheme.refresh();
  document.querySelectorAll('[data-theme-menu]').forEach(menu => {
    menu.querySelectorAll('[data-theme-option]').forEach(button => {
      button.disabled = false;
      button.addEventListener('click', () => {
        window.stringheTheme(button.dataset.themeOption);
        menu.open = false;
        menu.querySelector('summary').focus({preventScroll:true});
      });
    });
  });
  document.addEventListener('click', event => {
    document.querySelectorAll('[data-theme-menu][open]').forEach(menu => {
      if (!menu.contains(event.target)) menu.open = false;
    });
  });
  document.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    document.querySelectorAll('[data-theme-menu][open]').forEach(menu => {
      menu.open = false;
      menu.querySelector('summary').focus({preventScroll:true});
    });
  });
  // Le copie scaricate mantengono i rimandi al portale; online restano nel ramo corrente.
  if (location.protocol === 'file:') {
    document.querySelectorAll('[data-site-path]').forEach(link => {
      link.href = 'https://rickymusu-bit.github.io/fisica/' + link.dataset.sitePath;
    });
  }
  // Con la tastiera rendi visibile l’etichetta, senza riportare a vista il radio nascosto.
  document.addEventListener('focusin', event => {
    if (event.target.matches('.curve-choice:focus-visible')) {
      event.target.labels[0]?.scrollIntoView({block:'nearest',inline:'nearest',behavior:'instant'});
    }
  });
  const index = document.querySelector('.reader-index');
  if (index) index.addEventListener('toggle', () => {
    const label = index.open ? 'Chiudi indice' : 'Indice del capitolo';
    index.querySelector('summary').setAttribute('aria-label', label);
    index.querySelector('summary').title = label;
    document.querySelectorAll('.top-links > :not(.reader-index)').forEach(item => { item.inert = index.open; });
  });
  const bar = document.querySelector('.topbar');
  if (bar && typeof ResizeObserver === 'function') {
    new ResizeObserver(() => {
      document.documentElement.style.setProperty('--nav-height', bar.offsetHeight + 'px');
    }).observe(bar);
  }
})();
