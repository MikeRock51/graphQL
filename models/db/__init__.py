#!/usr/bin/env python3
"""Defines Storage functions"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from typing import List, Dict
from os import path

DB_PATH = path.dirname(__file__) + '/storage.db'
print(DB_PATH)

class DB:
    """Defines the Database object"""
    __engine =None
    __session = None

    def __init__(self) -> None:
        """Creates a database engine"""
        self.__engine = create_engine(f'sqlite:///{DB_PATH}', echo=True)

    def reload(self) -> None:
        """Creates database tables if it doesn't
        exist and creates a new database session"""
        from models.baseModel import Base
        models = self.allModels()

        Base.metadata.create_all(self.__engine)
        SessionFactory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(SessionFactory)

    def add(self, obj) -> None:
        """Adds obj to the current db session"""
        self.__session.add(obj)

    def save(self) -> None:
        """Commits session state to database"""
        self.__session.commit()

    def delete(self, obj) -> None:
        """Deletes obj from the current session and commits the session state"""
        if obj:
            self.__session.delete(obj)
            self.save()

    def getByID(self, obj, id) -> None:
        """Fetches the cls instance that matches the id"""
        models = self.allModels()

        if obj in models.values():
            instance = self.__session.query(obj).filter(obj.id == id).one()

            return instance

    def allModels(self) -> Dict:
        """Returns a dictionary of all available models"""
        from models.user import User
        from models.post import Post
        return {
                "User": User,
                "Post": Post
        }

    def close(self) -> None:
        """Removes the current db session"""
        self.__session.close()
