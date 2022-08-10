#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
from os import getenv

metadata = Base.metadata

place_amenity = Table('place_amenities', metadata, Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False), Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                           cascade="all, delete, delete-orphan")
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False, overlaps = "place_amenities")

    else:
        @property
        def reviews(self):
            """reviews getter"""
            list_review = []
            for review in models.storage.all("Review").value():
                if review.state_id == self.id:
                    list_review.append(review)
            return list_review
        @property
        def amenities(self):
            """amenities getter"""
            list_amenities = []
            for amenity in models.storage.all("Amenity").value():
                if amenity.id == self.id:
                    list_amenities.append(ameinity)
                return list_amenities
        
        @amenities.setter
        def amenities(self):
            """amenities setter"""
            amenity_ids = []
            for amenity in models.storage.all("Amenity").value():
                amenity_ids.append(amenity.id)

