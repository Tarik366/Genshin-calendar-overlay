import json

default_settings = {
    "Server": "Europe",
    "Language": "Turkish"
}

CJK_FONTS = [
    "Korean",
    "Korean (Korea)",
    "Japanese",
    "Japanese (Japan)",
    "Chinese",
    "Chinese (S)",
    "Chinese (Hong Kong)",
    "Chinese (Macau)",
    "Chinese (Singapore)", 
    "Chinese (T)",
]

def get_locale_code(lang):
    with open("BCP47.json", "r", encoding="utf-8") as file:
        js = json.load(file)
        return js[0][lang]