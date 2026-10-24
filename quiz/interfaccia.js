(() => {
  "use strict";
  const dataElement = document.getElementById("quiz-data");
  if (!dataElement) return;
  const dataset = JSON.parse(dataElement.textContent);
  const QUESTION_COUNT = 25;
  const SECONDS = {easy: 150, medium: 120, hard: 90};
  const LEVEL_LABELS = {easy: "Facile", medium: "Media", hard: "Difficile"};
  const chapters = new Map(dataset.chapters.map(c => [c.file, c]));
  const groupBoxes = [...document.querySelectorAll("[data-quiz-group]")];
  const chapterBoxes = [...document.querySelectorAll("[data-quiz-chapter]")];
  const config = document.getElementById("quiz-config");
  const active = document.getElementById("quiz-active");
  const results = document.getElementById("quiz-results");
  const startButton = document.getElementById("quiz-start");
  const configError = document.getElementById("quiz-config-error");
  const nextButton = document.getElementById("quiz-next");
  const skipButton = document.getElementById("quiz-skip");
  const stopButton = document.getElementById("quiz-stop");
  const clock = document.getElementById("quiz-clock");
  const counter = document.getElementById("quiz-counter");
  const progressBar = document.getElementById("quiz-progress-fill");
  const prompt = document.getElementById("quiz-prompt");
  const answerList = document.getElementById("quiz-answers");
  const navigation = document.getElementById("quiz-navigation");
  const resultNavigation = document.getElementById("quiz-result-navigation");
  const statusSummary = document.getElementById("quiz-status-summary");
  const resultSummary = document.getElementById("quiz-result-summary");
  let session = null;
  let intervalId = null;

  function shuffle(items) {
    const copy = items.slice();
    for (let i = copy.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [copy[i], copy[j]] = [copy[j], copy[i]];
    }
    return copy;
  }

  function selectedChapters() {
    return new Set(chapterBoxes.filter(box => box.checked).map(box => box.value));
  }

  function synchronizeCategories() {
    for (const category of groupBoxes) {
      const children = chapterBoxes.filter(box => box.dataset.category === category.value);
      const selected = children.filter(box => box.checked).length;
      category.checked = children.length > 0 && selected === children.length;
      category.indeterminate = selected > 0 && selected < children.length;
    }
    startButton.disabled = selectedChapters().size === 0;
    if (selectedChapters().size) configError.hidden = true;
  }

  for (const category of groupBoxes) {
    category.addEventListener("change", () => {
      for (const chapter of chapterBoxes) {
        if (chapter.dataset.category === category.value) chapter.checked = category.checked;
      }
      synchronizeCategories();
    });
  }
  for (const chapter of chapterBoxes) chapter.addEventListener("change", synchronizeCategories);
  synchronizeCategories();

  function formatDuration(seconds) {
    const total = Math.max(0, Math.ceil(seconds));
    const minutes = Math.floor(total / 60);
    const remainder = String(total % 60).padStart(2, "0");
    return minutes + ":" + remainder;
  }

  function totalTimeRemaining(now) {
    const s = session;
    if (!s) return 0;
    // Il tempo residuo delle domande saltate/confermate non si accumula.
    const quota = Math.max(0, s.perDeadline - now) +
      (QUESTION_COUNT - s.index - 1) * s.seconds * 1000;
    return Math.min(s.deadline - now, quota) / 1000;
  }

  function questionStatus(s, index, finished = false) {
    if (s.responses[index] !== null) return "answered";
    if (s.skipped[index]) return "skipped";
    if (!finished && index === s.index) return "current";
    return "pending";
  }

  function renderStatuses(target, s, finished = false) {
    const labels = {
      answered: "risposta data",
      skipped: "saltata",
      current: "in corso",
      pending: finished ? "non raggiunta" : "da affrontare"
    };
    const fragment = document.createDocumentFragment();
    for (let i = 0; i < QUESTION_COUNT; i++) {
      const status = questionStatus(s, i, finished);
      const item = document.createElement("li");
      item.className = "quiz-nav-item is-" + status;
      item.setAttribute("aria-label", "Domanda " + (i + 1) + ": " + labels[status]);
      item.textContent = String(i + 1);
      fragment.append(item);
    }
    target.replaceChildren(fragment);
    const answered = s.responses.filter(response => response !== null).length;
    const skipped = s.skipped.filter(Boolean).length;
    const summary = "Risposte date: " + answered + " · Saltate: " + skipped;
    (finished ? resultSummary : statusSummary).textContent = summary;
  }

  function drawQuestions(pool) {
    const selected = shuffle(pool).slice(0, QUESTION_COUNT);
    while (selected.length < QUESTION_COUNT) {
      const candidateOrder = shuffle(pool);
      // Il dataset di prova è ridotto: evita ripetizioni consecutive quando possibile.
      if (candidateOrder.length > 1 && selected.length &&
          candidateOrder[0].id === selected[selected.length - 1].id) {
        candidateOrder.push(candidateOrder.shift());
      }
      for (const q of candidateOrder) {
        if (selected.length === QUESTION_COUNT) break;
        selected.push(q);
      }
    }
    return selected.map(q => ({
      ...q,
      order: shuffle(q.options.map((label, originalIndex) => ({label, originalIndex})))
    }));
  }

  function show(phase) {
    config.hidden = phase !== "config";
    active.hidden = phase !== "active";
    results.hidden = phase !== "results";
  }

  function startQuiz() {
    const selected = selectedChapters();
    const level = document.querySelector('input[name="quiz-level"]:checked').value;
    const pool = dataset.questions.filter(q => selected.has(q.chapter) && q.level === level);
    if (!pool.length) {
      configError.textContent = "Non ci sono domande di prova per questa selezione.";
      configError.hidden = false;
      return;
    }
    const seconds = SECONDS[level];
    const now = Date.now();
    session = {
      questions: drawQuestions(pool),
      responses: Array(QUESTION_COUNT).fill(null),
      skipped: Array(QUESTION_COUNT).fill(false),
      index: 0,
      level,
      seconds,
      deadline: now + QUESTION_COUNT * seconds * 1000,
      perDeadline: now + seconds * 1000
    };
    show("active");
    renderQuestion();
    clearInterval(intervalId);
    intervalId = setInterval(onTick, 250);
    onTick();
    window.scrollTo({top: 0, behavior: "instant"});
  }

  function renderQuestion() {
    const s = session;
    if (!s) return;
    const q = s.questions[s.index];
    const chapter = chapters.get(q.chapter);
    counter.textContent = "Domanda " + (s.index + 1) + " di " + QUESTION_COUNT;
    progressBar.style.width = (s.index / QUESTION_COUNT * 100) + "%";
    document.getElementById("quiz-topic").textContent = chapter
      ? chapter.area + " — " + chapter.title : "";
    prompt.textContent = q.prompt;
    answerList.replaceChildren();
    q.order.forEach((option, position) => {
      const label = document.createElement("label");
      label.className = "quiz-answer";
      const input = document.createElement("input");
      input.type = "radio";
      input.name = "quiz-answer";
      input.value = String(option.originalIndex);
      input.setAttribute("aria-label", "Alternativa " + (position + 1));
      input.addEventListener("change", () => { nextButton.disabled = false; });
      const text = document.createElement("span");
      text.textContent = option.label;
      label.append(input, text);
      answerList.append(label);
    });
    nextButton.disabled = true;
    nextButton.textContent = s.index === QUESTION_COUNT - 1
      ? "Termina il quiz" : "Conferma e prosegui";
    renderStatuses(navigation, s);
    prompt.tabIndex = -1;
    prompt.focus({preventScroll: true});
    clock.textContent = formatDuration(totalTimeRemaining(Date.now()));
  }

  function goForward(expired) {
    if (!session) return;
    if (session.responses[session.index] === null) {
      session.skipped[session.index] = true;
    }
    const oldDeadline = session.perDeadline;
    if (session.index === QUESTION_COUNT - 1) {
      finish("completed");
      return;
    }
    session.index += 1;
    session.perDeadline = (expired ? oldDeadline : Date.now()) + session.seconds * 1000;
    renderQuestion();
  }

  function onTick() {
    if (!session) return;
    const now = Date.now();
    if (now >= session.deadline) {
      for (let i = session.index; i < QUESTION_COUNT; i++) {
        if (session.responses[i] === null) session.skipped[i] = true;
      }
      finish("timeout");
      return;
    }
    let count = 0;
    while (session && now >= session.perDeadline && count < QUESTION_COUNT) {
      goForward(true);
      count++;
    }
    if (session) clock.textContent = formatDuration(totalTimeRemaining(now));
  }

  nextButton.addEventListener("click", () => {
    if (!session) return;
    onTick();
    if (!session) return;
    const checked = answerList.querySelector('input[name="quiz-answer"]:checked');
    if (!checked) return;
    session.responses[session.index] = Number(checked.value);
    goForward(false);
  });
  skipButton.addEventListener("click", () => {
    onTick();
    if (session) goForward(false);
  });
  stopButton.addEventListener("click", () => {
    if (session && window.confirm("Concludere ora? Le domande non completate saranno considerate errate.")) {
      if (session.responses[session.index] === null) session.skipped[session.index] = true;
      finish("early");
    }
  });
  startButton.addEventListener("click", startQuiz);

  function labeledParagraph(label, value) {
    const p = document.createElement("p");
    const heading = document.createElement("span");
    heading.className = "quiz-label";
    heading.textContent = label + " ";
    p.append(heading, document.createTextNode(value));
    return p;
  }

  function finish(reason) {
    if (!session) return;
    clearInterval(intervalId);
    intervalId = null;
    const s = session;
    session = null;
    let correct = 0;
    const review = document.getElementById("quiz-review");
    review.replaceChildren();
    renderStatuses(resultNavigation, s, true);
    s.questions.forEach((q, i) => {
      const response = s.responses[i];
      const right = response === q.correct;
      if (right) correct++;
      const li = document.createElement("li");
      li.className = "quiz-review-item" + (right ? "" : " is-wrong");
      const h3 = document.createElement("h3");
      h3.textContent = (i + 1) + ". " + q.prompt;
      const chapter = chapters.get(q.chapter);
      li.append(h3);
      if (chapter) li.append(labeledParagraph("Capitolo:", chapter.title));
      if (response === null) {
        li.append(labeledParagraph("Stato:", s.skipped[i] ? "Saltata" : "Non raggiunta"));
      }
      li.append(labeledParagraph("La tua risposta:", response === null ? "Non data" : q.options[response]));
      li.append(labeledParagraph("Soluzione:", q.options[q.correct]));
      li.append(labeledParagraph("Spiegazione:", q.explanation));
      review.append(li);
    });
    const wrong = QUESTION_COUNT - correct;
    const mark = (correct * 10 / QUESTION_COUNT).toFixed(1).replace(".", ",");
    document.getElementById("quiz-grade").textContent = mark + " / 10";
    document.getElementById("quiz-correct").textContent = String(correct);
    document.getElementById("quiz-wrong").textContent = String(wrong);
    const note = document.getElementById("quiz-finished-reason");
    note.textContent = reason === "timeout"
      ? "Tempo terminato. Le domande non risposte sono conteggiate come errate."
      : reason === "early"
        ? "Quiz concluso anticipatamente. Le domande non completate sono conteggiate come errate."
        : "Quiz completato.";
    show("results");
    window.scrollTo({top: 0, behavior: "instant"});
    document.getElementById("quiz-results-title").focus({preventScroll: true});
  }

  document.getElementById("quiz-again").addEventListener("click", () => {
    show("config");
    window.scrollTo({top: 0, behavior: "instant"});
    document.getElementById("quiz-config-title").focus({preventScroll: true});
  });

  // Il conteggio si basa su Date.now(): il cambio scheda non sospende il tempo.
  document.addEventListener("visibilitychange", onTick);
  window.addEventListener("pageshow", onTick);
})();
