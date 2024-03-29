#!/usr/bin/env python3

import bcrypt

def hash_password(password: str) -> bytes:
    """Hashes the input password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def is_valid(hashed_password: bytes, password: str) -> bool:
    """Validates the provided password against the hashed
    password using bcrypt."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
