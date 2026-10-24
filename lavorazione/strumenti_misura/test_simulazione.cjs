// Casi quantitativi indipendenti dalla presentazione e dalle immagini.
const assert = require('node:assert/strict');
const {test} = require('node:test');
const m = require('./simulazione.js');
test('i pesetti hanno somma esatta e il fuori scala dipende dal carico', () => {
  const sum = m.masses.reduce((a,b)=>a+b,0);
  assert.equal(sum,380);
  assert.equal(Math.max(...m.options.capacity),500);
  assert.equal(m.reading(sum,{...m.defaults,capacity:500}),380);
  assert.equal(m.reading(sum,{...m.defaults,capacity:200}),null);
  assert.equal(m.reading(200,{...m.defaults,capacity:200}),200);
});
test('la sensibilità modifica il segnale e conserva la massa a calibrazione coerente', () => {
  for(const sensitivity of [1,2,5]) {
    const config={...m.defaults,sensitivity};
    assert.equal(m.signal(100,config),100*sensitivity);
    assert.equal(m.reading(100,config),100);
    assert.equal(m.reading(100,{...config,offset:2},-1),101);
  }
});
test('quantizzazione, zero spostato e disturbo restano contributi distinti', () => {
  assert.equal(m.reading(20,{...m.defaults,step:10},3),20);
  assert.equal(m.reading(20,{...m.defaults,step:10},6),30);
  assert.equal(m.reading(10,{...m.defaults,step:20}),20);
  assert.equal(m.reading(10,{...m.defaults,step:50}),0);
  assert.equal(m.reading(100,{...m.defaults,offset:2},0),102);
  assert.equal(m.quantize(-0.1,1),0);
  assert.equal(m.randomDisturbance(3,()=>0),-3);
  assert.equal(m.randomDisturbance(3,()=>0.5),0);
  assert.equal(m.randomDisturbance(3,()=>1),3);
});
test('dati del cronometro: media, semidispersione ed errore', () => {
  const s=m.statistics([2.31,2.37,2.40,2.43,2.49],0.01,2.50);
  assert.ok(Math.abs(s.mean-2.4)<1e-12);
  assert.ok(Math.abs(s.dispersion-0.09)<1e-12);
  assert.ok(Math.abs(s.error+0.10)<1e-12);
  assert.ok(Math.abs(s.relative-0.04)<1e-12);
});
test('serie asimmetrica: semidispersione diversa dalla massima distanza dalla media', () => {
  const s=m.statistics([100,100,100,100,104],1);
  assert.equal(s.mean,100.8); assert.equal(s.dispersion,2); assert.equal(s.uncertainty,2);
  assert.equal(s.error,null); assert.equal(s.relative,null);
  assert.ok(s.mean+s.uncertainty<s.max);
});
test('letture identiche non producono incertezza nulla; riferimento nullo non ammette rapporto', () => {
  const s=m.statistics([100,100,100,100,100],1,100);
  assert.equal(s.dispersion,0); assert.equal(s.uncertainty,1); assert.equal(s.error,0);
  assert.equal(m.statistics([1,2],1,0).relative,null);
  assert.equal(m.statistics([],1),null);
});
test('risposte italiane, segno dell’errore e valori non numerici', () => {
  assert.equal(m.parseNumber(' -0,10 '),-0.1);
  assert.equal(m.parseNumber('2.4'),2.4);
  assert.ok(Number.isNaN(m.parseNumber('')));
  assert.ok(Number.isNaN(m.parseNumber('100 g')));
  assert.ok(Number.isNaN(m.parseNumber('Infinity')));
  assert.ok(m.closeTo(m.parseNumber('100,13'),100.125));
  assert.ok(!m.closeTo(m.parseNumber('100'),100.125));
});
