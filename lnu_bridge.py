# lnu_bridge.py
# Prototype Mi'kmaw "language brain" for TheNetukilmkUtanProject
# Donald Marshall III x GPT-5.1 Thinking

from dataclasses import dataclass, asdict
from typing import List, Dict, Optional

# ---------- Core data structures ----------

@dataclass
class Morpheme:
    form: str                 # written form (SFO)
    gloss: str                # short meaning, e.g. "cold", "device"
    type: str                 # "root", "prefix", "suffix", "infix"
    notes: str = ""           # extra info (dialect, Pacifique form, etc.)

@dataclass
class LexiconEntry:
    sfo: str                          # Smith–Francis form
    pacifique: Optional[str]          # older spelling, if known
    pos: str                          # "VAI", "VII", "N", etc.
    english_gloss: str                # main English gloss
    animacy: Optional[str] = None     # "animate", "inanimate", or None
    semantic_fields: List[str] = None # e.g. ["humour", "ecology", "kinship"]
    morphemes: List[Morpheme] = None  # breakdown
    worldview_notes: str = ""         # Msit No'kmaq, TEK, story stuff

    def to_dict(self) -> Dict:
        d = asdict(self)
        # dataclasses don't auto-convert nested dataclasses -> dict
        if self.morphemes is not None:
            d["morphemes"] = [asdict(m) for m in self.morphemes]
        return d

# ---------- Seed morphemes (you expand this) ----------

MORPHEMES: List[Morpheme] = [
    # roots
    Morpheme("tekek", "cold (it is cold)", "root", "SFO; often pronounced with 'g' quality"),
    Morpheme("wikuom", "house, dwelling, storage place", "root", ""),
    Morpheme("aqan", "motion of arm/elbow, waving", "suffix", "used in weenieraqn joke"),
    Morpheme("ketlami", "care, concern, love-like care", "root", ""),
    Morpheme("welo't", "good, well, in good state", "root", ""),
    Morpheme("epsi", "I am warm / passionate", "root", "Pacifique/Prosper"),
    # derivational / inflectional bits
    Morpheme("ul", "to make, to cause", "suffix", "device/action builder"),
    Morpheme("qan", "device / instrument / 'thing that does it'", "suffix", ""),
    Morpheme("si", "I am (stative in some forms)", "suffix", ""),
    Morpheme("tasi", "in state/condition of", "suffix", ""),
]

# A quick lookup index
MORPHEME_INDEX: Dict[str, Morpheme] = {m.form: m for m in MORPHEMES}

# ---------- Seed lexicon (you keep adding entries) ----------

LEXICON: Dict[str, LexiconEntry] = {}

def add_entry(entry: LexiconEntry):
    LEXICON[entry.sfo] = entry

# Examples – you can add many more based on your books:

add_entry(LexiconEntry(
    sfo="tekek",
    pacifique=None,
    pos="ADJ-VII",
    english_gloss="it is cold",
    animacy="inanimate",
    semantic_fields=["weather", "sensation"],
    morphemes=[MORPHEME_INDEX["tekek"]],
    worldview_notes="Describes environmental condition; ties into survival, readiness, and TEK about seasons."
))

add_entry(LexiconEntry(
    sfo="Tekekulqan",
    pacifique=None,
    pos="N-INAN",
    english_gloss="refrigerator; the thing that makes things cold",
    animacy="inanimate",
    semantic_fields=["modern", "household", "humour"],
    morphemes=[
        MORPHEME_INDEX["tekek"],
        MORPHEME_INDEX["ul"],
        MORPHEME_INDEX["qan"],
    ],
    worldview_notes="Modern coinage: tekek (cold) + ul (cause/make) + qan (device). Should be checked/approved by fluent speakers/community."
))

add_entry(LexiconEntry(
    sfo="Kelu'si",
    pacifique=None,
    pos="VAI-1S",
    english_gloss="I am beautiful",
    animacy="animate",
    semantic_fields=["identity", "humour"],
    morphemes=[
        Morpheme("kelu'", "beautiful, good, nice-looking", "root", ""),
        Morpheme("si", "I am (stative)", "suffix", ""),
    ],
    worldview_notes="Used seriously and jokingly; fits rez humour and teasing about looks and confidence."
))

