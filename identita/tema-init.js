(() => {
  const root = document.documentElement;
  const system = matchMedia('(prefers-color-scheme: dark)');
  const valid = value => ['light', 'dark'].includes(value) ? value : 'auto';
  let preference = 'auto';
  try { preference = valid(localStorage.getItem('stringhe-theme')); } catch {}
  function apply(value) {
    preference = valid(value);
    root.dataset.themePreference = preference;
    root.dataset.theme = preference === 'auto' ? (system.matches ? 'dark' : 'light') : preference;
    document.querySelectorAll('[data-theme-select]').forEach(select => { select.value = preference; });
  }
  window.stringheTheme = value => {
    apply(value);
    try {
      if (preference === 'auto') localStorage.removeItem('stringhe-theme');
      else localStorage.setItem('stringhe-theme', preference);
    } catch {}
  };
  system.addEventListener('change', () => { if (preference === 'auto') apply('auto'); });
  window.addEventListener('storage', event => {
    if (event.key === 'stringhe-theme' || event.key === null) apply(event.newValue);
  });
  apply(preference);
})();
