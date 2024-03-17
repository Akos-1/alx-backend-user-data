#!/usr/bin/env python3

import logging
from typing import List
from filtered_datum import filter_datum


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"

    def __init__(self, fields: List[str]):
        format_str = f"[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
        super().__init__(format_str)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)
