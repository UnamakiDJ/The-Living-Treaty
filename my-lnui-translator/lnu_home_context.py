from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional

# ---------- Source References ----------

@dataclass
class SourceRef:
    """Bibliographic or web reference for where knowledge came from."""
    id: str                  # short key, e.g. "schmidt_marshall_1995"
    title: str
    details: str             # short citation string
    url: Optional[str] = None


# ---------- People / Figures ----------

@dataclass
class MiKmawFigure:
    name: str
    role: str
    life_dates: str
    bio: str
    significance: str
    key_sources: List[str]           # list of SourceRef.id
    image_url: Optional[str] = None  # for website display


# ---------- Vocabulary / Translation ----------

@dataclass
class MiKmawWordDialect:
    """
    Holds spelling/pronunciation for one orthographic tradition
    plus relational notes.
    """
    sf_orthography: Optional[str] = None        # Smith–Francis
    listuguj_orthography: Optional[str] = None  # Listuguj
    pronunciation_sfo: Optional[str] = None
    pronunciation_lo: Optional[str] = None
    pronunciation_ipa: Optional[str] = None
    context: str = ""            # ecological / cultural notes
    two_eyed_seeing: str = ""    # relational + analytic explanation
    sources: List[str] = None    # SourceRef.id list


@dataclass
class MiKmawWord:
    english: str
    dialects: Dict[str, MiKmawWordDialect]  # e.g. {"general": MiKmawWordDialect}


# ---------- History Nodes ----------

@dataclass
class HistoryNode:
    id: str
    title: str
    era_label: str          # e.g. "Pre-contact", "Treaty Era", "Residential Schools"
    summary: str
    themes: List[str]
    key_figures: List[str]  # MiKmawFigure keys
    key_sources: List[str]  # SourceRef.id
    notes_for_two_eyed_seeing: str


# ---------- Seven Sacred Teachings ----------

@dataclass
class SacredTeaching:
    name: str
    animal_symbol: Optional[str]
    description: str


@dataclass
class SevenGenerationsModel:
    description: str
    past_seven: str
    future_seven: str
    warnings: str


# ---------- Homepage / Context ----------

@dataclass
class HomeContext:
    sources: Dict[str, SourceRef]
    figures: Dict[str, MiKmawFigure]
    history_nodes: Dict[str, HistoryNode]
    sacred_teachings: List[SacredTeaching]
    seven_generations: SevenGenerationsModel
    mi_kmaw_words: Dict[str, MiKmawWord]
    orthography_options: List[str]  # e.g. ["Smith-Francis", "Listuguj"]


# ---------- Helper ----------

def as_json_ready(obj) -> Dict[str, Any]:
    """Convert dataclass instance to a plain dict (for JSON export)."""
    return asdict(obj)


# ---------- Build Sources ----------

def build_sources() -> Dict[str, SourceRef]:
    return {
        "schmidt_marshall_1995": SourceRef(
            id="schmidt_marshall_1995",
            title="Mi'kmaq Hieroglyphic Prayers",
            details="Schmidt, D.L. & Marshall, M. 1995. Mi'kmaq Hieroglyphic Prayers.",
            url="https://nimbus.ca"  # placeholder
        ),
        "denny_fanning_netukulimk": SourceRef(
            id="denny_fanning_netukulimk",
            title="Netukulimk: Structures of Sustainability in the Mi'kmaw Language",
            details="Denny, J.P. & Fanning, S., on Mi'kmaw grammar and sustainability.",
            url="https://www.muiniskw.org/pgCulture4b.htm"
        ),
        "muiniskw_listuguj_orth": SourceRef(
            id="muiniskw_listuguj_orth",
            title="Listuguj Orthography Chart",
            details="Muin'iskw / Listuguj resources: vowel and consonant chart.",
            url="https://www.muiniskw.org/pgCulture4b.htm"
        ),
        "mk_apps_sfo": SourceRef(
            id="mk_apps_sfo",
            title="Mi'kmaw Language Apps (MK)",
            details="Mi'kmaw Kina'matnewey apps using Smith-Francis Orthography.",
            url="https://www.mk.ca"
        ),
        "rand_dictionary": SourceRef(
            id="rand_dictionary",
            title="Dictionary of the Language of the Micmac Indians",
            details="Rand, S.T. 1888 dictionary (Internet Archive).",
            url="https://archive.org/details/dictionaryoflang00rand"
        ),
        "paul_wwnts": SourceRef(
            id="paul_wwnts",
            title="We Were Not the Savages",
            details="Paul, D.N. 3rd ed. 2006, Fernwood Publishing.",
            url="https://www.danielnpaul.com"
        ),
        "marshall_two_eyed": SourceRef(
            id="marshall_two_eyed",
            title="Etuaptmumk / Two-Eyed Seeing",
            details="Elder Albert Marshall on bringing together Indigenous and Western knowledges.",
            url="https://www.integrativescience.ca"
        ),
        "mikmaq_language_overview": SourceRef(
            id="mikmaq_language_overview",
            title="Mi'kmaq Language Overview",
            details="General article on Mi'kmaw grammar and writing systems.",
            url="https://en.wikipedia.org/wiki/Mi%27kmaq_language"
        )
    }


