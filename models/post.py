#!/usr/bin/env python3
"""The Post Model"""

from models.baseModel import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Text


class Post(BaseModel, Base):
    """Defines a post object"""

    __tablename__ = "posts"

    title = Column(String(60), nullable=False)
    content = Column(Text, nullable=False)
    authorID = Column(String(60), ForeignKey('users.id'), nullable=False)
