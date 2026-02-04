import spacy
nlp = spacy.load("en_core_web_sm")

def scrub_pii(text: str) -> str:
    """
    Function signature mah 'text: str' xa. 
    Yesle Pydantic object bata aayeko string lai process garxa.
    """
    doc = nlp(text)
    scrubbed_text = text
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "GPE", "ORG"]:
            scrubbed_text = scrubbed_text.replace(ent.text, f"[{ent.label_}]")
    return scrubbed_text