# models.py

from sqlalchemy import MetaData, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Meteorite(Base):
	__tablename__ = 'meteorite'

	id = Column(Integer, primary_key=True)
	mass = Column(Integer)
	nametype = Column(String(50))
	recclass = Column(String(50))
	fall = Column(String(10))
	name = Column(String(50), unique=True)
	year = Column(String)
	reclong = Column(Float)
	reclat = Column(Float)

	def __init__(self, mass = 0, nametype = None, recclass = None, 
	fall = None, name = None, year = None, reclong = 0.0, reclat = 0.0):
		self.mass = mass
		self.nametype = nametype
		self.recclass = recclass
		self.fall = fall
		self.name = name
		self.year = year
		self.reclong = reclong
		self.reclat = reclat

	def __repr__(self):
		return '<Meteorite %r>' % (self.name)


class Classifications(Base):
	__tablename__ = 'Classifications'

	id = Column(Integer, primary_key = True)
	name = Column(String)
	compositionalType = Column(String)
	parentBody = Column(String)
	numberFound = Column(Integer)

	def __init__(self, name = None, compositionalType = None, parentBody = None,
	 numberFound = 0):
		self.name = name
		self.compositionalType = compositionalType
		self.parentBody = parentBody
		self.numberFound = numberFound

	def __repr__(self):
		return '<Classifications %r>' % (self.name)

class Location(Base):
	__tablename__ = 'Location'

	id = Column(Integer, primary_key=True)
	country = Column(String)
	earliestYear = Column(Integer)
	lowestLong = Column(Float)
	lowestLat = Column(Float)
	highestLong = Column(Float)
	highestLat = Column(Float)

	def __init__(self, country = None, earliestYear = 0, lowestLat = 0.0,
	lowestLong = 0.0, highestLat = 0.0, highestLong = 0.0):
		self.country = country
		self.earliestYear = earliestYear
		self.lowestLong = lowestLong
		self.lowestLat = lowestLat
		self.highestLong = highestLong
		self.highestLat = highestLat

	def __repr__(self):
		return '<Location %r>' % (self.country)
	
		