# ---------- Core Figures ----------

def build_core_figures(sources: Dict[str, SourceRef]) -> Dict[str, MiKmawFigure]:
    figures = {}

    figures["membertou"] = MiKmawFigure(
        name="Grand Chief Membertou (Henri Membertou)",
        role="Grand Chief (Saqmaw), political and spiritual leader",
        life_dates="c.1507–1611",
        bio=(
            "Grand Chief near Port Royal during early French contact. Known as a "
            "warrior, spiritual leader, and diplomat who formed alliances with the French "
            "and was among the first chiefs baptized into Christianity."
        ),
        significance=(
            "Symbol of early Two-Eyed diplomacy: navigating Mi'kmaw spiritual leadership "
            "and French colonial power while trying to protect Mi'kma'ki."
        ),
        key_sources=["mikmaq_language_overview", "paul_wwnts"],
        image_url="/images/membertou.jpg"
    )

    figures["donald_marshall_jr"] = MiKmawFigure(
        name="Donald Marshall Jr.",
        role="Fisher, Treaty-Rights Defender, Catalyst for Legal Change",
        life_dates="1953–2009",
        bio=(
            "Wrongfully convicted of murder at 17, later exonerated. His Supreme Court "
            "case R. v. Marshall affirmed Mi'kmaw treaty rights to fish and sell catch "
            "for a moderate livelihood."
        ),
        significance=(
            "Embodies how colonial law can both harm and be forced to recognize Mi'kmaw "
            "rights. A Power-Tongue battlefield where treaties spoken in Mi'kmaw were "
            "interpreted through English legal logic."
        ),
        key_sources=["paul_wwnts"],
        image_url="/images/donald_marshall_jr.jpg"
    )

    figures["daniel_paul"] = MiKmawFigure(
        name="Daniel N. Paul",
        role="Author, Historian, Advocate",
        life_dates="1938–2024",
        bio=(
            "Mi'kmaw author of 'We Were Not the Savages', which retells Atlantic "
            "history from an Indigenous point of view and documents centuries of "
            "violence against the Mi'kmaq."
        ),
        significance=(
            "Provides a counter-archive to colonial histories and exposes how English "
            "print culture framed Mi'kmaw people as 'savages'."
        ),
        key_sources=["paul_wwnts"],
        image_url="/images/daniel_paul.jpg"
    )

    figures["albert_marshall"] = MiKmawFigure(
        name="Elder Albert Marshall",
        role="Elder, Co-creator of Etuaptmumk / Two-Eyed Seeing",
        life_dates="Eskasoni First Nation, contemporary",
        bio=(
            "Respected Elder from Eskasoni who articulated Two-Eyed Seeing, calling for "
            "the use of both Indigenous and Western knowledges for the benefit of all."
        ),
        significance=(
            "Provides the guiding principle for this project: hold Mi'kmaw relational "
            "knowledge in one eye and Western science/technology in the other."
        ),
        key_sources=["marshall_two_eyed"],
        image_url="/images/albert_marshall.jpg"
    )

    return figures


