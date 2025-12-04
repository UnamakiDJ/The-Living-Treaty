What is The Living Treaty?
This project is a living longhouse of memory, built by L’nuk and friends, to bridge L’nui’suti (Mi’kmaw) and Western systems of history, law, and science using Two-Eyed Seeing (Etuaptmumk).

One eye sees through Mi’kmaw language, stories, treaty law, and land-based knowledge. The other eye sees through Western archaeology, geology, courts, and archives. The goal is not to blend them into one, but to use both eyes together for the good of all our relations.

Two-Eyed Seeing Timeline of Mi’kma’ki
Filter by era or tag to explore events. Each event has a Western lens, an L’nuk lens, and a brief Two-Eyed Seeing reflection.

Era: 
All eras
Tag: 
All tags
Kluskap Stories & Western Science
These are not “just myths”. Kluskap stories carry laws, ethics, and observations about ice, tides, water, and land that echo Western geology, oceanography, and ecology.

Pre-Contact Archaeology & Geology
Here, archaeological sites and geological changes are read alongside oral histories and Kluskap narratives. This is Deep Time Two-Eyed Seeing.

Key L’nuk Figures
Language as Worldview
L’nui’suti (Mi’kmaw) is a polysynthetic, verb-centred language. Words can carry who is acting, how, why, and in relation to whom. English and other Latin-based languages are more analytic, splitting the world into separate nouns and categories.

The examples below show words in Smith/Francis Orthography (S/F.O) and Listuguj Orthography (L.O), with short Two-Eyed Seeing notes.

Main Sources & Companions
This site is not a substitute for Elders, Knowledge Keepers, or local heritage centres. It’s a bridge and a starting point.
// bridge.js
// Mi’kmaw ↔ English “bridge” based on patterns you taught:
// -ji'j diminutive, time words, feeling-as-state, Netukulimk, Msit No'kmaq, L'nuk, etc.

/**
 * Small teaching lexicon.
 * You can expand this over time.
 */
const LNU_LEXICON = {
  "amu": {
    english: "bee",
    pos: "N-AN",
    sf: "amu",
    lo: "amu",
    semantic_root: "bee / pollinator relative",
    morphological_notes: "Base form. With -ji'j → amuji'j (little bee / bee child).",
    two_eyed:
      "In ecology: a keystone pollinator. In L’nui’suti: a buzzing relative that " +
      "feeds the plant nations and teaches collective work."
  },

  "amuji'j": {
    english: "little bee / bee child",
    pos: "N-AN-DIM",
    sf: "amuji'j",
    lo: "amuji'j",
    semantic_root: "amu (bee) + ji'j (little/child)",
    morphological_notes:
      "Diminutive/child form; pattern: base noun + -ji'j → 'little/child of X'.",
    two_eyed:
      "Shows how Mi’kmaw marks smallness as relationship (child) not just size."
  },

  "mia'wj": {
    english: "cat",
    pos: "N-AN",
    sf: "mia'wj",
    lo: "miawji",
    semantic_root: "cat / feline relative",
    morphological_notes: "Base for mia'wji'j (kitten).",
    two_eyed:
      "A newer animal in Mi’kma’ki, but the language receives it into the same relational web."
  },

  "mia'wji'j": {
    english: "kitten / little cat",
    pos: "N-AN-DIM",
    sf: "mia'wji'j",
    lo: "miawji'j",
    semantic_root: "mia'wj (cat) + ji'j (little/child)",
    morphological_notes: "Same diminutive pattern as amu → amuji'j.",
    two_eyed:
      "A kitten is the child-being of the cat nation, not just a small object."
  },

  "Netukulimk": {
    english: "balanced way of taking from the land",
    pos: "N-ABSTR",
    sf: "Netukulimk",
    lo: "Netukulimk",
    semantic_root: "taking what is needed so life continues.",
    morphological_notes: "Root teaching; source for Netukulimk'kul.",
    two_eyed:
      "Like 'sustainability' in Western science, but grounded in kinship, ceremony, " +
      "and seven generations responsibility."
  },

  "Netukulimk'kul": {
    english: "one who lives Netukulimk / the practice of Netukulimk",
    pos: "N-AGENT",
    sf: "Netukulimk'kul",
    lo: "Netukulimk'gul",
    semantic_root: "Netukulimk + kul (doer/practice).",
    morphological_notes:
      "kul acts like an agent/practice marker: ‘one who does / embodies Netukulimk’.",
    two_eyed:
      "Shifts from abstract principle to lived way of life – footsteps that keep balance."
  },

  "Msit No'kmaq": {
    english: "all my relations / all my relatives",
    pos: "EXPR",
    sf: "Msit No'kmaq",
    lo: "Msit No'kmaq",
    semantic_root: "all + my relatives.",
    morphological_notes:
      "Includes humans, animals, plants, waters, winds, ancestors – not just 'family'.",
    two_eyed:
      "Where Western science talks about 'ecosystems', Msit No'kmaq reminds us they are kin."
  },

  "L'nuk": {
    english: "the people (plural of L’nu)",
    pos: "N-PL",
    sf: "L'nuk",
    lo: "Lnu'k",
    semantic_root: "people living within seven generations.",
    morphological_notes:
      "You described L’nu as 'human that lives under seven generations' – this encodes that chain.",
    two_eyed:
      "Being L’nu is not just legal status; it is a relationship to past and future relatives."
  },

  "tpuk": {
    english: "late last night",
    pos: "ADV-TIME",
    sf: "tpuk",
    lo: "tpug",
    semantic_root: "time in the back of the night that just passed.",
    morphological_notes: "Time word rooted in experience, not clock hours.",
    two_eyed:
      "Shows how Mi’kmaw time is lived and felt – tied to cycles of night and rest."
  },

  "atel": {
    english: "just now",
    pos: "ADV-TIME",
    sf: "atel",
    lo: "atel",
    semantic_root: "the moment that just happened.",
    morphological_notes: "Anchors a story in the living present.",
    two_eyed:
      "Again, time is relational: 'just now' in relation to the storyteller and listeners."
  },

  "awnasiey": {
    english: "I am nervous",
    pos: "V-STATE-1SG",
    sf: "awnasiey",
    lo: "awnasiey",
    semantic_root: "to be in a nervous state.",
    morphological_notes:
      "Emotion expressed as a verb/state you are in, not a noun you possess.",
    two_eyed:
      "Mind, body, and spirit move together. Feelings are processes in relationship with the world."
  },

  "gesig": {
    english: "winter / it is winter",
    pos: "N/STAT",
    sf: "gesig",
    lo: "kesik",
    semantic_root: "winter season being here.",
    morphological_notes: "Can function both as 'winter' and 'it is winter'.",
    two_eyed:
      "Winter is a character with responsibilities – stories, rest, and teachings – not just a date range."
  }
};

