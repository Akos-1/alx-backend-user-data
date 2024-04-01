#!/usr/bin/env python3

"""
Module: models.py
This module defines the SQLAlchemy model for the User table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy model for the User table.

    Attributes:
    - id: The integer primary key
    - email: A non-nullable string
    - hashed_password: A non-nullable string
    - session_id: A nullable string
    - reset_token: A nullable string
    """

    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String, nullable=False)
    hashed_password: str = Column(String, nullable=False)
    session_id: str = Column(String, nullable=True)
    reset_token: str = Column(String, nullable=True)
