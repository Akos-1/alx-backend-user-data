#!/usr/bin/env python3

"""
Module: db.py
This module provides the DB class for interacting with the database.
"""

from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm.exc import NoResultFound

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

    def find_user_by(self, **kwargs) -> User:
        """
        Find a user by the provided filter criteria.

        Args:
        - kwargs: Arbitrary keyword arguments representing filter criteria.

        Returns:
        - user: User object found by the filter criteria.

        Raises:
        - NoResultFound: If no user is found based on the provided filter criteria.
        - InvalidRequestError: If wrong query arguments are passed.
        """
        try:
            user = self._session.query(User).filter_by(**kwargs).first()
            if not user:
                raise NoResultFound("No user found for the given criteria.")
            return user
        except InvalidRequestError as e:
            raise InvalidRequestError("Invalid query arguments.") from e


if __name__ == "__main__":
    # Example usage
    db = DB()
    user = db.add_user("example@example.com", "hashed_password")
    print("User added:", user)
