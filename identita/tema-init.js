(() => {
  const root = document.documentElement;
  const valid = value => value === 'light' ? 'light' : 'dark';
  let preference = 'dark';
  try { preference = valid(localStorage.getItem('stringhe-theme')); } catch {}
  function apply(value) {
    preference = valid(value);
    root.dataset.themePreference = preference;
    root.dataset.theme = preference;
    document.querySelectorAll('[data-theme-toggle]').forEach(button => {
      button.setAttribute('aria-checked', String(preference === 'dark'));
      button.querySelector('[data-theme-label]').textContent = preference === 'dark' ? 'Scuro' : 'Chiaro';
    });
  }
  window.stringheTheme = value => {
    apply(value);
    try { localStorage.setItem('stringhe-theme', preference); } catch {}
  };
  window.addEventListener('storage', event => {
    if (event.key === 'stringhe-theme' || event.key === null) apply(event.newValue);
  });
  apply(preference);
})();
