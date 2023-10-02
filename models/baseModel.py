#!/usr/bin/env python3
"""Base model inheritted by other models"""

from uuid import uuid4
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, DateTime 
from datetime import datetime
from copy import copy
from models import storage
from typing import Dict


Base = declarative_base()

class BaseModel:
    """Defines common attributes and methods between models"""
    id = Column(String(60), primary_key=True, default=str(uuid4), nullable=False)
    createdAt = Column(DateTime, default=datetime.utcnow, nullable=False)
    updatedAt = Column(DateTime, default=datetime.utcnow, nullable=False)


    def str(self) -> str:
        """Returns a string representation of an instance"""
        return f"<{type(self).__name__}>"

    def toDict(self) -> Dict:
        """Returns a dictionary representation of an instance"""
        instance = copy(self.__dict__)
        instance['createdAt'] = instance['createdAt'].toisoformat()
        instance['updatedAt'] = instance['updateAt'].toisoformat()
        instance['__class__'] = type(self).__name__

        if instance['_sa_instance_state']:
            instance.pop('_sa_instance_state')

        return instance

    def save(self) -> None:
        """Saves the current instance to database"""
        storage.add(self)
        storage.save()
