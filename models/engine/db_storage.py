#!/usr/bin/python3

"""
Added new engine: DataBase Storage
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
from sqlalchemy.orm import scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization method"""
        user = os.environ['HBNB_MYSQL_USER']
        pas = os.environ['HBNB_MYSQL_PWD']
        host = os.environ['HBNB_MYSQL_HOST']
        db = os.environ['HBNB_MYSQL_DB']

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user,
                                              pas, host, db,
                                              pool_pre_ping=True))

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Returns a dictionary: a list of obj of one type
        """
         if cls:
            types = self.__session.query(cls).all()
        else:
            all_classes = [Amenity, City, Place, Review, State, User]
            types = []
            for cls in all_classes:
                types += self.__session.query(cls)
        my_dict = {}
        for obj in objects:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            my_dict[key] = obj
        return my_dict

    def new(self, obj):
        """
        Add object to current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commit object to current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Delete object to current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        Reload objects to current database session
        """
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine)
        Session = scoped_session(session_fact)
        self.__session = Session(expire_on_commit=False)

    def close(self):
        """
        Remove the method on the private session attribute
        """
        self.__session.close()
