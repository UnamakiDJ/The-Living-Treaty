// lexicon.js
// Seed Mi'kmaw lexicon for The Living Treaty / NetukilmkUtanProject.
// Structure is intentionally simple so JS + Python can share the same “shape”.

export const LNU_LEXICON = [
  {
    lemma: "kwe'",
    surface: "Kwe'",
    pos: "interjection",
    gloss: "Hello",
    animacy: null,
    root: "kwe'",
    morphology: [
      { piece: "kwe'", type: "root", gloss: "greeting / hello" }
    ],
    examples: [
      {
        mikmaq: "Kwe', teluisi Katew.",
        english: "Hello, my name is Katew."
      }
    ],
    source: "Kataq: The Story of Our Eels",
    worldview_notes: [
      "Used as a friendly greeting; often the first word children learn.",
      "Opening a story with “Kwe’” sets the tone of respect and relationship."
    ],
    needsReview: false
  },

  {
    lemma: "teluisi",
    surface: "Teluisi",
    pos: "expression",
    gloss: "My name is …",
    animacy: null,
    root: "teluis-",
    morphology: [
      { piece: "telu-",  type: "root",   gloss: "to be called / to be named (approx.)" },
      { piece: "-isi",   type: "suffix", gloss: "1st person (‘I am called’ – approximate)" }
    ],
    examples: [
      {
        mikmaq: "Teluisi Katew.",
        english: "My name is Katew."
      }
    ],
    source: "Kataq: The Story of Our Eels",
    worldview_notes: [
      "Introductions in Mi’kmaw usually come with place and kin, not just personal name."
    ],
    needsReview: true   // double-check the root analysis with elders / Prosper
  },

  {
    lemma: "kesalul",
    surface: "Kesalul",
    pos: "verb",
    gloss: "I love you (singular)",
    animacy: "animate",
    root: "kesal-",
    morphology: [
      { piece: "ke-",  type: "prefix", gloss: "you (2nd person)" },
      { piece: "sal",  type: "root",   gloss: "love, be precious" },
      { piece: "-ul",  type: "suffix", gloss: "I (1st person) acting on you" }
    ],
    examples: [
      {
        mikmaq: "Kesalul, nikmaq.",
        english: "I love you, my family."
      }
    ],
    source: "Rebecca Thomas – I Place You Into the Fire (poem); community usage",
    worldview_notes: [
      "Tiny shifts in glottal stop position change meaning: kesa’lul (I hurt you), ke’sa’lul (I put you into the fire).",
      "Shows how sound, emotion, and ceremony (fire) are tightly connected."
    ],
    needsReview: false
  },

  {
    lemma: "msit no'kmaq",
    surface: "Msit No'kmaq",
    pos: "expression",
    gloss: "All my relations",
    animacy: null,
    root: "msit + no'kmaq",
    morphology: [
      { piece: "msit",    type: "root", gloss: "all, everything" },
      { piece: "no'kmaq", type: "root", gloss: "my relations / all my kin" }
    ],
    examples: [
      {
        mikmaq: "Msit No'kmaq, wela'liek.",
        english: "All my relations, I thank you."
      }
    ],
    source: "Community teaching; LD manual",
    worldview_notes: [
      "Names the full web of kin – people, animals, plants, waters, winds, ancestors.",
      "Implies responsibility: if everything is your relation, you owe respect to everything."
    ],
    needsReview: false
  },

  {
    lemma: "wela'lin",
    surface: "Wela'lin",
    pos: "expression",
    gloss: "Thank you",
    animacy: null,
    root: "wel-",
    morphology: [
      { piece: "wel",    type: "root",   gloss: "good, well" },
      { piece: "a'lin",  type: "suffix", gloss: "to be thus / let it be so (approx.)" }
    ],
    examples: [
      {
        mikmaq: "Wela'lin Msit No'kmaq.",
        english: "Thank you, all my relations."
      }
    ],
    source: "LD manual; everyday speech",
    worldview_notes: [
      "Often deeper than ‘thanks’ – closer to ‘thank you for bringing me to this state/feeling’.",
      "Links gratitude to the state of balance between people and the land."
    ],
    needsReview: true
  },

  {
    lemma: "netukulimk",
    surface: "Netukulimk",
    pos: "noun-abstract",
    gloss: "Taking only what you need while caring for the land and future generations",
    animacy: null,
    root: "netukulimk",
    morphology: [],
    examples: [
      {
        mikmaq: "Netukulimk wjit aq aqamk skitqamu.",
        english: "Netukulimk is how we live with the earth."
      }
    ],
    source: "Mi'kmaw ethics / LD resource manual",
    worldview_notes: [
      "Key law of balance: harvest with respect, never taking so much that the system is harmed.",
      "Perfect bridge concept for conservation science and climate work."
    ],
    needsReview: false
  },

  {
    lemma: "kataq",
    surface: "Kataq",
    pos: "noun-animate",
    gloss: "American eel",
    animacy: "animate",
    root: "kataq",
    morphology: [
      { piece: "kataq", type: "root", gloss: "eel" }
    ],
    examples: [
      {
        mikmaq: "Kataq wjit apoqnmulti'juin lnu'k.",
        english: "The eel helps Mi'kmaq people live."
      }
    ],
    source: "Kataq: The Story of Our Eels",
    worldview_notes: [
      "In the story, Kataq speaks in first person and teaches about migration and pollution.",
      "Shows eels as relatives and teachers, not just ‘resource’."
    ],
    needsReview: true   // especially the example sentence spelling
  },

  {
    lemma: "yellow eel",
    surface: "Kataq (yellow stage)",
    pos: "noun-animate",
    gloss: "Yellow eel life stage",
    animacy: "animate",
    root: "kataq",
    morphology: [],
    examples: [
      {
        mikmaq: "Telu'tuksit kataq wtapasi't, 'yellow eel'.",
        english: "Now they call me yellow eel."
      }
    ],
    source: "Kataq: The Story of Our Eels – middle life stage",
    worldview_notes: [
      "Life stages (glass, yellow, silver) are part of the teaching about cycles and change."
    ],
    needsReview: true
  },

  {
    lemma: "silver eel",
    surface: "Kataq (silver stage)",
    pos: "noun-animate",
    gloss: "Silver eel life stage (ocean-going)",
    animacy: "animate",
    root: "kataq",
    morphology: [],
    examples: [
      {
        mikmaq: "Sulieweyamuksi't kataq, 'silver eel'.",
        english: "Now they call me silver eel."
      }
    ],
    source: "Kataq: The Story of Our Eels – returning to Sargasso Sea",
    worldview_notes: [
      "Colour change is read as Mother Earth preparing the eel for the long journey home."
    ],
    needsReview: true
  },

  {
    lemma: "oyster",
    surface: "oyster (from storybook – fill exact form)",
    pos: "noun-animate",
    gloss: "Oyster",
    animacy: "animate",
    root: "TODO",
    morphology: [],
    examples: [
      {
        mikmaq: "Oysters also breathe with water.",
        english: "Line from oyster story – fill Mi'kmaw text from book."
      }
    ],
    source: "Oyster storybook you photographed",
    worldview_notes: [
      "Oysters are described as cleaning water and caring for lakes and people.",
      "Good anchor word for teaching ecosystem services in Mi’kmaw."
    ],
    needsReview: true
  },

  {
    lemma: "apoqnmulti'juin",
    surface: "apoqnmulti'juin",
    pos: "verb/phrase",
    gloss: "we are helped to live / it helps us live (approx.)",
    animacy: null,
    root: "poqnm- ?",
    morphology: [],
    examples: [
      {
        mikmaq: "Kataq wjit apoqnmulti'juin lnu'k.",
        english: "The eel helps Mi'kmaq people live."
      }
    ],
    source: "Kataq: The Story of Our Eels",
    worldview_notes: [
      "Life is framed as mutual helping: beings help each other live, not one side using the other."
    ],
    needsReview: true
  },

  {
    lemma: "kji'kmanaq wustamuk",
    surface: "Kji'kmanaq Wustamuk",
    pos: "noun-proper",
    gloss: "Mother Earth (one common phrase – adjust to your dialect)",
    animacy: "animate",
    root: "wustam-",
    morphology: [],
    examples: [
      {
        mikmaq: "By respecting Mother Earth, apoqnmulti'jiew wjit kataq.",
        english: "By respecting Mother Earth, we help the eels live."
      }
    ],
    source: "Kataq + Oyster stories (Mother Earth theme)",
    worldview_notes: [
      "Mother Earth is treated as a living relative with agency, not background scenery."
    ],
    needsReview: true
  }
];
import { LNU_LEXICON } from "./lexicon.js";

export function lookupLocalWord(word) {
  const lower = word.toLowerCase();
  return (
    LNU_LEXICON.find(
      (e) =>
        e.surface.toLowerCase() === lower ||
        e.lemma.toLowerCase() === lower
    ) || null
  );
}
