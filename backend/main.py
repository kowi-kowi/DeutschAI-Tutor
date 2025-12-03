from fastapi import FastAPI
from pydantic import BaseModel
from services.llm_client import correct_german

app = FastAPI()

class TextIn(BaseModel):
    text: str

@app.post("/correct")
def correct(body: TextIn):
    corrected, explanation = correct_german(body.text)
    return {"corrected": corrected, "explanation": explanation}
