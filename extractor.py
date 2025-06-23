import json
import re

def clean_text(text):
    # Replace smart quotes
    text = text.replace("“", "\"").replace("”", "\"").replace("‘", "'").replace("’", "'")
    text = text.replace(u'\u00A0', ' ').replace(u'\u200B', '')
    return text.strip()

def extract_json(raw_text):
    try:
        raw_text = clean_text(raw_text)
        first_brace = raw_text.find('{')
        last_brace = raw_text.rfind('}')
        if first_brace != -1 and last_brace != -1:
            json_str = raw_text[first_brace:last_brace+1]
            return json.loads(json_str)
    except Exception as e:
        print("Extraction failed:", e)
    return None
