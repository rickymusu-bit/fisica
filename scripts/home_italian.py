"""Applica alla sola home italiana i comandi del catalogo e dei download."""
from html import escape, unescape
import re
from urllib.parse import unquote


def render_italian(document, root):
    document, count = re.subn(
        r'      <details class="header-menu" id="home-index">[\s\S]*?</details>\n',
        '', document, count=1)
    if count != 1:
        raise ValueError("Menu indice italiano assente o duplicato")
    document = document.replace('name="version" content="v4"', 'name="version" content="v7"')
    document = document.replace(
        'scegli «Scarica HTML»', 'usa l’icona di download')
    document = document.replace('<a class="jump" href="#indice">',
        '<a class="jump" href="#indice" aria-controls="indice" aria-expanded="false">')
    document = document.replace('<div class="catalogue" id="indice">',
        '<div class="catalogue" id="indice" hidden tabindex="-1">')
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
                f'<span class="file-size">{escape(label)}</span></a>')

    document, count = re.subn(r'<a( class="download"[^>]+)>Scarica HTML</a>', download, document)
    if count == 0:
        raise ValueError("Nessun download nella home italiana")
    document = document.replace('</style>', '''
/* Comandi della sola home italiana. */
.top{justify-content:flex-end}
.catalogue[hidden]{display:none}
.material .download{gap:10px;font-variant-numeric:tabular-nums}
.download svg{flex-shrink:0}
</style>''', 1)
    document = document.replace('</head>',
        '<noscript><style>.catalogue[hidden]{display:block}</style></noscript>\n</head>')
    script = '''
<script>
(() => {
  const catalogue = document.getElementById('indice');
  const explore = document.querySelector('.jump');
  function reveal(target, focus) {
    catalogue.hidden = false;
    explore.setAttribute('aria-expanded', 'true');
    if (focus) {
      target.tabIndex = -1;
      target.focus({preventScroll:true});
    }
    target.scrollIntoView({block:'start'});
  }
  function fromHash() {
    let id;
    try { id = decodeURIComponent(location.hash.slice(1)); } catch { return; }
    const target = document.getElementById(id);
    if (target && catalogue.contains(target)) reveal(target, false);
  }
  document.querySelectorAll('a[href="#indice"]').forEach(link => {
    link.addEventListener('click', () => reveal(catalogue, true));
  });
  window.addEventListener('hashchange', fromHash);
  fromHash();
})();
</script>
'''
    return document.replace('</body>', script + '</body>')
