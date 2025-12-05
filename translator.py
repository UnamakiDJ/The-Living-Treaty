"""
translator.py

Mi'kmaw–English helper for The Living Treaty / NetukilmkUtanProject.

This is NOT a simple "word = word" dictionary.
It is a small engine for:

    • describing Mi'kmaw words as bundles of meaning (polysynthesis)
    • annotating animacy, grammar role, and worldview notes
    • generating candidate terms for new concepts (e.g., modern tech)
    • serving explanations to a JS/HTTP layer (bridge.js, api.py, etc.)

Design goals
------------
1. Keep Mi'kmaw logic at the centre, not English.
2. Make it easy to extend: elders, speakers, and learners can add/adjust entries.
3. Separate:
      - lexicon data
      - morphological rules
      - worldview/TEK notes
      - high-level "translator" interface
4. Fail gracefully: if we don't know a word, we still give something useful
   (e.g. pattern suggestion, placeholders, warnings).

IMPORTANT
---------
This file intentionally encodes only *tiny* example lexicon data.
Populate the LEXICON_* dicts with entries from:

    • Wilfred Prosper lexicon
    • L'nui'suti app (Smith-Francis Orthography)
    • Kataq / Oyster / other UINR stories
    • Elders' teachings

so the structure stays stable while the knowledge grows.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Any


# ---------------------------------------------------------------------------
# Data models
# ---------------------------------------------------------------------------

@dataclass
class Morpheme:
    surface: str            # written form, e.g. "kesal"
    gloss: str              # short English gloss, e.g. "love"
    role: str               # "root", "preverb", "suffix", "final", etc.
    notes: Optional[str] = None


@dataclass
class WordEntry:
    """One lexical entry for a Mi'kmaw word."""
    headword: str                 # citation form, e.g. "kesalul"
    english: str                  # core translation, e.g. "I love you"
    part_of_speech: str           # "VTA", "VAI", "NA", "NI", etc.
    animacy: Optional[str]        # "animate", "inanimate", or None
    morphemes: List[Morpheme]     # ordered breakdown
    register: Optional[str] = None    # "everyday", "ceremonial", "child", etc.
    worldview_tags: List[str] = None  # ["kinship", "netukulimk", "msit_nokmaq"]
    examples: List[str] = None        # example Mi'kmaw sentences


@dataclass
class AnalysisResult:
    word: str
    entry: Optional[WordEntry]
    # When we don't have a full entry, these fields provide best-guess info.
    guessed_morphemes: List[Morpheme]
    animacy_guess: Optional[str]
    worldview_notes: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "word": self.word,
            "has_entry": self.entry is not None,
            "entry": asdict(self.entry) if self.entry else None,
            "guessed_morphemes": [asdict(m) for m in self.guessed_morphemes],
            "animacy_guess": self.animacy_guess,
            "worldview_notes": self.worldview_notes,
        }


@dataclass
class GenerationRequest:
    """
    High-level description of a concept we want a Mi'kmaw word for.

    Example:
        concept = "refrigerator"
        purpose = "keeps food cold and safe to eat"
        domain_tags = ["home", "food", "modern_object"]
    """
    concept: str
    purpose: str
    domain_tags: List[str]


@dataclass
class GenerationCandidate:
    word: str
    breakdown: List[Morpheme]
    explanation: str
    caution: str  # reminder to check with fluent speakers / elders

    def to_dict(self) -> Dict[str, Any]:
        return {
            "word": self.word,
            "breakdown": [asdict(m) for m in self.breakdown],
            "explanation": self.explanation,
            "caution": self.caution,
        }


# ---------------------------------------------------------------------------
# Minimal example lexicon
# ---------------------------------------------------------------------------

# You should expand these dictionaries with real data.
# Keys = headword in Smith-Francis orthography.

LEXICON_CORE: Dict[str, WordEntry] = {}


