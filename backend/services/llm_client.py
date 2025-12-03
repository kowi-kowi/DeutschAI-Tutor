from transformers import pipeline

# mały model startowy (potem podmienisz)
generator = pipeline("text2text-generation", model="mrm8488/t5-base-finetuned-wikiSQL")

def correct_german(text: str):
    prompt = (
        "Popraw język niemiecki w zdaniu i wyjaśnij po polsku:\n"
        f"Tekst: {text}\n"
        "Format: POPRAWA | WYJAŚNIENIE\n"
    )
    result = generator(prompt, max_length=256)[0]["generated_text"]
    if "|" in result:
        corrected, explanation = result.split("|", 1)
    else:
        corrected, explanation = result, "Brak wyjaśnienia"
    return corrected.strip(), explanation.strip()
