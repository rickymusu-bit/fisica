"""Applica alla sola home italiana i comandi del catalogo e dei download."""
from html import escape, unescape
import re
from urllib.parse import unquote


def render_italian(document, root):
    article_count = len(re.findall(r'<a class="read"', document))
    document, count = re.subn(
        r'      <details class="header-menu" id="home-index">[\s\S]*?</details>\n',
        '', document, count=1)
    if count != 1:
        raise ValueError("Menu indice italiano assente o duplicato")
    document = document.replace('name="version" content="v11"', 'name="version" content="v18"')
    document = document.replace(
        'scegli «Scarica HTML»', 'usa l’icona di download')
    document = re.sub(r'        <div class="intro-foot">[\s\S]*?</div>\n', '', document, count=1)
    document = document.replace('<header class="top">', '''<header class="top">
      <button class="articles-trigger" type="button" aria-haspopup="dialog" aria-controls="articles-panel" aria-expanded="false"><span aria-hidden="true">☰</span> Articoli</button>''')
    document = document.replace('<div class="catalogue" id="indice">',
        f'''<dialog id="articles-panel" aria-labelledby="articles-title">
        <div class="panel-heading"><h2 id="articles-title">Articoli <span>{article_count} articoli</span></h2><button class="panel-close" type="button" aria-label="Chiudi gli articoli" autofocus>×</button></div>
        <div class="catalogue" id="indice" tabindex="-1">''')
    document = document.replace('      </div>\n    </main>', '      </div>\n      </dialog>\n    </main>', 1)
    # Un unico originale SVG per il file riutilizzabile e la home autonoma.
    logo = (root / 'identita' / 'logo-materia-oscura.svg').read_text(encoding='utf-8')
    logo = logo.replace('<svg ', '<svg id="site-logo" class="site-logo" aria-hidden="true" focusable="false" ', 1)
    document, logo_count = re.subn(r'<img id="site-logo"[^>]+>', lambda _: logo, document)
    if logo_count != 1:
        raise ValueError("Segnaposto del logo assente o duplicato")

    # La scelta della lingua resta una normale visita alla relativa home.
    document = document.replace('href="./#indice"', 'href="./"')

    def download(match):
        attrs = match[1]
        filename = unquote(unescape(re.search(r'href="([^"]+)"', attrs)[1]))
        path = (root / filename).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            raise ValueError(f"Download non valido: {filename}")
        size = path.stat().st_size
        label = (f'{size / 1_000_000:.2f} MB' if size >= 1_000_000
                 else f'{size / 1_000:.2f} kB').replace('.', ',')
        exact = f'{size:,}'.replace(',', '.') + ' byte'
        attrs = re.sub(r'aria-label="([^"]+)"',
                       lambda m: 'aria-label="' + m[1] + ' — ' + exact + '"', attrs)
        return (f'<a{attrs} title="HTML · {exact}">'
                '<svg aria-hidden="true" viewBox="0 0 24 24" width="22" height="22" '
                'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
                'stroke-linejoin="round"><path d="M12 3v12m-5-5 5 5 5-5M4 16v5h16v-5"/></svg>'
                f'<span>Scarica</span><span class="file-size">{escape(label)}</span></a>')

    document, count = re.subn(r'<a( class="download"[^>]+)>Scarica(?: HTML)?</a>', download, document)
    if count == 0:
        raise ValueError("Nessun download nella home italiana")
    # La revisione nel collegamento evita il riuso di una copia precedente in cache.
    def current_article(match):
        attrs = match[0]
        filename = unquote(unescape(re.search(r'href="([^"?]+)"', attrs)[1]))
        source = (root / filename).read_text(encoding='utf-8')
        version = re.search(r'<meta\b(?=[^>]*\bname="version")[^>]*\bcontent="v([0-9]+)"', source)
        if not version:
            raise ValueError(f"Versione articolo assente: {filename}")
        return attrs.replace(f'href="{escape(filename)}"', f'href="{escape(filename)}?v={version[1]}"', 1)

    document = re.sub(r'<a class="(?:read|download)"[^>]*>', current_article, document)
    document = document.replace('</style>', '''
/* Comandi della sola home italiana. */
.top{justify-content:space-between}
.site-heading{display:flex;align-items:center;gap:18px;margin-bottom:30px}
.site-heading h1{margin:0;min-width:0}
.logo-toggle{display:block;flex:0 0 clamp(68px,7.5vw,104px);width:clamp(68px,7.5vw,104px);padding:0;border:0;background:transparent;line-height:0;cursor:pointer}
.logo-toggle:disabled{cursor:default}
.site-heading .site-logo{display:block;width:100%;height:auto;overflow:visible}
@media(max-width:600px){.site-heading{gap:12px;margin-bottom:20px}.logo-toggle{flex-basis:58px;width:58px}.site-heading h1{margin:0}}
button{font:inherit;color:inherit}
button:focus-visible{outline:3px solid var(--ink);outline-offset:5px}
.articles-trigger,.panel-close{display:inline-flex;align-items:center;justify-content:center;gap:12px;min-height:46px;border:2px solid var(--line);background:white;font-size:17px;font-weight:600;cursor:pointer;padding:8px 14px;line-height:1.4}
.articles-trigger:hover,.panel-close:hover{background:var(--ink);color:white}
#articles-panel{position:fixed;inset:0 auto 0 0;margin:0;width:min(680px,100%);max-width:100%;height:100dvh;max-height:100dvh;padding:0;border:0;border-right:3px solid var(--line);background:white;color:var(--ink);overflow:auto;overscroll-behavior:contain}
#articles-panel::backdrop{background:rgb(0 0 0 / .5)}
html:has(#articles-panel[open]){overflow:hidden}
.panel-heading{display:flex;align-items:center;justify-content:space-between;gap:16px;position:sticky;top:0;z-index:2;padding:14px 24px;background:var(--paper);border-bottom:3px solid var(--line)}
.panel-heading h2{margin:0;font-size:24px;line-height:1.4}
.panel-heading h2 span{display:block;font-size:14px;font-weight:400}
.panel-close{flex-shrink:0;width:46px;font-size:28px;padding:0}
#articles-panel .catalogue{border-top:0;padding:24px 24px 36px}
#articles-panel .group{scroll-margin-top:110px}
#articles-panel .material{grid-template-columns:minmax(0,1fr)}
#articles-panel .material .read{padding:20px 0 12px}
#articles-panel .material .download{justify-self:start;margin:0 0 20px 41px}
.material .download{gap:10px;font-variant-numeric:tabular-nums}
.download svg{flex-shrink:0}
@media(max-width:600px){#articles-panel{width:calc(100% - 16px)}.panel-heading{padding:12px 16px}#articles-panel .catalogue{padding:20px 14px 32px}#articles-panel .material .download{margin-left:32px}.articles-trigger{font-size:16px;padding:9px 12px}}
</style>''', 1)
    document = document.replace('</head>',
        '<noscript><style>#articles-panel{display:block;position:static;width:100%;height:auto;max-height:none;border:0}.panel-heading{position:static}.articles-trigger,.panel-close{display:none}</style></noscript>\n</head>')
    script = '''
<script>
(() => {
  const catalogue = document.getElementById('indice');
  const panel = document.getElementById('articles-panel');
  const trigger = document.querySelector('.articles-trigger');
  const close = panel.querySelector('.panel-close');
  function show(target) {
    if (!panel.open) panel.showModal();
    trigger.setAttribute('aria-expanded', 'true');
    if (target && target !== catalogue) target.scrollIntoView({block:'start'});
    else panel.scrollTop = 0;
  }
  trigger.addEventListener('click', () => show());
  close.addEventListener('click', () => panel.close());
  panel.addEventListener('close', () => {
    trigger.setAttribute('aria-expanded', 'false');
    trigger.focus({preventScroll:true});
  });
  panel.addEventListener('click', event => {
    const box = panel.getBoundingClientRect();
    if (event.target === panel && (event.clientX < box.left || event.clientX >= box.right || event.clientY < box.top || event.clientY >= box.bottom)) panel.close();
  });
  document.querySelectorAll('a[href="#indice"]').forEach(link => {
    link.addEventListener('click', event => { event.preventDefault(); show(catalogue); });
  });
  // Arrivo dagli articoli e ripristino della pagina: il catalogo resta chiuso.
  window.addEventListener('pageshow', () => {
    if (panel.open) panel.close();
    trigger.setAttribute('aria-expanded', 'false');
  });
})();
</script>
'''
    logo_controls = (root / 'identita' / 'controlli-logo.js').read_text(encoding='utf-8')
    return document.replace('</body>', '<script>\n' + logo_controls + '</script>\n' + script + '</body>')
