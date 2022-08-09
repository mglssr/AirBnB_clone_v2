#!/usr/bin/python3
""" State Module for HBNB project """


from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref ="state",
                          cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """getter attribute cities that returns the
        list of City instances with state_id"""
        list_cities = []
        for city in storage.all("City").value():
            if city.state_id == self.id:
                list_cities.append(city)
        return list_cities
