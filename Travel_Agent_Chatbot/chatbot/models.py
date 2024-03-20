from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from .database import Base

class TravelAgent(Base):
    __tablename__ = 'travel_agents'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    location = Column(String(255))
    packages = relationship('TravelPackage', back_populates='agent')

class TravelPackage(Base):
    __tablename__ = 'travel_packages'
    id = Column(Integer, primary_key=True, index=True)
    agent_id = Column(Integer, ForeignKey('travel_agents.id'))
    packagename = Column(String(255))
    description = Column(String(400))
    destination = Column(String(255))
    cost = Column(Float)
    origin_city_id = Column(Integer, ForeignKey('cities.id'))
    destination_city_id = Column(Integer, ForeignKey('cities.id'))
    valid_from = Column(DateTime)
    valid_to = Column(DateTime)
    origin_city = relationship("City", foreign_keys=[origin_city_id])
    destination_city = relationship("City", foreign_keys=[destination_city_id])
    agent = relationship('TravelAgent', back_populates='packages')

class City(Base):
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, index=True)
    Cityname = Column(String(255), index=True)
    country = Column(String(255))
    timezone = Column(String(255))
    airports = relationship("Airport", back_populates="city")

class Airport(Base):
    __tablename__ = "airports"
    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, ForeignKey('cities.id'))
    Airportname = Column(String(255))
    iata_code = Column(String(255), unique=True)
    city = relationship("City", back_populates="airports")

class Flight(Base):
    __tablename__ = "flights"
    id = Column(Integer, primary_key=True, index=True)
    departure_airport_id = Column(Integer, ForeignKey('airports.id'))
    arrival_airport_id = Column(Integer, ForeignKey('airports.id'))
    flight_duration = Column(Float)  # Flight duration in hours or minutes
    operating_airlines = Column(String(255))
    departure_airport = relationship("Airport", foreign_keys=[departure_airport_id])
    arrival_airport = relationship("Airport", foreign_keys=[arrival_airport_id])