def _init_lexicon() -> None:
    """Populate the core lexicon with starter entries.

    NOTE: This is only a tiny seed. In production, load this from JSON/YAML.
    """
    def W(headword, english, part_of_speech, animacy, morphemes, **kw) -> WordEntry:
        return WordEntry(
            headword=headword,
            english=english,
            part_of_speech=part_of_speech,
            animacy=animacy,
            morphemes=morphemes,
            worldview_tags=kw.get("worldview_tags", []),
            register=kw.get("register"),
            examples=kw.get("examples", []),
        )

    # "I love you" – core relationship verb from Rebecca Thomas' explanation.
    LEXICON_CORE["kesalul"] = W(
        headword="kesalul",
        english="I love you",
        part_of_speech="VTA-1sg>2",
        animacy="animate",
        morphemes=[
            Morpheme("ke-", "1st person acting (I)", "prefix"),
            Morpheme("sal", "love / precious", "root"),
            Morpheme("-ul", "1→2 object (you)", "final"),
        ],
        worldview_tags=["kinship", "emotion"],
        examples=["Kesalul nikmaq. – I love you, my relations."],
    )

    # "I hurt you" – similar shape, opposite valence.
    LEXICON_CORE["kesa'lul"] = W(
        headword="kesa'lul",
        english="I hurt you",
        part_of_speech="VTA-1sg>2",
        animacy="animate",
        morphemes=[
            Morpheme("ke-", "1st person acting (I)", "prefix"),
            Morpheme("sa'", "hurt / pain", "root"),
            Morpheme("-ul", "1→2 object (you)", "final"),
        ],
        worldview_tags=["emotion", "harm"],
    )

    # "I put you into the fire" – sacrifice / offering.
    LEXICON_CORE["ke'sa'lul"] = W(
        headword="ke'sa'lul",
        english="I place you into the fire (as offering/prayer)",
        part_of_speech="VTA-1sg>2",
        animacy="animate",
        morphemes=[
            Morpheme("ke'-", "into / into the fire", "preverb"),
            Morpheme("sa'", "put / place", "root"),
            Morpheme("-lul", "1→2 object", "final"),
        ],
        worldview_tags=["ceremony", "offering", "fire"],
    )

    # tekek – cold, used in your fridge example.
    LEXICON_CORE["tekek"] = W(
        headword="tekek",
        english="it is cold",
        part_of_speech="VII",  # intransitive inanimate
        animacy="inanimate",
        morphemes=[Morpheme("tekek", "cold (inanimate state)", "root")],
        worldview_tags=["weather", "state"],
    )

    # Nme'jik – fish (animate plural).
    LEXICON_CORE["nme'jik"] = W(
        headword="nme'jik",
        english="fishes",
        part_of_speech="NA-pl",
        animacy="animate",
        morphemes=[
            Morpheme("nme'", "fish", "root"),
            Morpheme("-jik", "animate plural", "suffix"),
        ],
        worldview_tags=["animals", "water"],
    )

    # msit no'kmaq – "all my relations".
    LEXICON_CORE["msit no'kmaq"] = W(
        headword="msit no'kmaq",
        english="all my relations",
        part_of_speech="expression",
        animacy=None,
        morphemes=[
            Morpheme("msit", "all", "quantifier"),
            Morpheme("no'kmaq", "my relations / all my kin", "noun"),
        ],
        worldview_tags=["msit_nokmaq", "philosophy", "relation"],
        register="ceremonial",
    )


_init_lexicon()


# ---------------------------------------------------------------------------
# Morphological & worldview rules (high level, not full linguistics)
# ---------------------------------------------------------------------------

ANIMACY_HINTS = {
    # if a word contains one of these roots, assume animate
    "nme'": "animate",
    "kataq": "animate",
    "waisik": "animate",   # animals
    "weskaq": "inanimate", # wind/air often treated differently
}

WORLDVIEW_HINTS = {
    "msit": "Msit No'kmaq – all is related.",
    "no'kmaq": "Relational kinship, not just biological family.",
    "nipugt": "In the woods / territory context.",
    "samqwan": "Water context – river, lake, ocean.",
    "e's": "Process / becoming; states often verbs, not nouns.",
}


