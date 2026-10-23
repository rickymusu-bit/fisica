/* Modello didattico condiviso: nessun accesso alla rete. */
(function (global) {
  'use strict';
  const masses = [10, 20, 50, 100, 200];
  const options = {capacity: [200, 500, 1000], step: [1, 20, 50], response: [0.5, 1, 2], sensitivity: [1, 2, 5]};
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
  const signed = number => (number > 0 ? '+' : '') + format(number);
  const api = {masses, options, defaults, labConfig, quantize, signal, reading, statistics, randomDisturbance, parseNumber, closeTo};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  global.MeasurementModel = api;
  if (typeof document === 'undefined') return;

  function mount(root) {
    const mode = root.dataset.measurement;
    const lab = mode === 'lab';
    const find = name => root.querySelector('[data-' + name + ']');
    const all = name => [...root.querySelectorAll('[data-' + name + ']')];
    let config = {...(lab ? labConfig : defaults)};
    let selected = new Set(), sample = 'A', current = 0, currentSignal = 0, stable = false;
    let rows = [], series = {A: [], B: []}, configuration = 1, timer = 0, frame = 0, generation = 0, acquisition = 0, recorded = false, recordedEarly = false;
    const known = 100;
    // Il valore B appartiene al modello; non viene trasferito al DOM o al grafico.
    const unknown = 125;
    const display = find('display'), status = find('status'), record = find('record');
    const reduceMotion = global.matchMedia && global.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function cancel() { generation++; clearTimeout(timer); cancelAnimationFrame(frame); }
    function mass() { return lab ? (sample === 'A' ? known : unknown) : [...selected].reduce((a, b) => a + b, 0); }
    function updateReading(value, rawSignal) {
      current = value; currentSignal = rawSignal;
      display.textContent = value === null ? 'Fuori scala' : format(value) + ' g';
      display.dataset.value = value === null ? 'overload' : String(value);
      if (!lab) find('signal').textContent = format(rawSignal) + ' mV';
    }
    function canRecord() {
      const count = lab ? series[sample].length : rows.filter(r => r.configuration === configuration).length;
      const duplicate = recorded && (lab || !stable || !recordedEarly);
      record.disabled = current === null || duplicate || count >= (lab ? 10 : 20) || (lab && (!stable || acquisition === 0));
      if (lab) find('measure').disabled = count >= 10;
      if (count >= (lab ? 10 : 20)) status.textContent = lab ? 'Raggiunte dieci letture per questo campione. Puoi confrontare i risultati, cambiare campione o cancellare la serie.' : 'Raggiunte venti letture per questa configurazione. Cambia una proprietà o cancella la serie per continuare.';
      if (!lab && !selected.size) record.disabled = true;
    }
    function acquire() {
      cancel(); const token = generation; acquisition++; recorded = false; recordedEarly = false; stable = false;
      const m = mass();
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
        [row.configuration, format(row.mass) + ' g', format(row.value) + ' g', row.stable ? 'Stabilizzata' : 'Anticipata',
          'P ' + row.config.capacity + ' g; q ' + row.config.step + ' g; risposta ' + format(row.config.response) + ' s; S ' + row.config.sensitivity + ' mV/g; zero ' + signed(row.config.offset) + ' g; disturbo ±' + row.config.noise + ' g']
          .forEach(v => tr.append(cell(String(v)))); body.append(tr);
      } else for (const key of ['A', 'B']) series[key].forEach((value, index) => {
        const tr = document.createElement('tr');
        [key === 'A' ? 'A, riferimento 100 g' : 'B, massa ignota', index + 1, format(value) + ' g'].forEach(v => tr.append(cell(String(v))));
        body.append(tr);
      });
      if (!body.children.length) { const tr = document.createElement('tr'); const td = cell('Nessuna lettura registrata.'); td.colSpan = lab ? 3 : 5; tr.append(td); body.append(tr); }
    }
    function clearAnswers() {
      all('answer').forEach(input => input.value = '');
      if (lab) {
        find('feedback').textContent = ''; find('results').hidden = true;
        all('only-reference').forEach(el => el.hidden = sample !== 'A');
        all('only-unknown').forEach(el => el.hidden = sample !== 'B');
        find('sample-label').textContent = sample === 'A' ? 'Campione A: riferimento 100 g' : 'Campione B: massa ignota';
      }
    }
    record.addEventListener('click', () => {
      if (record.disabled) return;
      recorded = true;
      recordedEarly = !stable;
      if (lab) { series[sample].push(current); clearAnswers(); renderChart(); }
      else rows.push({configuration, mass: mass(), value: current, stable, config: {...config}});
      renderRows();
      status.textContent = 'Lettura registrata: ' + format(current) + ' g. ' + (lab ? 'Rimuovi e ripeti per una nuova misura.' : 'Puoi modificare il carico o una proprietà.');
      canRecord();
    });
    function reset() {
      cancel(); selected.clear(); sample = 'A'; currentSignal = 0; stable = false; acquisition = 0; recorded = false; recordedEarly = false;
      rows = []; series = {A: [], B: []}; configuration = 1; config = {...(lab ? labConfig : defaults)};
      updateReading(0, 0); status.textContent = lab ? 'Scegli il campione e avvia una misura.' : 'Aggiungi un pesetto al piatto.';
      if (lab) { find('sample').value = 'A'; clearAnswers(); renderChart(); }
      else {
        all('weight').forEach(btn => btn.setAttribute('aria-pressed', 'false'));
        all('property').forEach(input => {
          const key = input.dataset.property;
          input.value = options[key] ? options[key].indexOf(config[key]) : config[key]; updateSlider(input);
        });
        find('loaded-mass').textContent = '0 g'; find('series-label').textContent = 'Configurazione 1';
      }
      renderRows(); canRecord();
    }
    find('reset').addEventListener('click', reset);
    find('clear').addEventListener('click', () => {
      if (lab) { series[sample] = []; clearAnswers(); renderChart(); }
      else rows = rows.filter(row => row.configuration !== configuration);
      renderRows(); canRecord(); status.textContent = 'Letture della serie corrente cancellate.';
    });
    function updateSlider(input) {
      const key = input.dataset.property, value = options[key] ? options[key][Number(input.value)] : Number(input.value);
      config[key] = value;
      const unit = {capacity:'g', step:'g', response:'s', sensitivity:'mV/g', offset:'g', noise:'g'}[key];
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
        find('series-label').textContent = 'Configurazione ' + configuration;
        acquire();
      }));
      find('empty').addEventListener('click', () => {
        selected.clear(); all('weight').forEach(b => b.setAttribute('aria-pressed', 'false')); acquire();
      });
    } else {
      find('measure').addEventListener('click', acquire);
      find('sample').addEventListener('change', event => {
        cancel(); sample = event.target.value; acquisition = 0; stable = false; recorded = false;
        updateReading(0, 0); clearAnswers(); canRecord();
        status.textContent = 'Campione selezionato. Avvia una nuova misura; le due serie restano separate.';
      });
      function results() {
        const stats = statistics(series[sample], config.step, sample === 'A' ? known : null);
        if (!stats || stats.count < 5) { find('feedback').textContent = 'Registra almeno cinque letture della serie scelta.'; return null; }
        return stats;
      }
      find('check').addEventListener('click', () => {
        const stats = results(); if (!stats) return;
        const required = sample === 'A' ? ['mean', 'error'] : ['mean', 'dispersion', 'uncertainty'];
        const wrong = required.filter(key => !closeTo(parseNumber(root.querySelector('[data-answer="' + key + '"]').value), stats[key]));
        find('feedback').textContent = wrong.length ? 'Ricontrolla: ' + wrong.map(k => ({mean:'media',error:'errore con segno',dispersion:'semidispersione',uncertainty:'incertezza didattica'})[k]).join(', ') + '. Usa tutti i dati senza arrotondamenti intermedi; nella risposta sono ammessi due decimali.' : 'Calcoli corretti. Confronta ora i risultati con i punti nel grafico.';
        if (!wrong.length) showResults(stats);
      });
      function showResults(stats) {
        const out = find('results'); out.hidden = false;
        let text = 'Media ' + format(stats.mean) + ' g; semidispersione ' + format(stats.dispersion) + ' g. ';
        text += sample === 'A' ? 'Errore del valore medio ' + signed(stats.error) + ' g; valore assoluto ' + format(Math.abs(stats.error)) + ' g; errore percentuale ' + format(stats.relative * 100) + '%.' :
          'Stima didattica: m = (' + decimal(stats.mean) + ' ± ' + decimal(stats.uncertainty) + ') g. Il riferimento della massa ignota non è disponibile.';
        out.textContent = text;
      }
      find('solution').addEventListener('click', () => { const stats = results(); if (stats) { showResults(stats); find('feedback').textContent = 'Confronto mostrato su richiesta. La fascia rappresenta la stima scolastica, non una garanzia sul valore della massa.'; } });
    }

    function renderChart() {
      const host = find('chart'); if (!host) return;
      const ns = 'http://www.w3.org/2000/svg';
      const svg = document.createElementNS(ns, 'svg');
      svg.setAttribute('viewBox', '0 0 800 440'); svg.setAttribute('role', 'img');
      svg.setAttribute('aria-labelledby', 'misure-chart-title misure-chart-desc');
      const el = (name, attrs, text) => { const node = document.createElementNS(ns, name); for (const [k,v] of Object.entries(attrs)) node.setAttribute(k,String(v)); if (text !== undefined) node.textContent = text; svg.append(node); return node; };
      el('title', {id:'misure-chart-title'}, 'Distribuzione delle letture di massa, serie A e B');
      let description = 'Ogni punto è una lettura; i punti coincidenti sono impilati. Asse orizzontale in grammi. ';
      const left = 65, right = 750, x = v => left + (v - 90) / 50 * (right-left);
      for (let tick = 90; tick <= 140; tick += 5) {
        el('line',{x1:x(tick),x2:x(tick),y1:58,y2:365,class:'plot-grid'});
        el('text',{x:x(tick),y:394,'text-anchor':'middle',class:'plot-tick'},String(tick));
      }
      el('text',{x:410,y:426,'text-anchor':'middle',class:'plot-label'},'Massa indicata (g)');
      for (const [key,y] of [['A',165],['B',345]]) {
        const values = series[key], stats = statistics(values, config.step, key === 'A' ? known : null);
        el('text',{x:65,y:y-120,class:'plot-label'},key === 'A' ? 'A — massa nota, riferimento 100 g' : 'B — massa ignota');
        el('line',{x1:left,x2:right,y1:y,y2:y,class:'plot-axis'});
        if (key === 'A') {
          el('line',{x1:x(known),x2:x(known),y1:y-92,y2:y+12,class:'plot-reference'});
          el('text',{x:x(known)-8,y:y-83,'text-anchor':'end',class:'plot-tick'},'Riferimento');
        }
        if (!stats) { el('text',{x:475,y:y-55,'text-anchor':'middle',class:'plot-muted'},'Nessuna lettura'); description += key + ': nessuna lettura. '; continue; }
        if (key === 'B') {
          el('rect',{x:x(stats.mean-stats.uncertainty),y:y-110,width:x(stats.mean+stats.uncertainty)-x(stats.mean-stats.uncertainty),height:110,class:'plot-band'});
          for (const edge of [stats.min, stats.max]) el('line',{x1:x(edge),x2:x(edge),y1:y-7,y2:y+9,class:'plot-extreme'});
          el('text',{x:65,y:y-93,class:'plot-tick'},'d = ' + format(stats.dispersion) + ' g; U = ' + format(stats.uncertainty) + ' g');
          el('text',{x:65,y:y-70,class:'plot-tick'},'Fascia ' + format(stats.mean-stats.uncertainty) + '–' + format(stats.mean+stats.uncertainty) + ' g');
        }
        const stacks = new Map();
        for (const value of values) {
          const stack = (stacks.get(value) || 0) + 1; stacks.set(value,stack);
          const point = el('circle',{cx:x(value),cy:y-12-(stack-1)*11,r:4,class:'plot-point plot-'+key.toLowerCase()});
          const title = document.createElementNS(ns,'title'); title.textContent = 'Serie ' + key + ': ' + format(value) + ' g'; point.append(title);
        }
        el('line',{x1:x(stats.mean),x2:x(stats.mean),y1:y-85,y2:y+12,class:'plot-mean'});
        el('text',{x:key === 'A' ? 475 : 65,y:y-45,class:'plot-tick'},'Media ' + format(stats.mean) + ' g');
        if (key === 'A') {
          el('line',{x1:x(known),x2:x(stats.mean),y1:y-102,y2:y-102,class:'plot-error'});
          for (const value of [known,stats.mean]) el('line',{x1:x(value),x2:x(value),y1:y-106,y2:y-98,class:'plot-error'});
          el('text',{x:475,y:y-83,class:'plot-tick'},'Errore della media ' + signed(stats.error) + ' g');
        }
        description += key + ': ' + values.length + ' letture, media ' + format(stats.mean) + ' g; ' + (key === 'A' ? 'riferimento 100 g, errore ' + signed(stats.error) + ' g. ' : 'semidispersione ' + format(stats.dispersion) + ' g e incertezza didattica ' + format(stats.uncertainty) + ' g. ');
      }
      const desc = document.createElementNS(ns,'desc'); desc.id = 'misure-chart-desc'; desc.textContent = description; svg.prepend(desc);
      host.replaceChildren(svg); find('chart-description').textContent = description;
      const zoom = find('chart-copy');
      if (zoom) {
        const copy = svg.cloneNode(true);
        copy.querySelector('title').id = 'misure-chart-title-zoom';
        copy.querySelector('desc').id = 'misure-chart-desc-zoom';
        copy.setAttribute('aria-labelledby','misure-chart-title-zoom misure-chart-desc-zoom');
        zoom.replaceChildren(copy);
      }
    }
    root.classList.add('sim-ready'); all('interactive').forEach(el => el.disabled = false); reset();
  }
  document.querySelectorAll('[data-measurement]').forEach(mount);
})(typeof globalThis !== 'undefined' ? globalThis : this);
