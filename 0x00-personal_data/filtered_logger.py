#!/usr/bin/env python3

import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates log message fields based on specified fields
    and redaction character.

    Arguments:
    fields: List of strings representing fields to obfuscate.
    redaction: String representing the character used for obfuscation.
    message: String representing the log line.
    separator: String representing the character
    separating fields in the log line.

    Returns:
    String: Log message with specified fields obfuscated.
    """
    return re.sub(fr'\b(?:{"|".join(fields)})\b', redaction, message, flags=re.IGNORECASE)
