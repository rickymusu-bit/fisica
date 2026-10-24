(()=>{
'use strict';
document.documentElement.classList.add('js-enabled');
const fmt=n=>new Intl.NumberFormat('it-IT',{maximumFractionDigits:2}).format(Object.is(n,-0)?0:n);
for(const button of document.querySelectorAll('[data-toggle]')){
 button.addEventListener('click',()=>{
  const frame=document.getElementById(button.dataset.toggle),show=frame.classList.toggle('show-fit');
  button.setAttribute('aria-pressed',String(show));button.textContent=(show?'Nascondi la ':'Mostra la ')+button.dataset.kind;
 });
}
for(const figure of document.querySelectorAll('[data-model]')){
 const model=figure.dataset.model,initial=Number(figure.dataset.initial),unit=figure.dataset.unit,probe=Number(figure.dataset.probe);
 const input=figure.querySelector('[data-k]'),svg=figure.querySelector('svg'),frame=figure.querySelector('.image-frame'),button=figure.querySelector('[data-toggle]');
 const xmax=Number(svg.dataset.xmax),ymax=Number(svg.dataset.ymax),X=x=>50+325*x/xmax,Y=y=>245-215*y/ymax;
 const value=(k,x)=>model==='direct'?k*x:model==='inverse'?k/x:k*x*x;
 const curve=figure.querySelector('[data-curve]'),reference=figure.querySelector('[data-reference]');
 const table=document.querySelector('[data-model-table="'+model+'"]');
 const points=[...figure.querySelectorAll('[data-point-x]')];
 const probeDot=document.createElementNS('http://www.w3.org/2000/svg','circle');probeDot.setAttribute('class','probe fit');probeDot.setAttribute('r','6');svg.append(probeDot);
 function update(reveal){
  const k=Number(input.value);
  const samples=[];
  // Evita la singolarità e campiona solo la porzione visibile, senza valori infiniti.
  const min=model==='inverse'?k/ymax:0;
  for(let i=0;i<=400;i++){const x=min+(xmax-min)*i/400;samples.push(X(x).toFixed(3)+','+Y(value(k,x)).toFixed(3));}
  curve.setAttribute('points',samples.join(' '));
  reference.hidden=k===initial;
  if(k===initial)reference.setAttribute('hidden','');else reference.removeAttribute('hidden');
  for(const point of points){const x=Number(point.dataset.pointX);point.setAttribute('cy',Y(value(k,x)));}
  if(table)for(const row of table.tBodies[0].rows){const x=Number(row.cells[0].textContent.replace(',','.'));row.cells[1].textContent=fmt(value(k,x));}
  probeDot.setAttribute('cx',X(probe));probeDot.setAttribute('cy',Y(value(k,probe)));
  figure.querySelector('[data-k-value]').textContent=fmt(k)+(unit?' '+unit:'');
  input.setAttribute('aria-valuetext',fmt(k)+(unit?' '+unit:''));
  const result=value(k,probe);
  const reading=model==='direct'?`Con ${fmt(probe)} libri: ${fmt(result)} €.`:model==='inverse'?`A ${fmt(probe)} km/h: ${fmt(result)} h.`:`A x = ${fmt(probe)}: y = ${fmt(result)}.`;
  figure.querySelector('[data-model-reading]').textContent=reading+(k!==initial?` Tratteggio: k = ${fmt(initial)}${unit?' '+unit:''}.`:'');
  svg.setAttribute('aria-label',`Grafico ${model==='direct'?'della proporzionalità diretta':model==='inverse'?'della proporzionalità inversa':'della proporzionalità quadratica'}, k = ${fmt(k)} ${unit}. ${reading}`);
  figure.dataset.currentK=String(k);
  if(reveal){frame.classList.add('show-fit');button.setAttribute('aria-pressed','true');button.textContent='Nascondi la '+button.dataset.kind;}
 }
 input.disabled=false;input.addEventListener('input',()=>update(true));update(false);
}
const svg=document.getElementById('plane');
if(!svg)return;
const point=document.getElementById('point'),hit=document.getElementById('hit-point'),gx=document.getElementById('x-guide'),gy=document.getElementById('y-guide'),readout=document.getElementById('coordinate-readout');
let x=2,y=2,dragging=false;
const clamp=n=>Math.max(-5,Math.min(5,n)),round=n=>Math.round(n*10)/10;
function location(){if(x===0&&y===0)return 'origine';if(x===0)return 'asse y';if(y===0)return 'asse x';return (x>0?(y>0?'I':'IV'):(y>0?'II':'III'))+' quadrante';}
function set(nx,ny){
 x=round(clamp(nx));y=round(clamp(ny));const X=160+24*x,Y=160-24*y;
 for(const c of [point,hit]){c.setAttribute('cx',X);c.setAttribute('cy',Y);}
 gx.setAttribute('d',`M${X} ${Y}V160`);gy.setAttribute('d',`M160 ${Y}H${X}`);
 readout.textContent=`P = (${fmt(x)}; ${fmt(y)}); ${location()}`;
 point.setAttribute('aria-label',`Punto P, coordinate ${fmt(x)} e ${fmt(y)}; ${location()}. Usa le frecce per spostarlo.`);
 svg.setAttribute('aria-label',`Piano cartesiano. P = (${fmt(x)}; ${fmt(y)}); ${location()}.`);
}
function fromPointer(e){const p=svg.createSVGPoint();p.x=e.clientX;p.y=e.clientY;const q=p.matrixTransform(svg.getScreenCTM().inverse());set((q.x-160)/24,(160-q.y)/24);}
for(const target of [point,hit]){
 target.addEventListener('pointerdown',e=>{dragging=true;target.setPointerCapture(e.pointerId);fromPointer(e);e.preventDefault();});
 target.addEventListener('pointermove',e=>{if(dragging)fromPointer(e);});
 target.addEventListener('pointerup',()=>dragging=false);target.addEventListener('pointercancel',()=>dragging=false);
}
point.addEventListener('keydown',e=>{const s=e.shiftKey ? 0.1 : 0.5;let dx=0,dy=0;if(e.key==='ArrowLeft')dx=-s;else if(e.key==='ArrowRight')dx=s;else if(e.key==='ArrowUp')dy=s;else if(e.key==='ArrowDown')dy=-s;else return;e.preventDefault();set(x+dx,y+dy);});
set(2,2);
})();
