(() => {
  "use strict";
  const dataElement = document.getElementById("quiz-data");
  if (!dataElement) return;
  const dataset = JSON.parse(dataElement.textContent);
  const MAX_QUESTIONS = 30;
  const SECONDS_PER_QUESTION = 120;
  const categories = new Map(dataset.categories.map(c => [c.id, c]));
  const categoryBoxes = [...document.querySelectorAll("[data-quiz-category]")];
  const levelBoxes = [...document.querySelectorAll('input[name="quiz-level"]')];
  const config = document.getElementById("quiz-config");
  const active = document.getElementById("quiz-active");
  const results = document.getElementById("quiz-results");
  const startButton = document.getElementById("quiz-start");
  const countInput = document.getElementById("quiz-count");
  const countMinus = document.getElementById("quiz-count-minus");
  const countPlus = document.getElementById("quiz-count-plus");
  const durationOutput = document.getElementById("quiz-duration");
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

  function selectedCategory() {
    return categoryBoxes.find(box => box.checked && !box.disabled)?.value ?? null;
  }

  function getQuestionCount() {
    const count = Number(countInput.value);
    return Number.isInteger(count) && count >= 1 && count <= MAX_QUESTIONS ? count : null;
  }

  function setAvailability(box, available, message) {
    box.disabled = !available;
    if (!available) box.checked = false;
    const label = box.closest("label");
    label.classList.toggle("is-unavailable", !available);
    let note = label.querySelector(".quiz-unavailable-note");
    if (!available && !note) {
      note = document.createElement("small");
      note.className = "quiz-unavailable-note";
      note.textContent = message;
      label.append(note);
    }
    if (note) note.hidden = available;
  }

  function updateAvailability() {
    const level = levelBoxes.find(box => box.checked).value;
    const available = new Set(dataset.questions
      .filter(question => question.level === level)
      .map(question => question.category));
    for (const category of categoryBoxes) {
      setAvailability(category, available.has(category.value), "Non disponibile");
    }
    updateConfiguration();
  }

  function updateConfiguration() {
    const count = getQuestionCount();
    countMinus.disabled = count === 1;
    countPlus.disabled = count === MAX_QUESTIONS;
    startButton.disabled = selectedCategory() === null || count === null;
    durationOutput.textContent = count === null
      ? "Inserisci un numero da 1 a 30."
      : formatDuration(count * SECONDS_PER_QUESTION);
    if (!startButton.disabled) configError.hidden = true;
  }

  for (const category of categoryBoxes) category.addEventListener("change", updateConfiguration);
  for (const level of levelBoxes) level.addEventListener("change", updateAvailability);
  countInput.addEventListener("input", updateConfiguration);
  function changeQuestionCount(step) {
    // Anche un valore inserito a mano non valido è recuperabile tramite i pulsanti.
    const raw = countInput.valueAsNumber;
    const base = Number.isFinite(raw)
      ? Math.max(1, Math.min(MAX_QUESTIONS, Math.round(raw))) : 25;
    countInput.value = String(Math.max(1, Math.min(MAX_QUESTIONS, base + step)));
    updateConfiguration();
  }
  countMinus.addEventListener("click", () => changeQuestionCount(-1));
  countPlus.addEventListener("click", () => changeQuestionCount(1));
  updateAvailability();

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
      (s.count - s.index - 1) * s.seconds * 1000;
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
    for (let i = 0; i < s.count; i++) {
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

  function drawQuestions(pool, count) {
    const selected = shuffle(pool).slice(0, count);
    while (selected.length < count) {
      const candidateOrder = shuffle(pool);
      // Il dataset di prova è ridotto: evita ripetizioni consecutive quando possibile.
      if (candidateOrder.length > 1 && selected.length &&
          candidateOrder[0].id === selected[selected.length - 1].id) {
        candidateOrder.push(candidateOrder.shift());
      }
      for (const q of candidateOrder) {
        if (selected.length === count) break;
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
    const selected = selectedCategory();
    const count = getQuestionCount();
    if (count === null) {
      configError.textContent = "Scegli un numero di domande tra 1 e 30.";
      configError.hidden = false;
      return;
    }
    const level = document.querySelector('input[name="quiz-level"]:checked').value;
    const pool = dataset.questions.filter(q => q.category === selected && q.level === level);
    if (!pool.length) {
      configError.textContent = "Non ci sono domande per questa categoria e difficoltà.";
      configError.hidden = false;
      return;
    }
    const seconds = SECONDS_PER_QUESTION;
    const now = Date.now();
    session = {
      questions: drawQuestions(pool, count),
      responses: Array(count).fill(null),
      skipped: Array(count).fill(false),
      count,
      index: 0,
      level,
      seconds,
      deadline: now + count * seconds * 1000,
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
    const category = categories.get(q.category);
    counter.textContent = "Domanda " + (s.index + 1) + " di " + s.count;
    progressBar.style.width = (s.index / s.count * 100) + "%";
    document.getElementById("quiz-topic").textContent = category ? category.title : "";
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
    nextButton.textContent = s.index === s.count - 1
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
    if (session.index === session.count - 1) {
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
      for (let i = session.index; i < session.count; i++) {
        if (session.responses[i] === null) session.skipped[i] = true;
      }
      finish("timeout");
      return;
    }
    let count = 0;
    while (session && now >= session.perDeadline && count < session.count) {
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
      const category = categories.get(q.category);
      li.append(h3);
      if (category) li.append(labeledParagraph("Categoria:", category.title));
      if (response === null) {
        li.append(labeledParagraph("Stato:", s.skipped[i] ? "Saltata" : "Non raggiunta"));
      }
      li.append(labeledParagraph("La tua risposta:", response === null ? "Non data" : q.options[response]));
      li.append(labeledParagraph("Soluzione:", q.options[q.correct]));
      li.append(labeledParagraph("Spiegazione:", q.explanation));
      review.append(li);
    });
    const wrong = s.count - correct;
    document.getElementById("quiz-score").textContent = correct + " / " + s.count;
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

