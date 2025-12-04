# translator.py

from dataclasses import asdict
from typing import Dict, List, Optional, Literal

from lnu_home_context import build_home_context, HomeContext, MiKmawWord, MiKmawWordDialect

InputType = Literal["auto", "mikmaw", "english"]
OrthPref = Literal["SFO", "LO", "BOTH"]


class Translator:
    """
    Two-Eyed Seeing language bridge:
    - Uses your HomeContext lexical data
    - Lets you look up words by Mi'kmaw (S/F.O or Listuguj) or English
    - Returns spelling, meaning, context, Two-Eyed Seeing notes, sources
    """

    def __init__(self, context: Optional[HomeContext] = None):
        self.ctx: HomeContext = context or build_home_context()
        self._build_indexes()

    def _build_indexes(self) -> None:
        """Build internal search indexes for fast lookup."""
        self.sfo_index: Dict[str, str] = {}       # S/F.O -> word key
        self.lo_index: Dict[str, str] = {}        # Listuguj -> word key
        self.english_index: Dict[str, List[str]] = {}  # english.lower() -> [keys]

        for key, entry in self.ctx.mi_kmaw_words.items():
            # english index
            e = entry.english.lower()
            self.english_index.setdefault(e, []).append(key)

            # dialect index (we used "general" dialect in your context model)
            dialect: MiKmawWordDialect = entry.dialects.get("general")  # type: ignore
            if not dialect:
                continue

            if dialect.sf_orthography:
                sfo = dialect.sf_orthography.strip()
                self.sfo_index[sfo] = key

            if dialect.listuguj_orthography:
                lo = dialect.listuguj_orthography.strip()
                self.lo_index[lo] = key

    # --------- public API ---------

    def translate_word(
        self,
        query: str,
        input_type: InputType = "auto",
        orthography: OrthPref = "SFO"
    ) -> Optional[Dict]:
        """
        Look up a word and return a Two-Eyed Seeing bundle.

        query:       user input (Mi'kmaw or English)
        input_type:  "auto" | "mikmaw" | "english"
        orthography: "SFO" | "LO" | "BOTH" (output preference)

        Returns: dict with:
          - english
          - sfo_spelling
          - lo_spelling
          - context
          - two_eyed_seeing
          - sources (resolved to full citation dicts)
        """
        query = query.strip()
        if not query:
            return None

        key = None

        # 1. Decide how to interpret query
        if input_type == "english":
            key = self._lookup_by_english(query)
        elif input_type == "mikmaw":
            key = self._lookup_by_mikmaw(query)
        else:
            # auto: try Mi'kmaw first, then English
            key = self._lookup_by_mikmaw(query)
            if key is None:
                key = self._lookup_by_english(query)

        if key is None:
            return None

        return self._build_response_bundle(key, orthography)

    # --------- internal helpers ---------

    def _lookup_by_mikmaw(self, word: str) -> Optional[str]:
        """Try S/F.O and Listuguj indexes."""
        # exact match first
        if word in self.sfo_index:
            return self.sfo_index[word]
        if word in self.lo_index:
            return self.lo_index[word]

        # try case-insensitive match
        w_lower = word.lower()
        for k, v in self.sfo_index.items():
            if k.lower() == w_lower:
                return v
        for k, v in self.lo_index.items():
            if k.lower() == w_lower:
                return v

        return None

    def _lookup_by_english(self, english: str) -> Optional[str]:
        """Look up by exact English gloss (case-insensitive)."""
        e = english.lower().strip()
        keys = self.english_index.get(e)
        if not keys:
            return None
        # if multiple, just return the first for now
        return keys[0]

    def _build_response_bundle(self, key: str, orthography: OrthPref) -> Dict:
        """Build a dictionary with all the information for the given word key."""
        entry: MiKmawWord = self.ctx.mi_kmaw_words[key]
        dialect: MiKmawWordDialect = entry.dialects["general"]  # type: ignore

        # spelling preference logic
        if orthography == "SFO":
            sfo_spelling = dialect.sf_orthography
            lo_spelling = dialect.listuguj_orthography
        elif orthography == "LO":
            sfo_spelling = dialect.sf_orthography
            lo_spelling = dialect.listuguj_orthography
        else:  # BOTH
            sfo_spelling = dialect.sf_orthography
            lo_spelling = dialect.listuguj_orthography

        # resolve sources
        src_details: List[Dict] = []
        if dialect.sources:
            for sid in dialect.sources:
                src = self.ctx.sources.get(sid)
                if src:
                    src_details.append(asdict(src))

        return {
            "key": key,
            "english": entry.english,
            "sfo_spelling": sfo_spelling,
            "lo_spelling": lo_spelling,
            "context": dialect.context,
            "two_eyed_seeing": dialect.two_eyed_seeing,
            "sources": src_details,
        }


# --------- simple CLI test ---------

if __name__ == "__main__":
    t = Translator()

    # test a few lookups
    tests = [
        ("tupsi", "mikmaw"),
        ("alder tree", "english"),
        ("Te'sikiskik", "mikmaw"),
        ("Poqnitpa'q Aqtatpa'q", "mikmaw"),
        ("winter", "english"),
    ]

    for q, kind in tests:
        print("=" * 60)
        print(f"Query: {q!r} ({kind})")
        result = t.translate_word(q, input_type=kind)  # type: ignore
        if result is None:
            print("  -> Not found")
        else:
            print(f"English: {result['english']}")
            print(f"S/F.O:   {result['sfo_spelling']}")
            print(f"Listuguj:{result['lo_spelling']}")
            print("Context:")
            print(" ", result["context"])
            print("Two-Eyed Seeing:")
            print(" ", result["two_eyed_seeing"])
            print("Sources:")
            for s in result["sources"]:
                print(f"  - {s['details']}")
