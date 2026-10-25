import string
import re

def check_password_strength(password: str) -> str:

    if not password:
        return "Sehr schwach", 0

    score = 0

    # Punkte für Länge des Passworts

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Zeichenarten
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*()\-_=+\[\]{};:,.<>?/|]", password):
        score += 1

    # Bewertung
    if score <= 2:
        strength = "Schwach"
    elif score <= 4:
        strength = "Mittel"
    else:
        strength = "Stark"

    return strength