# api.py

from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional, Literal

from translator import Translator, InputType, OrthPref

app = FastAPI(title="L'nui'suti Two-Eyed Translator")

translator = Translator()


class TranslateResponse(BaseModel):
    key: str
    english: str
    sfo_spelling: Optional[str]
    lo_spelling: Optional[str]
    context: str
    two_eyed_seeing: str
    sources: list


@app.get("/translate", response_model=Optional[TranslateResponse])
def translate(
    q: str = Query(..., description="Word to look up (Mi'kmaw or English)"),
    input_type: InputType = Query("auto", description="auto | mikmaw | english"),
    orth: OrthPref = Query("SFO", description="SFO | LO | BOTH")
):
    """
    Word-level Two-Eyed translator endpoint.

    Example:
      /translate?q=tupsi&input_type=mikmaw&orth=SFO
      /translate?q=winter&input_type=english&orth=BOTH
    """
    result = translator.translate_word(q, input_type=input_type, orthography=orth)
    if result is None:
        return None
    return TranslateResponse(**result)
