(() => {
  document.querySelectorAll('[data-theme-select]').forEach(select => {
    select.value = document.documentElement.dataset.themePreference || 'auto';
    select.addEventListener('change', () => window.stringheTheme(select.value));
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
