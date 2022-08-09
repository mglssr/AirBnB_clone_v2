#!/usr/bin/python3
"""
    Define class DatabaseStorage
"""
from os import getenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
import models
from models.state import State
from models.city import City
from models.base_model import Base
from sqlalchemy.orm import Session

class DBStorage:
    """
    Db
    """
    __engine = None
    __session = None


    def __init__(self):
        """
        engine must be linked to the MySQL database
        """
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        envv = getenv("HBNB_ENV", "none")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      user, pwd, host, db), pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        
        if envv == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        query on the current database session
        """
        classes = [BaseModel, User, Place, State, City, Amenity, Review]
        obj_dict = {}
        if cls is not None:
            for obj in self.__session.query(cls).all():
                obj_dict[f"{cls}.{obj.id}"] = obj
        else:
            for clas in classes:
                for obj in self.__session.query(clas).all():
                    obj_dict[f"{clas}.{obj.id}"] = obj 
        return obj_dict
        

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        reload
        """
        self.__session = Base.metadata.create_all(self.__engine)
        f = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(f)
        self.__session = Session()
