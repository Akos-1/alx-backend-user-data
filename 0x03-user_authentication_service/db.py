#!/usr/bin/env python3

"""
Module: db.py
This module provides the DB class for interacting with the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

from user import User

Base = declarative_base()


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Add a new user to the database.

        Args:
        - email: Email of the user.
        - hashed_password: Hashed password of the user.

        Returns:
        - user: User object representing the added user.
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        try:
            self._session.commit()
        except IntegrityError:
            self._session.rollback()
            raise ValueError("User with this email already exists in the database.")
        return user


if __name__ == "__main__":
    # Example usage
    db = DB()
    user = db.add_user("example@example.com", "hashed_password")
    print("User added:", user)
