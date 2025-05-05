CRISIS_KEYWORDS = ["kill myself", "end it all", "suicidal", "no point"]

def check_for_crisis(text):
    for word in CRISIS_KEYWORDS:
        if word in text.lower():
            return True
    return False
