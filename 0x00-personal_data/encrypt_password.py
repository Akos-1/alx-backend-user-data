#!/usr/bin/env python3

import bcrypt

def hash_password(password: str) -> bytes:
    """Hashes the input password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