def guess_animacy(word: str) -> Optional[str]:
    word_lower = word.lower()
    for frag, anim in ANIMACY_HINTS.items():
        if frag in word_lower:
            return anim
    # fallback: very rough heuristic
    if word_lower.endswith("jik"):
        return "animate"
    if word_lower.endswith("l") or word_lower.endswith("k"):
        return None
    return None


def collect_worldview_notes(word: str) -> List[str]:
    notes: List[str] = []
    lowered = word.lower()
    for frag, note in WORLDVIEW_HINTS.items():
        if frag in lowered:
            notes.append(note)
    return notes


# ---------------------------------------------------------------------------
# Core translator class
# ---------------------------------------------------------------------------

class LnuTranslator:
    """
    Main interface used by API/bridge.js.

    Typical usage from Python:

        tx = LnuTranslator()
        analysis = tx.analyze_word("kesalul")
        print(analysis.to_dict())

        candidates = tx.generate_modern_term(
            GenerationRequest(
                concept="refrigerator",
                purpose="keeps food and drink cold and safe",
                domain_tags=["home", "food", "modern_object"],
            )
        )
    """

    def __init__(self, lexicon: Optional[Dict[str, WordEntry]] = None):
        self.lexicon = lexicon or LEXICON_CORE

    # ------------------ lookup & analysis ------------------

    def lookup(self, word: str) -> Optional[WordEntry]:
        # Normalize a little: strip spaces, lowercase where safe.
        key = word.strip()
        # try exact first
        if key in self.lexicon:
            return self.lexicon[key]
        # loose search (case-insensitive)
        for hw, entry in self.lexicon.items():
            if hw.lower() == key.lower():
                return entry
        return None

    def analyze_word(self, word: str) -> AnalysisResult:
        entry = self.lookup(word)
        if entry:
            # We already have a curated breakdown; also attach worldview notes.
            notes = collect_worldview_notes(entry.headword)
            # merge stored worldview tags into notes in a friendly way
            if entry.worldview_tags:
                notes.append(
                    "Worldview tags: " + ", ".join(entry.worldview_tags)
                )
            return AnalysisResult(
                word=word,
                entry=entry,
                guessed_morphemes=[],
                animacy_guess=entry.animacy,
                worldview_notes=notes,
            )

        # No entry: try a light morphological guess based on patterns
        guessed: List[Morpheme] = []
        anim_guess = guess_animacy(word)
        notes = collect_worldview_notes(word)

        # very small set of pattern heuristics – extend as needed
        if word.endswith("jik"):
            stem = word[:-3]
            guessed.append(Morpheme(stem, "possible animate root", "root"))
            guessed.append(Morpheme("-jik", "animate plural", "suffix"))
            notes.append(
                "-jik often marks animate plural (people, animals, living beings)."
            )
        elif "'" in word:
            # split on apostrophes as rough morpheme boundaries
            parts = word.split("'")
            for p in parts:
                if not p:
                    continue
                guessed.append(Morpheme(p, "possible morpheme", "unknown"))
            notes.append(
                "Apostrophes often mark long vowels or morpheme boundaries."
            )

        if not guessed:
            guessed.append(
                Morpheme(word, "unknown – add to lexicon with elders", "unknown")
            )
            notes.append(
                "No lexicon entry yet. This is a good candidate to confirm with fluent speakers."
            )

        if anim_guess:
            notes.append(f"Animacy guess: {anim_guess}.")

        return AnalysisResult(
            word=word,
            entry=None,
            guessed_morphemes=guessed,
            animacy_guess=anim_guess,
            worldview_notes=notes,
        )

    # ------------------ sentence helpers ------------------

    def analyze_sentence(self, sentence: str) -> Dict[str, Any]:
        """
        Break a Mi'kmaw sentence into words and analyze each.
        This does NOT attempt full syntax – just word-level support.
        """
        # simple tokenization – you may want something smarter later
        tokens = [t for t in sentence.replace(",", " ").split() if t]
        analyses = [self.analyze_word(tok).to_dict() for tok in tokens]
        return {
            "sentence": sentence,
            "tokens": tokens,
            "analyses": analyses,
        }

    # ------------------ modern term generation ------------------

    def generate_modern_term(self, req: GenerationRequest) -> List[GenerationCandidate]:
        """
        Suggest Mi'kmaw-style words for a modern concept.

        This uses PATTERNS, not "translations". All results MUST be
        checked with fluent speakers / elders before real-world use.
        """

        candidates: List[GenerationCandidate] = []

        # 1. Example pattern for "thing that keeps X cold" (refrigerator).
        if "refrigerator" in req.concept.lower() or (
            "cold" in req.purpose.lower() and "food" in req.purpose.lower()
        ):
            # Use tekek (it is cold) + container / house notion.
            # We'll propose something like:
            #   "Mesentaqtekekim" – "that which makes-things-be-cold-inside"
            morphemes = [
                Morpheme("mesen-", "to keep / maintain", "preverb"),
                Morpheme("taq-", "inside / container / dwelling", "root-ish"),
                Morpheme("tekek", "cold (inanimate state)", "root"),
                Morpheme("-im", "instrument / thing that does this", "suffix"),
            ]
            word = "Mesentaqtekekim"
            explanation = (
                "Built from mesen- (to keep/maintain) + taq (inside) + tekek (cold) "
                "+ -im (instrument). Rough sense: 'the thing that keeps the inside cold'."
            )
            caution = (
                "Prototype only. Confirm phonology, stress and cultural fit with fluent "
                "Mi'kmaw speakers and elders before adopting. Adjust spelling to local dialect."
            )
            candidates.append(GenerationCandidate(word, morphemes, explanation, caution))

        # 2. Generic fallback pattern: describe purpose in verbs.
        # This gives at least one candidate even if we have no handcrafted pattern.
        base_root = "apoqnmatultim"  # "it helps / it supports" – placeholder root
        morphemes = [
            Morpheme(base_root, "to help / support (placeholder root)", "root"),
            Morpheme("-ik", "thing which does this", "suffix"),
        ]
        generic_word = base_root.capitalize() + "ik"
        explanation = (
            "Generic helper pattern: root meaning 'to help/support' + -ik (instrument). "
            "Use this only as a brainstorming starting point."
        )
        caution = (
            "Generic pattern. Replace the root with a better verb that reflects the purpose "
            "once you consult speakers (e.g., a more specific verb for how the object acts)."
        )
        candidates.append(GenerationCandidate(generic_word, morphemes, explanation, caution))

        return candidates

    # ------------------ API-friendly wrappers ------------------

    def explain_word_for_api(self, word: str) -> Dict[str, Any]:
        """Return a JSON-serializable explanation for one word."""
        return self.analyze_word(word).to_dict()

    def explain_sentence_for_api(self, sentence: str) -> Dict[str, Any]:
        """Return a JSON-serializable explanation for a sentence."""
        return self.analyze_sentence(sentence)

    def generate_term_for_api(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Accept a dict from bridge.js and return candidate words.

        Expected payload:
            {
                "concept": "refrigerator",
                "purpose": "keeps food and drinks cold",
                "domain_tags": ["home", "food", "modern_object"]
            }
        """
        req = GenerationRequest(
            concept=payload.get("concept", ""),
            purpose=payload.get("purpose", ""),
            domain_tags=payload.get("domain_tags", []) or [],
        )
        cands = self.generate_modern_term(req)
        return {
            "concept": req.concept,
            "candidates": [c.to_dict() for c in cands],
        }

# lexicon_data.py
# Python mirror of lexicon.js for use inside translator.py

from typing import List, Dict, Any

LNU_LEXICON: List[Dict[str, Any]] = [
    {
        "lemma": "kwe'",
        "surface": "Kwe'",
        "pos": "interjection",
        "gloss": "Hello",
        "animacy": None,
        "root": "kwe'",
        "morphology": [
            {"piece": "kwe'", "type": "root", "gloss": "greeting / hello"},
        ],
        "examples": [
            {
                "mikmaq": "Kwe', teluisi Katew.",
                "english": "Hello, my name is Katew.",
            }
        ],
        "source": "Kataq: The Story of Our Eels",
        "worldview_notes": [
            "Used as a friendly greeting; often the first word children learn.",
            "Opening a story with “Kwe’” sets the tone of respect and relationship.",
        ],
        "needsReview": False,
    },

    {
        "lemma": "teluisi",
        "surface": "Teluisi",
        "pos": "expression",
        "gloss": "My name is …",
        "animacy": None,
        "root": "teluis-",
        "morphology": [
            {"piece": "telu-", "type": "root", "gloss": "to be called / named (approx.)"},
            {"piece": "-isi", "type": "suffix", "gloss": "1st person ‘I am called’ (approx.)"},
        ],
        "examples": [
            {"mikmaq": "Teluisi Katew.", "english": "My name is Katew."}
        ],
        "source": "Kataq: The Story of Our Eels",
        "worldview_notes": [
            "Introductions in Mi’kmaw often come with place and kin, not just personal name.",
        ],
        "needsReview": True,
    },

    {
        "lemma": "kesalul",
        "surface": "Kesalul",
        "pos": "verb",
        "gloss": "I love you (singular)",
        "animacy": "animate",
        "root": "kesal-",
        "morphology": [
            {"piece": "ke-", "type": "prefix", "gloss": "you (2nd person)"},
            {"piece": "sal", "type": "root", "gloss": "love, be precious"},
            {"piece": "-ul", "type": "suffix", "gloss": "I (1st person) acting on you"},
        ],
        "examples": [
            {
                "mikmaq": "Kesalul, nikmaq.",
                "english": "I love you, my family.",
            }
        ],
        "source": "Rebecca Thomas – I Place You Into the Fire; community usage",
        "worldview_notes": [
            "Tiny shifts in glottal stop position change meaning.",
            "Shows the link between sound, emotion, and ceremony (fire).",
        ],
        "needsReview": False,
    },

    {
        "lemma": "msit no'kmaq",
        "surface": "Msit No'kmaq",
        "pos": "expression",
        "gloss": "All my relations",
        "animacy": None,
        "root": "msit + no'kmaq",
        "morphology": [
            {"piece": "msit", "type": "root", "gloss": "all, everything"},
            {"piece": "no'kmaq", "type": "root", "gloss": "my relations / all my kin"},
        ],
        "examples": [
            {
                "mikmaq": "Msit No'kmaq, wela'liek.",
                "english": "All my relations, I thank you.",
            }
        ],
        "source": "Community teaching; LD manual",
        "worldview_notes": [
            "Names the full web of kin – people, animals, plants, waters, winds, ancestors.",
            "Implies responsibility to everything you’re related to.",
        ],
        "needsReview": False,
    },

    {
        "lemma": "wela'lin",
        "surface": "Wela'lin",
        "pos": "expression",
        "gloss": "Thank you",
        "animacy": None,
        "root": "wel-",
        "morphology": [
            {"piece": "wel", "type": "root", "gloss": "good, well"},
            {"piece": "a'lin", "type": "suffix", "gloss": "to be thus / let it be so (approx.)"},
        ],
        "examples": [
            {"mikmaq": "Wela'lin Msit No'kmaq.", "english": "Thank you, all my relations."}
        ],
        "source": "LD manual; everyday speech",
        "worldview_notes": [
            "Often deeper than ‘thanks’ – about the state you’re brought into.",
        ],
        "needsReview": True,
    },

    {
        "lemma": "netukulimk",
        "surface": "Netukulimk",
        "pos": "noun-abstract",
        "gloss": "Taking only what you need while caring for land and future generations",
        "animacy": None,
        "root": "netukulimk",
        "morphology": [],
        "examples": [
            {
                "mikmaq": "Netukulimk wjit aq aqamk skitqamu.",
                "english": "Netukulimk is how we live with the earth.",
            }
        ],
        "source": "Mi'kmaw ethics / LD resource manual",
        "worldview_notes": [
            "Key law of balance between harvest and responsibility.",
        ],
        "needsReview": False,
    },

    {
        "lemma": "kataq",
        "surface": "Kataq",
        "pos": "noun-animate",
        "gloss": "American eel",
        "animacy": "animate",
        "root": "kataq",
        "morphology": [
            {"piece": "kataq", "type": "root", "gloss": "eel"},
        ],
        "examples": [
            {
                "mikmaq": "Kataq wjit apoqnmulti'juin lnu'k.",
                "english": "The eel helps Mi'kmaq people live.",
            }
        ],
        "source": "Kataq: The Story of Our Eels",
        "worldview_notes": [
            "Eel is a teacher and relative in the story, not just food.",
        ],
        "needsReview": True,
    },

    {
        "lemma": "yellow eel",
        "surface": "Kataq (yellow stage)",
        "pos": "noun-animate",
        "gloss": "Yellow eel life stage",
        "animacy": "animate",
        "root": "kataq",
        "morphology": [],
        "examples": [],
        "source": "Kataq: The Story of Our Eels",
        "worldview_notes": [
            "Represents middle life stage in lakes and rivers.",
        ],
        "needsReview": True,
    },

    {
        "lemma": "silver eel",
        "surface": "Kataq (silver stage)",
        "pos": "noun-animate",
        "gloss": "Silver eel life stage (ocean-going)",
        "animacy": "animate",
        "root": "kataq",
        "morphology": [],
        "examples": [],
        "source": "Kataq: The Story of Our Eels",
        "worldview_notes": [
            "Stage for the long journey back to Sargasso Sea.",
        ],
        "needsReview": True,
    },

    {
        "lemma": "oyster",
        "surface": "oyster (fill exact Mi'kmaw form)",
        "pos": "noun-animate",
        "gloss": "Oyster",
        "animacy": "animate",
        "root": "TODO",
        "morphology": [],
        "examples": [],
        "source": "Oyster storybook (your photos)",
        "worldview_notes": [
            "Described as filtering and cleaning the water in the lakes.",
        ],
        "needsReview": True,
    },

    {
        "lemma": "apoqnmulti'juin",
        "surface": "apoqnmulti'juin",
        "pos": "verb/phrase",
        "gloss": "helps us live / we are helped to live (approx.)",
        "animacy": None,
        "root": "TODO",
        "morphology": [],
        "examples": [],
        "source": "Kataq: The Story of Our Eels",
        "worldview_notes": [
            "Shows mutual support between people and more-than-human kin.",
        ],
        "needsReview": True,
    },

    {
        "lemma": "mother earth",
        "surface": "Mother Earth (fill preferred Mi'kmaw form)",
        "pos": "noun-proper",
        "gloss": "Mother Earth",
        "animacy": "animate",
        "root": "TODO",
        "morphology": [],
        "examples": [],
        "source": "Eel + Oyster stories; LD manual",
        "worldview_notes": [
            "Central relative that all the water teachings return to.",
        ],
        "needsReview": True,
    },
]

# ---------------------------------------------------------------------------
# Module-level singleton (optional convenience)
# ---------------------------------------------------------------------------

_default_translator: Optional[LnuTranslator] = None


def get_translator() -> LnuTranslator:
    global _default_translator
    if _default_translator is None:
        _default_translator = LnuTranslator()
    return _default_translator
from lexicon_data import LNU_LEXICON

class LnuTranslator:
    def __init__(self):
        self.lexicon = LNU_LEXICON

    def find_entry(self, word: str):
        lower = word.lower()
        for entry in self.lexicon:
            if entry["surface"].lower() == lower or entry["lemma"].lower() == lower:
                return entry
        return None

    # and your explain_word_for_api() can call self.find_entry(...)
