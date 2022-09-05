#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name=""

    @property
    def cities(self):
        """getter attribute cities that returns the
        list of City instances with state_id"""
        list_cities = []
        list_obj = models.storage.all(City)
        for city in list_obj.values():
            if city.state_id == self.id:
                list_cities.append(city)
        return list_cities