// --- Helpers ---

function normalizeForm(form) {
  return (form || "").toString().trim().toLowerCase();
}

// Recognize basic morphology, especially -ji'j diminutive
function analyzeMorphology(formRaw) {
  const form = normalizeForm(formRaw);

  // pattern: base + ji'j or ji’j
  const dimMatch = form.match(/(.+?)ji['’]j$/);
  if (dimMatch) {
    const base = dimMatch[1];
    return {
      type: "diminutive",
      base_form: base,
      full_form: form
    };
  }

  return {
    type: "simple",
    base_form: form,
    full_form: form
  };
}

// Core lookup in both directions
function lookupBridgeEntry(queryRaw) {
  const q = normalizeForm(queryRaw);
  if (!q) return { matches: [], analysis: null };

  const matches = [];
  const analysis = analyzeMorphology(q);

  // 1. Direct Mi’kmaw form
  if (LNU_LEXICON[q]) {
    matches.push({
      key: q,
      source: "direct",
      entry: LNU_LEXICON[q]
    });
  }

  // 2. Diminutive base
  if (analysis.type === "diminutive") {
    const base = analysis.base_form;
    if (LNU_LEXICON[base]) {
      const baseEntry = LNU_LEXICON[base];
      matches.push({
        key: analysis.full_form,
        source: "diminutive",
        entry: {
          ...baseEntry,
          english: `little ${baseEntry.english} / child-${baseEntry.english}`,
          morphological_notes:
            (baseEntry.morphological_notes || "") +
            " · Recognized automatically as -ji'j child/little form."
        }
      });
    }
  }

  // 3. English gloss → Mi’kmaw
  Object.entries(LNU_LEXICON).forEach(([key, entry]) => {
    const gloss = normalizeForm(entry.english);
    if (gloss.includes(q) && !matches.find((m) => m.key === key)) {
      matches.push({
        key,
        source: "english-gloss",
        entry
      });
    }
  });

  return { matches, analysis };
}

// Render into #bridge-results
function renderBridgeToDom(queryRaw) {
  const container = document.getElementById("bridge-results");
  if (!container) return;

  container.innerHTML = "";
  const q = normalizeForm(queryRaw);

  if (!q) {
    container.innerHTML =
      "<p>Type a Mi’kmaw word or an English meaning to see what this small basket knows.</p>";
    return;
  }

  const { matches, analysis } = lookupBridgeEntry(q);

  if (!matches.length) {
    container.innerHTML =
      "<p>No matches in this teaching bundle yet. Try another word, " +
      "or work with language keepers to grow the basket.</p>";
    return;
  }

  matches.forEach(({ key, source, entry }) => {
    const div = document.createElement("article");
    div.className = "card";

    div.innerHTML = `
      <h3>${entry.english}</h3>
      <small>Lookup: "${queryRaw}" • matched via ${source}</small>
      <p><span class="badge">Key</span> ${key}</p>
      <p><span class="badge">S/F.O</span> ${entry.sf || "—"}</p>
      <p><span class="badge">L.O</span> ${entry.lo || "—"}</p>
      <p>${entry.morphological_notes || ""}</p>
      <p><strong>Two-Eyed Seeing:</strong> ${entry.two_eyed || ""}</p>
    `;

    container.appendChild(div);
  });

  if (analysis && analysis.type === "diminutive") {
    const note = document.createElement("p");
    note.style.fontSize = "0.8rem";
    note.style.color = "#9ca3af";
    note.textContent =
      `Pattern note: "${queryRaw}" was recognized as base + "-ji'j" (diminutive / child form).`;
    container.appendChild(note);
  }
}

// Attach to input + button
function setupBridgeUI() {
  const input = document.getElementById("bridge-input");
  const button = document.getElementById("bridge-button");
  if (!input || !button) return;

  const go = () => renderBridgeToDom(input.value);
  button.addEventListener("click", go);
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      go();
    }
  });

  renderBridgeToDom("");
}

if (typeof document !== "undefined") {
  document.addEventListener("DOMContentLoaded", setupBridgeUI);
}

// Export for Node tests if you ever want them
if (typeof module !== "undefined") {
  module.exports = {
    LNU_LEXICON,
    analyzeMorphology,
    lookupBridgeEntry
  };
}
