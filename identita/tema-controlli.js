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
  // Fallback per i browser che non raggruppano ancora i details con name.
  document.querySelectorAll('.site-header,.topbar').forEach(header => {
    const menus = [...header.querySelectorAll('details.lang,details.string-lang,details[data-theme-menu]')];
    menus.forEach(menu => menu.addEventListener('toggle', () => {
      if (menu.open) menus.forEach(other => { if (other !== menu) other.open = false; });
    }));
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
  // Suggerimenti comuni: nessun secondo tocco necessario per attivare un comando.
  const tooltip = document.createElement('div');
  tooltip.id = 'function-tooltip';
  tooltip.className = 'function-tooltip';
  tooltip.role = 'tooltip';
  tooltip.hidden = true;
  document.body.append(tooltip);
  const controls = 'button,summary,[role="button"],.string-nav,.site-nav>a,.action,.download,.brand';
  let current = null, timer, leaveTimer;
  const controlAt = target => target instanceof Element ? target.closest(controls) : null;
  function hideTip() {
    clearTimeout(timer);
    clearTimeout(leaveTimer);
    if (current) {
      const ids = (current.getAttribute('aria-describedby') || '').split(/\s+/).filter(id => id && id !== tooltip.id);
      if (ids.length) current.setAttribute('aria-describedby', ids.join(' '));
      else current.removeAttribute('aria-describedby');
    }
    current = null;
    tooltip.hidden = true;
  }
  function showTip(control, touch = false) {
    if (!control || control.disabled) return;
    hideTip();
    const name = control.getAttribute('aria-label') || control.getAttribute('title') ||
      control.dataset.functionName || control.querySelector('strong')?.textContent || control.textContent;
    if (!name?.trim()) return;
    // Il title nativo rimane disponibile senza JavaScript; evitiamo due suggerimenti.
    if (control.hasAttribute('title')) {
      control.dataset.functionName = control.title;
      control.removeAttribute('title');
    }
    current = control;
    tooltip.textContent = name.trim().replace(/\s+/g, ' ');
    control.setAttribute('aria-describedby', [control.getAttribute('aria-describedby'), tooltip.id].filter(Boolean).join(' '));
    tooltip.hidden = false;
    positionTip();
    if (touch) timer = setTimeout(hideTip, 1800);
  }
  function positionTip() {
    if (!current || tooltip.hidden) return;
    const rect = current.getBoundingClientRect(), tip = tooltip.getBoundingClientRect();
    let top = rect.top > tip.height + 12 ? rect.top - tip.height - 8 : rect.bottom + 8;
    const header = current.closest('.site-header,.topbar');
    if (header) {
      top = header.getBoundingClientRect().bottom + 8;
      header.querySelectorAll('details[open]>.lang-menu,details[open]>.theme-options,details[open]>.string-lang-menu').forEach(menu => {
        top = Math.max(top, menu.getBoundingClientRect().bottom + 8);
      });
    }
    tooltip.style.left = Math.max(8, Math.min(innerWidth - tip.width - 8, rect.left + (rect.width - tip.width) / 2)) + 'px';
    tooltip.style.top = Math.max(8, Math.min(innerHeight - tip.height - 8, top)) + 'px';
  }
  // Dopo l’apertura nativa dei menu, il suggerimento si dispone sotto le opzioni.
  document.addEventListener('click', () => { if (current) requestAnimationFrame(positionTip); });
  document.addEventListener('pointerover', event => {
    if (event.pointerType === 'touch') return;
    if (tooltip.contains(event.target)) { clearTimeout(leaveTimer); return; }
    const control = controlAt(event.target);
    if (control && control !== current) showTip(control);
  });
  document.addEventListener('pointerout', event => {
    if (!current || event.pointerType === 'touch') return;
    if (current.contains(event.relatedTarget) || tooltip.contains(event.relatedTarget)) return;
    clearTimeout(leaveTimer);
    leaveTimer = setTimeout(hideTip, 120);
  });
  document.addEventListener('pointerdown', event => {
    const control = controlAt(event.target);
    if (control && event.pointerType === 'touch') showTip(control, true);
    else if (!control && !tooltip.contains(event.target)) hideTip();
  });
  document.addEventListener('focusin', event => {
    const control = controlAt(event.target);
    if (control?.matches(':focus-visible')) showTip(control);
  });
  document.addEventListener('focusout', event => {
    if (event.target === current) hideTip();
  });
  document.addEventListener('keydown', event => { if (event.key === 'Escape') hideTip(); });
  document.addEventListener('scroll', hideTip, {capture:true, passive:true});
  window.addEventListener('resize', hideTip);
})();
