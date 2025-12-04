from typing import Optional, Dict, Any
from lnu_home_context import build_home_context, MiKmawWord

class Translator:
    def __init__(self) -> None:
        self.home = build_home_context()

    def _find_by_mikmaw(self, form: str) -> Optional[MiKmawWord]:
        f = form.strip().lower()
        for w in self.home.mi_kmaw_words.values():
            d = w.dialects.get("general")
            if not d:
                continue
            if (d.sf_orthography or "").lower() == f:
                return w
            if (d.listuguj_orthography or "").lower() == f:
                return w
        return None

    def _find_by_english(self, gloss: str) -> Optional[MiKmawWord]:
        g = gloss.strip().lower()
        for w in self.home.mi_kmaw_words.values():
            if w.english.lower() == g or g in w.english.lower():
                return w
        return None

    def translate(self, q: str, input_type: str = "auto") -> Optional[Dict[str, Any]]:
        """
        q: query (Mi'kmaw or English)
        input_type: "mikmaw", "english", or "auto"
        """
        if not q.strip():
            return None

        if input_type == "mikmaw":
            w = self._find_by_mikmaw(q)
        elif input_type == "english":
            w = self._find_by_english(q)
        else:
            w = self._find_by_mikmaw(q) or self._find_by_english(q)

        if not w:
            return None

        d = w.dialects["general"]
        return {
            "english": w.english,
            "sf_orthography": d.sf_orthography,
            "listuguj_orthography": d.listuguj_orthography,
            "context": d.context,
            "two_eyed_seeing": d.two_eyed_seeing,
            "sources": d.sources,
        }


if __name__ == "__main__":
    tr = Translator()
    for q in ["tupsi", "winter", "Te'sikiskik", "Netukulimk"]:
        print("====", q, "====")
        print(tr.translate(q, input_type="auto"))
        print()
