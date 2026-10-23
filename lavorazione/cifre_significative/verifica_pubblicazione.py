from pathlib import Path
import concurrent.futures, hashlib, json, urllib.request, urllib.error
root=Path(__file__).resolve().parents[2];manifest=json.loads((root/'pubblicazione.json').read_text());base='https://rickymusu-bit.github.io/fisica/'
names=manifest['articoli']+['index.html','articoli.html','quiz.html','crediti.html']
excluded=manifest['esclusi_da_pubblicazione_e_aggiornamenti']+manifest['indirizzi_storici_dismessi']+['anteprima-bordi-stringhe.html','modello-dispense.html','lavorazione/prefissi_sistema_internazionale/bozza.html','lavorazione/cifre_significative/bozza.html']
def check(item):
 name,expected=item;req=urllib.request.Request(base+name,headers={'User-Agent':'StringhePublicationVerification/1.0','Cache-Control':'no-cache'})
 try:
  with urllib.request.urlopen(req,timeout=60) as response: data=response.read();status=response.status
 except urllib.error.HTTPError as error: status=error.code;data=b''
 result={'file':name,'status':status,'expected':expected}
 if expected==200:
  result['sha256']=hashlib.sha256(data).hexdigest();result['identico_alla_build']=data==(root/'_site'/name).read_bytes()
 result['ok']=status==expected and (expected!=200 or result['identico_alla_build'])
 return result
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool: results=list(pool.map(check,[(n,200) for n in names]+[(n,404) for n in excluded]))
report={'base':base,'risultati':results,'ok':all(x['ok'] for x in results)}
(root/'lavorazione/cifre_significative/verifica-pubblicazione-online.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(report,indent=2,ensure_ascii=False))
if not report['ok']:raise SystemExit(1)
