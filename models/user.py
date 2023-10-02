#!/usr/bin/env python3
"""The User Model"""

from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String, Integer


class User(BaseModel, Base):
    """Defines a user object"""
    __tablename__ = "users"

    firstname = Column(String(128), nullable=False)
    lastname = Column(String(128), nullable=False)
    age = Column(Integer, nullable=True)
