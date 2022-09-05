#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey("places.id"),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """
    place
    """
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
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", cascade="all, delete-orphan",
                               backref='place')
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="places", viewonly=False)
    else:
        city_id = ""
        user_id = ""

        @property
        def reviews(self):
            """
            reviews
            """
            reviewsList = []
            for review in models.storage.all(Review).values():
                if self.id == review.place_id:
                    reviewsList.append(models.storage.all(Review)[review])
            return reviewsList

        @property
        def amenities(self):
            """
            amenities
            """
            amenityList = []
            for amenity in models.storage.all(Amenity).values():
                if self.id == amenity.place_id:
                    amenityList.append(models.storage.all(Amenity)[amenity])
            return amenityList

        @amenities.setter
        def amenities(self, amenity_object):
            if type(amenity_object).__name__ == "Amenity":
                self.amenity_ids.append(amenity_object.id)
