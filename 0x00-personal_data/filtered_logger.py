#!/usr/bin/env python3

import logging
from logging import StreamHandler
from filtered_logger import RedactingFormatter

PII_FIELDS = ("name", "email", "phone", "ssn", "credit_card")

def get_logger():
    """Return a logging.Logger object with specified configurations."""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    
    handler = StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    
    logger.addHandler(handler)
    
    return logger

if __name__ == "__main__":
    # Test the logger
    logger = get_logger()
    logger.info