add_entry(LexiconEntry(
    sfo="epsi",
    pacifique="êpsi",
    pos="VAI-1S",
    english_gloss="I am warm; I am passionate",
    animacy="animate",
    semantic_fields=["emotion", "temperature", "spirit"],
    morphemes=[MORPHEME_INDEX["epsi"]],
    worldview_notes="Physical and emotional warmth; passion, fire inside. Prosper/Pacifique style."
))

add_entry(LexiconEntry(
    sfo="welo'tasi",
    pacifique=None,
    pos="VII",
    english_gloss="it is well taken care of; in a good state",
    animacy="inanimate",
    semantic_fields=["care", "netukulimk"],
    morphemes=[
        MORPHEME_INDEX["welo't"],
        MORPHEME_INDEX["tasi"],
    ],
    worldview_notes="Implies ongoing good relationship, not just a one-time fix. Fits Netukulimk."
))

# ---------- Core functions ----------

def lookup_word(sfo_word: str) -> Optional[LexiconEntry]:
    """
    Look up a word exactly as SFO in the lexicon.
    """
    return LEXICON.get(sfo_word)


def analyze_morphemes(sfo_word: str) -> List[Morpheme]:
    """
    Very simple heuristic splitter: tries to peel off known suffixes
    and match a root. This is a prototype; you will refine the rules.
    """
    found: List[Morpheme] = []
    remaining = sfo_word

    # Try suffixes first (longest first)
    suffixes = sorted(
        [m for m in MORPHERES if m.type == "suffix"],
        key=lambda m: len(m.form),
        reverse=True
    )

    # NOTE: variable name fix (MORPHEMES)
def analyze_morphemes(sfo_word: str) -> List[Morpheme]:
    """
    Very simple heuristic splitter: tries to peel off known suffixes
    and match a root. This is a prototype; you will refine the rules.
    """
    found: List[Morpheme] = []
    remaining = sfo_word

    suffixes = sorted(
        [m for m in MORPHEMES if m.type == "suffix"],
        key=lambda m: len(m.form),
        reverse=True
    )

    # peel suffixes
    changed = True
    while changed:
        changed = False
        for suf in suffixes:
            if remaining.endswith(suf.form) and remaining != suf.form:
                found.insert(0, suf)  # suffix at the end of list
                remaining = remaining[: -len(suf.form)]
                changed = True
                break

    # whatever is left, see if it's a root we know
    if remaining in MORPHEME_INDEX:
        found.insert(0, MORPHEME_INDEX[remaining])
    else:
        # unknown leftover root
        if remaining:
            found.insert(0, Morpheme(remaining, "UNKNOWN-ROOT", "root", "not yet in database"))

    return found
def explain_word(sfo_word: str) -> Dict:
    """
    High-level explanation used by your web portal.
    Returns a dict you can JSONify and send to the frontend.
    """
    entry = lookup_word(sfo_word)
    if entry:
        return {
            "source": "lexicon",
            "entry": entry.to_dict()
        }

    # If not found, try to analyze it morphologically as best we can.
    morphemes = analyze_morphemes(sfo_word)
    return {
        "source": "analysis",
        "entry": {
            "sfo": sfo_word,
            "english_gloss": "UNKNOWN (check with elder / dictionary)",
            "morphemes": [asdict(m) for m in morphemes],
            "worldview_notes": "Automatically analyzed. This is a guess. Must be verified by fluent speakers or reference works."
        }
    }
def build_humorous_compound(english_stub: str, mikmaq_motion_suffix: str = "aqan") -> str:
    """
    Build a playful compound like 'weenieraqn':
    English stub (roman letters) + a known Mi'kmaw motion suffix.
    This is NOT proper Mi'kmaw, but it's a teaching + humour tool.
    """
    # Very naive: just glue them together
    return english_stub + mikmaq_motion_suffix
>>> build_humorous_compound("weenie")
'weenieaqan'
