# analyzer.py
import string
def analyze_password(password, weak_list):
    """
    Analyze a single password and return:
    - status ("VERY WEAK", "WEAK", "MEDIUM", "STRONG")
    - reasons list
    - suggestions list
    """

    reasons = []
    suggestions = []
    password_lower = password.lower()

    if password_lower in weak_list:
        reasons.append("Password is in weak dictionary list")
        suggestions.append("Pick a completely different password")

    if len(password) < 8:
        reasons.append(f"Too short: only {len(password)} characters")
        suggestions.append("Make password at least 10 characters")

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    if not has_upper:
        suggestions.append("Add uppercase letters")
    if not has_lower:
        suggestions.append("Add lowercase letters")
    if not has_digit:
        suggestions.append("Add digits")
    if not has_symbol:
        suggestions.append("Include symbols like !@#$%^&*")

    if password_lower in weak_list:
        status = "VERY WEAK"
    elif len(password) < 8:
        status = "WEAK"
    elif (has_upper + has_lower + has_digit + has_symbol) >= 3:
        status = "STRONG"
    else:
        status = "MEDIUM"

    suggestions = list(dict.fromkeys(suggestions))

    return status, reasons, suggestions
