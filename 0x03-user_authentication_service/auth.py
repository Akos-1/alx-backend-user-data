#!/usr/bin/env python3

"""
Module: db.py
This module provides the DB class for interacting
with the database.
"""

import bcrypt


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        # Your initialization code here
        pass

    # Existing code...

    def _hash_password(self, password: str) -> bytes:
        """
        Hashes a password using bcrypt.

        Args:
        - password: The password string to hash.

        Returns:
        - hashed_password: Bytes representing the salted
        hash of the input password.
        """
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password


if __name__ == "__main__":
    # Example usage
    db = DB()
    password = "example_password"
    hashed_password = db._hash_password(password)
    print("Hashed Password:", hashed_password)
