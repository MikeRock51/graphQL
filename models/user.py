#!/usr/bin/env python3
"""The User Model"""

from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Defines a user object"""

    __tablename__ = "users"

    firstname = Column(String(128), nullable=False)
    lastname = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    age = Column(Integer, nullable=True)
    posts = relationship('Post', backref='author', cascade='all, delete')

    @property
    def fullname(self):
        """Returns users full name"""
        return f"{self.firstname} {self.lastname}"
