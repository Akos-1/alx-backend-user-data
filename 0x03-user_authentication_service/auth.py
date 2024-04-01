#!/usr/bin/env python3

from db import DB
from user import User
from typing import Optional


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Register a new user.

        Args:
        - email: Email of the user.
        - password: Password of the user.

        Returns:
        - user: User object representing the registered user.

        Raises:
        - ValueError: If a user already exists with the passed email.
        """
        # Check if user with the email already exists
        try:
            existing_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except ValueError:
            pass  # User does not exist, proceed with registration

        # Hash the password
        hashed_password = self._hash_password(password)

        # Save the user to the database
        user = self._db.add_user(email, hashed_password)
        return user

    def _hash_password(self, password: str) -> bytes:
        """
        Hashes a password.

        Args:
        - password: Password string.

        Returns:
        - hashed_password: Bytes representing the hashed password.
        """
        # Hash the password using a secure hashing algorithm
        # For example, bcrypt can be used
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


if __name__ == "__main__":
    auth = Auth()
    auth.register_user("test@example.com", "password123")
