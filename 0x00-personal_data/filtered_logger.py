#!/usr/bin/env python3

import logging
from logging import StreamHandler
import re
from typing import List
from filtered_logger import RedactingFormatter

PII_FIELDS = ("name", "email", "phone", "ssn", "password")

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

def get_logger():
    """Return a logging.Logger object with specified configurations."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    
    handler = StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    
    logger.addHandler(handler)
    
    return logger

def main():
    """Obtain a database connection, retrieve and display filtered rows from the users table."""
    logger = get_logger()
    # Assuming get_db is implemented elsewhere to obtain a database connection
    # and retrieve all rows in the users table
    db_connection = get_db()
    users = db_connection.get_users()
    for user in users:
        logger.info(f"name={user['name']}; email={user['email']}; phone={user['phone']}; ssn={user['ssn']}; password={user['password']}; ip={user['ip']}; last_login={user['last_login']}; user_agent={user['user_agent']};")


if __name__ == "__main__":
    main()
