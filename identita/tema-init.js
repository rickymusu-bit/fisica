(() => {
  const root = document.documentElement;
  const valid = value => value === 'light' ? 'light' : 'dark';
  let preference = 'dark';
  try { preference = valid(localStorage.getItem('stringhe-theme')); } catch {}
  function apply(value) {
    preference = valid(value);
    root.dataset.themePreference = preference;
    root.dataset.theme = preference;
    document.querySelectorAll('[data-theme-menu]').forEach(menu => {
      const label = preference === 'dark' ? 'Scuro' : 'Chiaro';
      const summary = menu.querySelector('summary');
      summary.setAttribute('aria-label', 'Tema del sito: ' + label);
      summary.dataset.functionName = 'Tema: ' + label;
      summary.removeAttribute('title');
      menu.querySelectorAll('[data-theme-option]').forEach(button => {
        button.setAttribute('aria-pressed', String(button.dataset.themeOption === preference));
      });
    });
  }
  window.stringheTheme = value => {
    apply(value);
    try { localStorage.setItem('stringhe-theme', preference); } catch {}
  };
  window.stringheTheme.refresh = () => apply(preference);
  window.addEventListener('storage', event => {
    if (event.key === 'stringhe-theme' || event.key === null) apply(event.newValue);
  });
  apply(preference);
})();
