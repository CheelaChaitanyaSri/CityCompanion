# security.py - Security System

import re
import logging
from datetime import datetime

logging.basicConfig(filename="security_events.txt", level=logging.INFO)

def detect_misuse(user_input: str) -> bool:
    """
    Detects unsafe or spammy patterns in user input.
    """
    spam_patterns = [
        r"(http|www)\S+",       # suspicious links
        r"(free money|click here|win big)",  # spammy phrases
        r"(hack|cheat|illegal)" # unsafe terms
    ]

    for pattern in spam_patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            log_event("Misuse detected", user_input)
            return True

    return False

def log_event(event: str, details: str):
    """
    Logs security events with timestamp.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"[{timestamp}] {event} – {details}")
