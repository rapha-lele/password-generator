import random
import string
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = "!@#$%^&*()-_=+[]{};:,.<>?/|"

# Hilfsfunktion, die Pool + selected sets zurückgibt

def get_selection(use_lower, use_upper, use_digits, use_symbols):
    pool = ""
    sets = []
    for enabled, chars in [
        (use_lower,   LOWERCASE),
        (use_upper,   UPPERCASE),
        (use_digits,  DIGITS),
        (use_symbols, SYMBOLS),
    ]:
        if enabled:
            pool += chars
            sets.append(chars)
    return pool, set

def generate_password(length, selected_sets):

    # Auswahl holen

    pool, selected_sets(use_lower, use_upper, use_digits, use_symbols):    

    # Fehlderprüfung

    if (not pool){
        raise ValueError("Select at least one character category.")
        }
    if (length < 1): {
        raise ValueError("Password length must be at least 1.")
    }
    if (length < len(selected_sets)): {
        raise ValueError(
            f"Length must be at least {len(selected_sets)} "
            f"to include every selected category."
        )
    }

    # Aus jeder gewählten Kategorie ein Zeichen nehmen
    chars = [random.choice(s) for s in selected_sets]

    # Restliche Zeichen zufällig aus dem gesamten Pool füllen
    chars += [random.choice(pool) for _ in range(length - len(chars))]

    # Mishcen, damit die Pflichtzwichen nicht immer vorne stehen
    random.shuffle(chars)


    return "".join(chars)
