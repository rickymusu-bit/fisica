"""Recupera soltanto le immagini già scelte, conservando i byte originali."""
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import quote
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from PIL import Image

HERE = Path(__file__).resolve().parent
COMMONS = 'https://commons.wikimedia.org/w/api.php?'
FILES = [
 ('copertina-sydney.jpg', 'SHB-Red-Dust.jpg', 'https://thumb.wikimedia.org/wikipedia/commons/thumb/1/19/SHB-Red-Dust.jpg/960px-SHB-Red-Dust.jpg'),
 ('giunto-ponte.jpg', 'Nishi-ōhashi Bridge the expansion joint of the NE end Nakasu 4-chōme Hakata-ku Fukuoka 20231219.jpg', 'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/72/Nishi-%C5%8Dhashi_Bridge_the_expansion_joint_of_the_NE_end_Nakasu_4-ch%C5%8Dme_Hakata-ku_Fukuoka_20231219.jpg/960px-Nishi-%C5%8Dhashi_Bridge_the_expansion_joint_of_the_NE_end_Nakasu_4-ch%C5%8Dme_Hakata-ku_Fukuoka_20231219.jpg'),
 ('giunto-ferrovia.jpg', 'Expansion joint, Hayle.jpg', 'https://upload.wikimedia.org/wikipedia/commons/a/a6/Expansion_joint%2C_Hayle.jpg'),
 ('termometro.jpg', 'Mercury Thermometer.jpg', 'https://thumb.wikimedia.org/wikipedia/commons/thumb/5/57/Mercury_Thermometer.jpg/960px-Mercury_Thermometer.jpg'),
 ('conserve.jpg', 'PreservedFood1.jpg', 'https://thumb.wikimedia.org/wikipedia/commons/thumb/7/7e/PreservedFood1.jpg/960px-PreservedFood1.jpg'),
 ('lago-louise.jpg', 'A frozen Lake Louise - Banff - panoramio.jpg', None),
 ('lamina-bimetallica.svg', 'Bimetallic strip.svg', None),
 ('termostato.jpg', 'WPThermostat new.jpg', None),
 ('danni-gelo.jpg', None, 'https://i.redd.it/2jq40fxtax801.jpg'),
]

def get(url):
    with urlopen(Request(url, headers={'User-Agent':'FisicaMaterials/1.0 (educational project; source attribution retained)'}), timeout=60) as response:
        return response.read()

def fetch(record):
    filename, title, url = record
    info = None
    if title:
        api = COMMONS + 'action=query&format=json&prop=imageinfo&iiprop=url%7Cextmetadata%7Csize&iiurlwidth=960&titles=' + quote('File:'+title)
        response = json.loads(get(api))
        info = next(iter(response['query']['pages'].values()))['imageinfo'][0]
        if url is None:
            url = info.get('thumburl', info['url']) if filename == 'lago-louise.jpg' else info['url']
    try:
        raw = get(url)
    except Exception:
        # Wikimedia may refuse a thumbnail wider than the source; same chosen photo.
        if filename != 'termometro.jpg' or not info:
            raise
        url = info['url']
        raw = get(url)
    target = HERE / filename
    target.write_bytes(raw)
    meta = {'file':filename,'url':url,'source_title':title,'bytes':len(raw),
            'sha256':hashlib.sha256(raw).hexdigest(),'commons':info}
    if filename.endswith('.jpg'):
        image = Image.open(target)
        image.load()
        meta['dimensions'] = image.size
    return meta

if __name__ == '__main__':
    results = []
    with ThreadPoolExecutor(max_workers=5) as pool:
        for record, result in zip(FILES, pool.map(fetch, FILES)):
            results.append(result)
            print(result['file'], result['bytes'], result.get('dimensions'), flush=True)
    (HERE/'originali.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
