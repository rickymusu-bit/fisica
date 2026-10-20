(() => {
  document.querySelectorAll('[data-theme-toggle]').forEach(button => {
    const dark = document.documentElement.dataset.theme !== 'light';
    button.setAttribute('aria-checked', String(dark));
    button.querySelector('[data-theme-label]').textContent = dark ? 'Scuro' : 'Chiaro';
    button.disabled = false;
    button.addEventListener('click', () => {
      window.stringheTheme(document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark');
    });
  });
  // Le copie scaricate mantengono i rimandi al portale; online restano nel ramo corrente.
  if (location.protocol === 'file:') {
    document.querySelectorAll('[data-site-path]').forEach(link => {
      link.href = 'https://rickymusu-bit.github.io/fisica/' + link.dataset.sitePath;
    });
  }
  const index = document.querySelector('.reader-index');
  if (index) index.addEventListener('toggle', () => {
    document.querySelectorAll('.top-links > :not(.reader-index)').forEach(item => { item.inert = index.open; });
  });
  const bar = document.querySelector('.topbar');
  if (bar && typeof ResizeObserver === 'function') {
    new ResizeObserver(() => {
      document.documentElement.style.setProperty('--nav-height', bar.offsetHeight + 'px');
    }).observe(bar);
  }
})();
