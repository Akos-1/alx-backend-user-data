#!/usr/bin/env python3

import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """Obfuscates log message fields based on specified fields and redaction character."""
    return re.sub(fr'\b(?:{"|".join(fields)})\b', redaction, message, flags=re.IGNORECASE)

class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super().__init__()
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)
