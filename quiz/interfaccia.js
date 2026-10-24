(() => {
  'use strict';
  const COUNT = 25;
  const LEVELS = {facile:{seconds:150,choices:3},medio:{seconds:120,choices:4},difficile:{seconds:90,choices:5}};
  const root = document.querySelector('[data-quiz-app]');
  if (!root) return;
  const $ = id => root.querySelector('#' + id);
  const catalogue = JSON.parse($('quiz-catalogue-data').textContent);
  const bank = JSON.parse($('quiz-demo-data').textContent).domande;
  const selection = $('quiz-selection');
  const game = $('quiz-game');
  const results = $('quiz-results-screen');
  const chapterInputs = [...root.querySelectorAll('input[data-quiz-chapter]')];
  const categoryInputs = [...root.querySelectorAll('input[data-quiz-category]')];
  let state = null;
  let interval = null;
  const shuffle = values => {
    const result = [...values];
    for(let i = result.length - 1; i > 0; i--){
      const j = Math.floor(Math.random() * (i + 1));
      [result[i],result[j]] = [result[j],result[i]];
    }
    return result;
  };
  const selectedChapters = () => chapterInputs.filter(el => el.checked).map(el => el.value);
  const level = () => root.querySelector('input[name="quiz-livello"]:checked').value;
  const formatTime = ms => {
    const sec = Math.max(0,Math.ceil(ms/1000));
    return String(Math.floor(sec/60)).padStart(2,'0') + ':' + String(sec%60).padStart(2,'0');
  };
  const duration = () => COUNT * LEVELS[level()].seconds * 1000;
  function status(){
    for(const parent of categoryInputs) {
      const children = chapterInputs.filter(el => el.dataset.category === parent.value);
      const selected = children.filter(el => el.checked).length;
      parent.checked = selected === children.length && children.length > 0;
      parent.indeterminate = selected > 0 && selected < children.length;
    }
    const subjects = selectedChapters();
    const available = bank.filter(q => subjects.includes(q.capitolo) && q.livello === level()).length;
    $('quiz-selection-count').textContent = subjects.length + (subjects.length===1?' capitolo selezionato':' capitoli selezionati');
    $('quiz-length').textContent = COUNT + ' domande';
    $('quiz-total-time').textContent = formatTime(duration());
    $('quiz-start').disabled = subjects.length===0 || available < COUNT;
    const warning = $('quiz-warning');
    warning.hidden = subjects.length > 0 && available >= COUNT;
    warning.textContent = subjects.length===0
      ? 'Seleziona almeno un capitolo.'
      : 'Il dataset dimostrativo contiene ' + available + ' domande per questa selezione: ne servono almeno ' + COUNT + '.';
  }
  for(const parent of categoryInputs){
    parent.addEventListener('change', () => {
      for(const child of chapterInputs.filter(el => el.dataset.category === parent.value)) child.checked = parent.checked;
      status();
    });
  }
  for(const child of chapterInputs) child.addEventListener('change',status);
  for(const button of root.querySelectorAll('input[name="quiz-livello"]')) button.addEventListener('change',status);
  function buildQuestions(){
    const subjects = shuffle(selectedChapters());
    const buckets = subjects.map(chapter => ({
      chapter,questions:shuffle(bank.filter(q => q.capitolo === chapter && q.livello === level()))
    }));
    const chosen=[];
    // Bilanciamento tra capitoli selezionati senza ripetere la stessa domanda.
    while(chosen.length < COUNT){
      let added = 0;
      for(const bucket of buckets){
        if(chosen.length >= COUNT) break;
        const next=bucket.questions.pop();
        if(next){chosen.push(next);added++;}
      }
      if(!added) break;
    }
    return shuffle(chosen).map(q=>{
      const size=LEVELS[level()].choices;
      const answers=shuffle([q.opzioni[q.corretta],...shuffle(q.opzioni.filter((_,i)=>i!==q.corretta)).slice(0,size-1)]);
      return {...q,answers,correct:q.opzioni[q.corretta]};
    });
  }
  function start(){
    const chosen=buildQuestions();
    if(chosen.length!==COUNT){status();return;}
    const now=Date.now();
    const max=duration();
    state={questions:chosen,index:0,answers:Array(COUNT).fill(null),
      started:now,totalDeadline:now+max,questionDeadline:now+LEVELS[level()].seconds*1000,seconds:LEVELS[level()].seconds};
    selection.hidden=true;results.hidden=true;game.hidden=false;
    displayQuestion();
    interval=window.setInterval(tick,250);
    tick();
    window.scrollTo({top:0,behavior:'instant'});
  }
  function displayQuestion(){
    if(!state)return;
    const n=state.index;
    const question=state.questions[n];
    $('quiz-current').textContent='Domanda '+(n+1)+' di '+COUNT;
    $('quiz-topic').textContent=catalogue.find(item=>item.file===question.capitolo)?.title || '';
    $('quiz-question-text').textContent=question.testo;
    $('quiz-progress').value=n+1;
    const target=$('quiz-answers');
    target.replaceChildren();
    question.answers.forEach((answer,i)=>{
      const label=document.createElement('label');
      label.className='quiz-answer';
      const radio=document.createElement('input');
      radio.type='radio';radio.name='quiz-answer';radio.value=String(i);
      radio.addEventListener('change',()=>{$('quiz-next').disabled=false;});
      const span=document.createElement('span');
      span.textContent=answer;
      label.append(radio,span);
      target.append(label);
    });
    $('quiz-next').textContent=n===COUNT-1?'Concludi il quiz':'Conferma e continua';
    $('quiz-next').disabled=true;
    $('quiz-question-text').focus({preventScroll:true});
  }
  function move(choice){
    if(!state) return;
    state.answers[state.index]=choice;
    state.index++;
    if(state.index===COUNT){finish('completato');return;}
    state.questionDeadline=Math.min(Date.now()+state.seconds*1000,state.totalDeadline);
    displayQuestion();
    tick();
  }
  function tick(){
    if(!state)return;
    const now=Date.now();
    $('quiz-clock').textContent=formatTime(state.totalDeadline-now);
    $('quiz-clock').classList.toggle('warn',state.totalDeadline-now<5*60*1000);
    if(now>=state.totalDeadline){finish('tempo_totale');return;}
    // Recupera anche i timeout avvenuti quando la scheda era sospesa.
    while(state && now>=state.questionDeadline){
      state.answers[state.index]=null;
      const nextDeadline=state.questionDeadline+state.seconds*1000;
      state.index++;
      if(state.index===COUNT){finish('tempo_domanda');return;}
      state.questionDeadline=Math.min(nextDeadline,state.totalDeadline);
      displayQuestion();
    }
  }
  function addText(container,tag,value,cls){
    const node=document.createElement(tag);
    node.textContent=value;
    if(cls)node.className=cls;
    container.append(node);
    return node;
  }
  function finish(reason){
    if(!state)return;
    clearInterval(interval);interval=null;
    game.hidden=true;results.hidden=false;
    const right=state.questions.reduce((sum,q,i)=>sum+(state.answers[i]===q.correct?1:0),0);
    const unanswered=state.answers.filter(q=>q===null).length;
    const mark=(10*right/COUNT).toFixed(1).replace('.',',');
    $('quiz-mark').textContent=mark+'/10';
    $('quiz-correct').textContent=String(right)+'/'+COUNT;
    $('quiz-wrong').textContent=String(COUNT-right-unanswered);
    $('quiz-unanswered').textContent=String(unanswered);
    $('quiz-result-note').textContent=reason==='completato'
      ? 'Quiz completato.'
      : reason==='interrotto'
        ? 'Quiz concluso in anticipo: le domande rimanenti risultano senza risposta.'
        : 'Tempo scaduto: le domande non completate risultano senza risposta.';
    const review=$('quiz-review-list');review.replaceChildren();
    state.questions.forEach((q,i)=>{
      const answer=state.answers[i];
      const item=document.createElement('article');item.className='quiz-review-item';
      addText(item,'h3',(i+1)+'. '+q.testo);
      addText(item,'p',answer===q.correct?'Corretta':(answer===null?'Non risposta':'Errata'),
        'quiz-status '+(answer===q.correct?'ok':'bad'));
      if(answer!==q.correct)addText(item,'p','La tua risposta: '+(answer===null?'—':answer));
      addText(item,'p','Soluzione: '+q.correct);
      if(q.spiegazione)addText(item,'p',q.spiegazione,'quiz-footnote');
      review.append(item);
    });
    state=null;
    window.scrollTo({top:0,behavior:'instant'});
    $('quiz-results-title').focus({preventScroll:true});
  }
  $('quiz-start').addEventListener('click',start);
  $('quiz-next').addEventListener('click',()=>{
    const chosen=game.querySelector('input[name="quiz-answer"]:checked');
    if(chosen&&state)move(state.questions[state.index].answers[Number(chosen.value)]);
  });
  $('quiz-skip').addEventListener('click',()=>move(null));
  $('quiz-finish').addEventListener('click',()=>{
    if(state && window.confirm('Terminare il quiz? Le domande rimanenti saranno considerate senza risposta.')) finish('interrotto');
  });
  $('quiz-retry').addEventListener('click',()=>{
    results.hidden=true;game.hidden=true;selection.hidden=false;status();
    window.scrollTo({top:0,behavior:'instant'});
  });
  status();
})();
