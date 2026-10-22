"""Confronta le pagine ufficiali con la build verificata dopo il deployment."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import hashlib
import json
import subprocess
import sys

WORK = Path(__file__).resolve().parent
ROOT = WORK.parents[1]
BASE = 'https://rickymusu-bit.github.io/fisica/'


def main():
    release = sys.argv[1]
    names = ['index.html', 'articoli.html', 'grandezze_fisiche_sistema_internazionale_it.html',
             'metodo_scientifico_it.html', 'termodinamica_sistemi_it.html', 'crediti.html']
    def check(name):
        result = subprocess.run(['curl', '-fsSL', '--max-time', '45', BASE + name + '?release=' + release], capture_output=True)
        assert result.returncode == 0, (name, result.returncode, result.stderr.decode())
        expected = (ROOT / '_site' / name).read_bytes()
        assert result.stdout == expected, (name, 'La pagina pubblica differisce dalla build verificata')
        return {'file': name, 'bytes': len(result.stdout), 'sha256': hashlib.sha256(result.stdout).hexdigest(), 'build_identical': True}
    with ThreadPoolExecutor(max_workers=3) as pool:
        pages = list(pool.map(check, names))
    publication = json.loads((ROOT / 'pubblicazione.json').read_text())
    exclusions = []
    for name in publication['esclusi_da_pubblicazione_e_aggiornamenti'] + publication['indirizzi_storici_dismessi']:
        result = subprocess.run(['curl', '-sSL', '--max-time', '30', '-o', '/dev/null', '-w', '%{http_code}', BASE + name + '?release=' + release], capture_output=True, text=True)
        assert result.returncode == 0 and result.stdout == '404', (name, result.stdout)
        exclusions.append({'file': name, 'status': 404})
    report = {'release': release, 'pages': pages, 'excluded_urls': exclusions}
    (WORK / 'verifiche-online.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
