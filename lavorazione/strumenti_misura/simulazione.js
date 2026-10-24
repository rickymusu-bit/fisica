/* Modello didattico condiviso: nessun accesso alla rete. */
(function (global) {
  'use strict';
  const masses = [10, 20, 50, 100, 200];
  const options = {capacity: [200, 300, 500], step: [1, 20, 50], response: [0.5, 1, 2], sensitivity: [1, 2, 5]};
  const defaults = {capacity: 500, step: 1, response: 1, sensitivity: 1, offset: 0, noise: 0};
  const labConfig = {...defaults, noise: 3};
  function quantize(value, step) { return Number((Math.round(value / step) * step).toFixed(8)) || 0; }
  function signal(mass, config, disturbance = 0) { return (mass + config.offset + disturbance) * config.sensitivity; }
  function reading(mass, config, disturbance = 0) {
    return mass > config.capacity ? null : quantize(signal(mass, config, disturbance) / config.sensitivity, config.step);
  }
  function statistics(values, step, reference = null) {
    if (!values.length) return null;
    const mean = values.reduce((a, b) => a + b, 0) / values.length;
    const min = Math.min(...values), max = Math.max(...values), dispersion = (max - min) / 2;
    return {count: values.length, mean, min, max, dispersion, uncertainty: Math.max(step, dispersion),
      error: reference === null ? null : mean - reference,
      relative: reference === null || reference === 0 ? null : Math.abs(mean - reference) / Math.abs(reference)};
  }
  function randomDisturbance(amplitude, random = Math.random) { return amplitude * (2 * random() - 1); }
  function parseNumber(value) {
    const text = String(value).trim().replace(',', '.');
    return /^[+-]?(?:\d+(?:\.\d*)?|\.\d+)$/.test(text) ? Number(text) : NaN;
  }
  function closeTo(value, expected) { return Number.isFinite(value) && Math.abs(value - expected) <= 0.00501; }
  const format = (number, digits = 2) => Number(number).toLocaleString('it-IT', {maximumFractionDigits: digits});
  const decimal = number => Number(number).toLocaleString('it-IT', {minimumFractionDigits: 1, maximumFractionDigits: 1});
  const quality = value => ['Molto bassa','Bassa','Medio-bassa','Media','Medio-alta','Alta'][value];
  const signed = number => (number > 0 ? '+' : '') + format(number);
  const api = {masses, options, defaults, labConfig, quantize, signal, reading, statistics, randomDisturbance, parseNumber, closeTo};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  global.MeasurementModel = api;
  if (typeof document === 'undefined') return;

  function mount(root, index) {
    const mode = root.dataset.measurement;
    const lab = mode === 'lab';
    const study=root.dataset.study;
    const fixedSample=study==='uncertainty' ? 'B' : 'A';
    const chartId='misure-'+index;
    const find = name => root.querySelector('[data-' + name + ']');
    const all = name => [...root.querySelectorAll('[data-' + name + ']')];
    let config = {...(lab ? labConfig : defaults)};
    let selected = new Set(), sample = fixedSample, current = 0, currentSignal = 0, stable = false;
    let rows = [], series = {A: [], B: []}, configuration = 1, timer = 0, frame = 0, generation = 0, acquisition = 0, recorded = false, recordedEarly = false;
    const known = 100;
    // Il valore B appartiene al modello; non viene trasferito al DOM o al grafico.
    const unknown = 125;
    const display = find('display'), status = find('status'), record = find('record');
    const reduceMotion = global.matchMedia && global.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function cancel() { generation++; clearTimeout(timer); cancelAnimationFrame(frame); }
    function mass() { return lab ? (sample === 'A' ? known : unknown) : [...selected].reduce((a, b) => a + b, 0); }
    function paintLoad() {
      const pan=find('pan'),scene=root.querySelector('.sim-balance-scene');
      if (!pan || !scene) return;
      pan.replaceChildren();
      const items=lab ? (acquisition>0 ? [sample==='A' ? known : unknown] : []) : [...selected].sort((a,b)=>a-b);
      const ns='http://www.w3.org/2000/svg';
      for (const m of items) {
        const svg=document.createElementNS(ns,'svg'),use=document.createElementNS(ns,'use');
        svg.setAttribute('viewBox',scene.dataset.weightViewbox);svg.setAttribute('role','img');
        svg.setAttribute('aria-label',lab ? (sample==='A' ? 'Campione A, riferimento 100 g sul piatto' : 'Campione B sul piatto') : 'Pesetto da '+m+' g sul piatto');
        svg.classList.add('sim-pan-weight');svg.style.setProperty('--weight-size',String(Math.cbrt(m/200)));
        use.setAttribute('href','#'+scene.dataset.weightSymbol);svg.append(use);
        const item=document.createElement('span'),label=document.createElement('span');
        item.className='sim-pan-item';item.style.setProperty('--weight-size',String(Math.cbrt(m/200)));
        label.className='sim-mass-label';label.setAttribute('aria-hidden','true');
        label.textContent=lab && sample==='B' ? 'B' : m+' g';
        item.append(svg,label);pan.append(item);
      }
    }
    function updateReading(value, rawSignal) {
      current = value; currentSignal = rawSignal;
      display.textContent = value === null ? (root.classList.contains('sim-has-balance') ? 'OL' : 'Fuori scala') : format(value) + ' g';
      display.setAttribute('aria-label',value===null ? 'Fuori scala' : 'Indicazione della bilancia: '+format(value)+' g');
      display.dataset.value = value === null ? 'overload' : String(value);
    }
    function canRecord() {
      const count = lab ? series[sample].length : rows.filter(r => r.configuration === configuration).length;
      const duplicate = recorded && (lab || !stable || !recordedEarly);
      record.disabled = current === null || duplicate || count >= (lab ? 10 : 20) || (lab && (!stable || acquisition === 0));
      if (lab) find('measure').disabled = count >= 10;
      if (count >= (lab ? 10 : 20)) status.textContent = lab ? 'Raggiunte dieci letture per questo campione. Puoi confrontare i risultati, cambiare campione o cancellare la serie.' : 'Raggiunte venti letture in questa serie. Cambia una proprietà o cancella la serie per continuare.';
      if (!lab && !selected.size) record.disabled = true;
    }
    function acquire() {
      cancel(); const token = generation; acquisition++; recorded = false; recordedEarly = false; stable = false;
      const m = mass();
      paintLoad();
      if (lab) find('measure').textContent='Rimuovi e ripeti';
      if (!lab) find('loaded-mass').textContent = format(m) + ' g';
      if (m > config.capacity) {
        updateReading(null, signal(m, config)); status.textContent = 'Il carico supera la portata di ' + format(config.capacity) + ' g.';
        canRecord(); return;
      }
      const disturbance = randomDisturbance(config.noise);
      const targetSignal = signal(m, config, disturbance);
      const startSignal = lab ? 0 : currentSignal;
      const started = performance.now(), duration = config.response * 1000;
      status.textContent = 'Attendi la stabilizzazione della lettura.';
      updateReading(quantize(startSignal / config.sensitivity, config.step), startSignal); canRecord();
      function finish() {
        if (token !== generation) return;
        updateReading(reading(m, config, disturbance), targetSignal); stable = true;
        status.textContent = 'Lettura stabilizzata. Puoi registrarla.'; canRecord();
      }
      function advance(now) {
        if (token !== generation) return;
        const portion = Math.min(1, (now - started) / duration);
        const value = startSignal + (targetSignal - startSignal) * portion;
        updateReading(quantize(value / config.sensitivity, config.step), value);
        if (portion < 1) frame = requestAnimationFrame(advance);
      }
      if (!reduceMotion) frame = requestAnimationFrame(advance);
      timer = setTimeout(finish, duration);
    }
    function cell(text) { const el = document.createElement('td'); el.textContent = text; return el; }
    function renderRows() {
      const body = find('rows'); body.replaceChildren();
      if (!lab) for (const row of rows) {
        const tr = document.createElement('tr');
        [format(row.mass) + ' g', format(row.value) + ' g', row.stable ? 'Stabilizzata' : 'Anticipata',
          'P ' + row.config.capacity + ' g; risoluzione ' + row.config.step + ' g; risposta ' + format(row.config.response) + ' s; accuratezza ' + quality(5-Math.abs(row.config.offset)) + '; precisione ' + quality(5-row.config.noise)]
          .forEach(v => tr.append(cell(String(v)))); body.append(tr);
      } else for (const key of ['A', 'B']) series[key].forEach((value, index) => {
        const tr = document.createElement('tr');
        [key === 'A' ? 'A, riferimento 100 g' : 'B, massa ignota', index + 1, format(value) + ' g'].forEach(v => tr.append(cell(String(v))));
        body.append(tr);
      });
      if (!body.children.length) { const tr = document.createElement('tr'); const td = cell('Nessuna lettura registrata.'); td.colSpan = lab ? 3 : 4; tr.append(td); body.append(tr); }
    }
    function refreshStudyLabel() {
      if(lab) find('sample-label').textContent=sample==='A'?'Campione A: riferimento 100 g':'Campione B: massa ignota';
    }
    record.addEventListener('click', () => {
      if (record.disabled) return;
      recorded = true;
      recordedEarly = !stable;
      if (lab) { series[sample].push(current); refreshStudyLabel(); renderChart(); }
      else rows.push({configuration, mass: mass(), value: current, stable, config: {...config}});
      renderRows();
      status.textContent = 'Lettura registrata: ' + format(current) + ' g. ' + (lab ? 'Rimuovi e ripeti per una nuova misura.' : 'Puoi modificare il carico o una proprietà.');
      canRecord();
    });
    function reset() {
      cancel(); selected.clear(); sample = fixedSample; currentSignal = 0; stable = false; acquisition = 0; recorded = false; recordedEarly = false;
      rows = []; series = {A: [], B: []}; configuration = 1; config = {...(lab ? labConfig : defaults)};
      updateReading(0, 0); status.textContent = lab ? 'Appoggia il campione e avvia una misura.' : 'Aggiungi un pesetto al piatto.';
      if (lab) { find('measure').textContent='Appoggia e misura'; refreshStudyLabel(); renderChart(); }
      else {
        all('weight').forEach(btn => btn.setAttribute('aria-pressed', 'false'));
        all('property').forEach(input => {
          const key = input.dataset.property;
          input.value = options[key] ? options[key].indexOf(config[key]) : (['offset','noise'].includes(key) ? 5-config[key] : config[key]); updateSlider(input);
        });
        find('loaded-mass').textContent = '0 g';
      }
      renderRows(); canRecord();
      paintLoad();
    }
    find('reset').addEventListener('click', reset);
    find('clear').addEventListener('click', () => {
      if (lab) { series[sample] = []; refreshStudyLabel(); renderChart(); }
      else rows = rows.filter(row => row.configuration !== configuration);
      renderRows(); canRecord(); status.textContent = 'Letture della serie corrente cancellate.';
    });
    function updateSlider(input) {
      const key = input.dataset.property, value = options[key] ? options[key][Number(input.value)] : Number(input.value);
      if (['offset','noise'].includes(key)) {
        config[key] = 5-value;
        root.querySelector('[data-property-output="' + key + '"]').textContent = quality(value);
        input.setAttribute('aria-valuetext',quality(value));return;
      }
      config[key] = value;
      const unit = {capacity:'g', step:'g', response:'s', offset:'g', noise:'g'}[key];
      root.querySelector('[data-property-output="' + key + '"]').textContent = format(value) + ' ' + unit;
      input.setAttribute('aria-valuetext', format(value) + ' ' + unit);
    }
    if (!lab) {
      all('weight').forEach(btn => btn.addEventListener('click', () => {
        const m = Number(btn.dataset.weight);
        if (selected.has(m)) selected.delete(m); else selected.add(m);
        btn.setAttribute('aria-pressed', String(selected.has(m))); acquire();
      }));
      all('property').forEach(input => input.addEventListener('input', () => {
        updateSlider(input); configuration++;
        acquire();
      }));
      find('empty').addEventListener('click', () => {
        selected.clear(); all('weight').forEach(b => b.setAttribute('aria-pressed', 'false')); acquire();
      });
    } else {
      find('measure').addEventListener('click', acquire);
    }

    function renderChart() {
      const host=find('chart');if(!host)return;
      const ns='http://www.w3.org/2000/svg',svg=document.createElementNS(ns,'svg');
      const unknownStudy=sample==='B',values=series[sample],stats=statistics(values,config.step,unknownStudy?null:known);
      const chartWidth=Math.max(180,host.getBoundingClientRect().width);
      svg.setAttribute('viewBox','0 0 '+chartWidth+' 282');svg.setAttribute('role','img');
      svg.setAttribute('aria-labelledby',chartId+'-title '+chartId+'-desc');
      const el=(name,attrs,text)=>{const node=document.createElementNS(ns,name);for(const[k,v]of Object.entries(attrs))node.setAttribute(k,String(v));if(text!==undefined)node.textContent=text;svg.append(node);return node;};
      el('title',{id:chartId+'-title'},unknownStudy?'Incertezza della massa ignota':'Errore rispetto alla massa di riferimento');
      el('text',{x:16,y:24,class:'plot-label'},unknownStudy?'Massa ignota':'Riferimento 100 g');
      const bounds=stats?[stats.min,stats.max,...(unknownStudy?[stats.mean-stats.uncertainty,stats.mean+stats.uncertainty]:[known])]:[96,104];
      let low=stats?2*Math.floor((Math.min(...bounds)-1)/2):96;
      let high=stats?2*Math.ceil((Math.max(...bounds)+1)/2):104;
      while(high-low<8){low-=2;high+=2;}
      svg.dataset.axisMin=String(low);svg.dataset.axisMax=String(high);
      const left=36,right=chartWidth-16,y=220,x=v=>left+(v-low)/(high-low)*(right-left);
      for(let tick=low;tick<=high;tick+=2){
        if(unknownStudy&&!stats)break;
        el('line',{x1:x(tick),x2:x(tick),y1:96,y2:y,class:'plot-grid'});
      }
      if(stats||!unknownStudy){
        const labels=chartWidth<360?[low,(low+high)/2,high]:Array.from({length:(high-low)/2+1},(_,i)=>low+2*i);
        for(const tick of labels){el('line',{x1:x(tick),x2:x(tick),y1:y,y2:y+5,class:'plot-axis'});el('text',{x:x(tick),y:246,'text-anchor':'middle',class:'plot-tick'},String(tick));}
      }
      el('line',{x1:left,x2:right,y1:y,y2:y,class:'plot-axis'});
      el('text',{x:chartWidth/2,y:274,'text-anchor':'middle',class:'plot-label'},'Massa indicata (g)');
      if(!unknownStudy)el('line',{x1:x(known),x2:x(known),y1:96,y2:y+12,class:'plot-reference'});
      let description='Ogni punto è una lettura della massa '+(unknownStudy?'ignota. ':'nota. ');
      if(!stats){el('text',{x:chartWidth/2,y:170,'text-anchor':'middle',class:'plot-muted'},'Nessuna lettura');description+='Nessuna lettura registrata.';}
      else{
        el('text',{x:16,y:48,class:'plot-tick'},'Media '+format(stats.mean)+' g');
        if(unknownStudy){
          el('rect',{x:x(stats.mean-stats.uncertainty),y:96,width:x(stats.mean+stats.uncertainty)-x(stats.mean-stats.uncertainty),height:y-96,class:'plot-band'});
          for(const edge of[stats.min,stats.max])el('line',{x1:x(edge),x2:x(edge),y1:y-7,y2:y+9,class:'plot-extreme'});
          el('text',{x:16,y:72,class:'plot-tick'},'d = '+format(stats.dispersion)+' g; U = '+format(stats.uncertainty)+' g');
          description+='Media '+format(stats.mean)+' g; semidispersione '+format(stats.dispersion)+' g; incertezza '+format(stats.uncertainty)+' g. Fascia da '+format(stats.mean-stats.uncertainty)+' a '+format(stats.mean+stats.uncertainty)+' g.';
        }else{
          el('line',{x1:x(known),x2:x(stats.mean),y1:92,y2:92,class:'plot-error'});
          for(const value of[known,stats.mean])el('line',{x1:x(value),x2:x(value),y1:87,y2:97,class:'plot-error'});
          el('text',{x:16,y:72,class:'plot-tick'},'Errore della media '+signed(stats.error)+' g');
          description+='Riferimento 100 g; media '+format(stats.mean)+' g; errore '+signed(stats.error)+' g.';
        }
        const stacks=new Map();
        for(const value of values){const stack=(stacks.get(value)||0)+1;stacks.set(value,stack);
          const point=el('circle',{cx:x(value),cy:y-12-(stack-1)*11,r:4,class:'plot-point plot-'+sample.toLowerCase()});
          const title=document.createElementNS(ns,'title');title.textContent=format(value)+' g';point.append(title);}
        el('line',{x1:x(stats.mean),x2:x(stats.mean),y1:96,y2:y+12,class:'plot-mean'});
      }
      el('desc',{id:chartId+'-desc'},description);host.replaceChildren(svg);find('chart-description').textContent=description;
    }
    root.classList.add('sim-ready'); all('interactive').forEach(el => el.disabled = false); reset();
    if(lab){
      let lastWidth=0;
      const updateSize=()=>{const width=find('chart').getBoundingClientRect().width;if(Math.abs(width-lastWidth)>1){lastWidth=width;renderChart();}};
      if(typeof ResizeObserver!=='undefined')new ResizeObserver(updateSize).observe(find('chart'));
      else global.addEventListener('resize',updateSize);
    }
  }
  document.querySelectorAll('[data-measurement]').forEach((root,index)=>mount(root,index));
})(typeof globalThis !== 'undefined' ? globalThis : this);