# ---------- Core Words (examples only – you can keep adding) ----------

def build_core_words(sources: Dict[str, SourceRef]) -> Dict[str, MiKmawWord]:
    words: Dict[str, MiKmawWord] = {}

    # Example: alder tree (tupsi)
    words["tupsi"] = MiKmawWord(
        english="alder tree",
        dialects={
            "general": MiKmawWordDialect(
                sf_orthography="tupsi",
                listuguj_orthography="tupsi",
                pronunciation_sfo="TUP-sih",
                pronunciation_lo="TUP-see",
                pronunciation_ipa="ˈtʊp.si",
                context=(
                    "Alder grows along rivers and wetlands. Provides wood for tools and "
                    "supports fish habitat and soil health."
                ),
                two_eyed_seeing=(
                    "In Relational Tongue, 'tupsi' is not a generic 'resource' but a "
                    "relative in the waterside ecosystem. In Power Tongue, it may appear "
                    "in forestry or engineering reports as a species name. Combining "
                    "both lets us manage rivers respectfully and scientifically."
                ),
                sources=["denny_fanning_netukulimk", "rand_dictionary"]
            )
        }
    )

    # Example: winter / it is winter – gesig / kesik
    words["winter"] = MiKmawWord(
        english="winter / it is winter",
        dialects={
            "general": MiKmawWordDialect(
                sf_orthography="gesg",
                listuguj_orthography="kesik",
                pronunciation_sfo="GESSK (with final g)",
                pronunciation_lo="KEH-sik",
                pronunciation_ipa=None,
                context=(
                    "Refers to the winter season; associated with snow, cold, and the "
                    "time of storytelling and reflection."
                ),
                two_eyed_seeing=(
                    "Relationally, winter is a teaching season: time to gather, heal, "
                    "and listen to stories. Analytically, it is defined by climate "
                    "data, temperature, and daylight. Together, they guide how we "
                    "prepare communities for changing winters under climate change."
                ),
                sources=["mikmaq_language_overview", "denny_fanning_netukulimk"]
            )
        }
    )

    # Example: everyday / every night from your app screenshots
    words["everyday"] = MiKmawWord(
        english="every day",
        dialects={
            "general": MiKmawWordDialect(
                sf_orthography="Te'sikiskik",
                listuguj_orthography=None,
                pronunciation_sfo="TEH-see-kiss-kik",
                context="Used for habits that happen each day.",
                two_eyed_seeing=(
                    "Carries a sense of ongoing rhythm, like the heartbeat of daily "
                    "life in a household or community."
                ),
                sources=["mk_apps_sfo"]
            )
        }
    )

    words["everynight"] = MiKmawWord(
        english="every night",
        dialects={
            "general": MiKmawWordDialect(
                sf_orthography="Te'sitpa'q",
                listuguj_orthography=None,
                pronunciation_sfo="TEH-sit-pak",
                context="Used for activities or conditions that occur each night.",
                two_eyed_seeing=(
                    "Links routine to the night world: stars, dreams, and night duties "
                    "such as checking the fire or nets."
                ),
                sources=["mk_apps_sfo"]
            )
        }
    )

    # Example: Poqnitpa'q (it is dark) and Aqtatpa'q (midnight)
    words["dark_midnight"] = MiKmawWord(
        english="it is dark at midnight",
        dialects={
            "general": MiKmawWordDialect(
                sf_orthography="Poqnitpa'q Aqtatpa'q",
                listuguj_orthography=None,
                pronunciation_sfo="BOHG-nit-pak AK-tat-pak",
                context=(
                    "Phrase built from 'it is dark' (Poqnitpa'q) and 'midnight' "
                    "(Aqtatpa'q)."
                ),
                two_eyed_seeing=(
                    "Names a moment in the nightly cycle. In relational terms, this may "
                    "be when certain animals move or ceremonies occur; in analytic "
                    "terms, it is 00:00 hours. Both lenses matter for navigation, "
                    "safety, and ceremony."
                ),
                sources=["mk_apps_sfo"]
            )
        }
    )

    return words


# ---------- Seven Sacred Teachings + Seven Generations ----------

def build_teachings() -> List[SacredTeaching]:
    return [
        SacredTeaching("Love", "Eagle", "Unconditional care for self, others, and creation."),
        SacredTeaching("Respect", "Buffalo", "Honouring all relations and their autonomy."),
        SacredTeaching("Courage", "Bear", "Facing fear with heart and integrity."),
        SacredTeaching("Honesty", "Sabe", "Speaking and living truthfully."),
        SacredTeaching("Wisdom", "Beaver", "Using knowledge for the good of all."),
        SacredTeaching("Humility", "Wolf", "Knowing you are part of the circle, not above it."),
        SacredTeaching("Truth", "Turtle", "Living all the teachings together every day.")
    ]


def build_seven_generations_model() -> SevenGenerationsModel:
    return SevenGenerationsModel(
        description=(
            "Seven Generations thinking remembers the seven generations behind us "
            "and plans for the seven generations ahead."
        ),
        past_seven=(
            "Ancestors who carried language, treaties, and land-based knowledge "
            "through colonization and attempted erasure."
        ),
        future_seven=(
            "Children not yet born who will inherit the consequences of our "
            "choices about land, water, and language revitalization."
        ),
        warnings=(
            "Greed, short-term profit, and ego can cut the thread between past "
            "and future generations."
        )
    )


# ---------- Build the Whole HomeContext ----------

def build_home_context() -> HomeContext:
    sources = build_sources()
    figures = build_core_figures(sources)
    words = build_core_words(sources)
    teachings = build_teachings()
    seven_gen = build_seven_generations_model()

    # history_nodes is left light so you can expand later
    history_nodes: Dict[str, HistoryNode] = {
        "precontact": HistoryNode(
            id="precontact",
            title="Ancient Mi'kma'ki",
            era_label="11,000+ years ago – pre-contact",
            summary=(
                "Mi'kmaw people living with the rhythm of the land and waters across "
                "Mi'kma'ki, with knowledge carried orally, in place names, and in art."
            ),
            themes=["land-based", "oral tradition", "place names"],
            key_figures=[],
            key_sources=["mikmaq_language_overview"],
            notes_for_two_eyed_seeing=(
                "Archaeology and geology offer one 'eye' on this era; oral history and "
                "ceremony offer the other."
            )
        ),
        "residential_schools": HistoryNode(
            id="residential_schools",
            title="Residential Schools and Language Suppression",
            era_label="19th–20th century",
            summary=(
                "Children taken to schools like Shubenacadie, punished for speaking "
                "Mi'kmaw. Many returned home with English dominant."
            ),
            themes=["language loss", "trauma", "survival"],
            key_figures=[],
            key_sources=["paul_wwnts"],
            notes_for_two_eyed_seeing=(
                "Power Tongue left a paper trail of policies and reports; Relational "
                "Tongue holds the lived stories of survivors and families."
            )
        )
    }

    return HomeContext(
        sources=sources,
        figures=figures,
        history_nodes=history_nodes,
        sacred_teachings=teachings,
        seven_generations=seven_gen,
        mi_kmaw_words=words,
        orthography_options=["Smith-Francis Orthography (S/F.O)", "Listuguj Orthography"]
    )


# ---------- Optional: a tiny CLI-style helper ----------

def explain_word(key: str, orthography_preference: str = "SFO") -> str:
    """
    Return a human-readable explanation of a Mi'kmaw word entry,
    choosing either Smith-Francis or Listuguj spelling when available.
    """
    home = build_home_context()
    word = home.mi_kmaw_words.get(key)
    if not word:
        return "Word not found in this small demo lexicon."

    dial = word.dialects["general"]

    if orthography_preference.upper().startswith("L"):
        spelling = dial.listuguj_orthography or dial.sf_orthography
        orth_label = "Listuguj"
    else:
        spelling = dial.sf_orthography or dial.listuguj_orthography
        orth_label = "Smith-Francis"

    return (
        f"English: {word.english}\n"
        f"{orth_label} spelling: {spelling}\n"
        f"Context: {dial.context}\n"
        f"Two-Eyed Seeing: {dial.two_eyed_seeing}\n"
    )
