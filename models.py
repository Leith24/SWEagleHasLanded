# models.py

from sqlalchemy import MetaData, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from geopy.geocoders import Nominatim

Base = declarative_base()
geolocator = Nominatim()

class Meteorite(Base):

	"""
	Model for Meteorites, has an id, mass, recclass, fall,
	name, year, and country

	"""
	__tablename__ = 'meteorite'
	_instances = set()

	id_num = Column(Integer, primary_key=True)
	mass = Column(Integer)
	recclass = Column(String(50))
	fall = Column(String(10))
	name = Column(String(50), unique=True)
	year = Column(String)
	country = Column(String)

	def __init__(self, id_num, mass = 0, recclass = None, name = None, year = None, reclong = 0.0, reclat = 0.0):
		self.name = name
		self._instances.add(weakref.ref(self))
		self.mass = mass
		self.recclass = Classification.get(recclass)
		self.year = year
		self.reclong = reclong
		self.reclat = reclat
		self.geolocation = str(reclat) + ', ' + str(reclong)
		self.country = country.addMeteorite(self)

	def __repr__(self):
		return '<Meteorite %r>' % (self.name)

	@classmethod
	def getinstances(cls):
		dead = set()
		for ref in cls._instances:
			obj = ref()
			if obj is not None:
				yield obj
			else:
				dead.add(ref)
		cls._instances -= dead

class Classification(Base):

		"""
	Model for Classification, has an id, compostion, parentBody,
	numberFound, and meteorites

	"""
	__tablename__ = 'Classifications'
	_instances = set()

	id_num = Column(Integer, primary_key = True)
	name = Column(String)
	composition = Column(String)
	parentBody = Column(String)
	numberFound = Column(Integer)
	meteorites = Column(String)

	def __init__(self, name = None, compositionalType = None, parentBody = None):
		self.name = name
		self._instances.add(weakref.ref(self))
		self.composition = compositionalType
		self.parentBody = parentBody
		self.numberFound = numberFound
		self.meteorites = []


	def __repr__(self):
		return '<Classification %r>' % (self.name)

	@classmethod
	def getinstances(cls):
		dead = set()
		for ref in cls._instances:
			obj = ref()
			if obj is not None:
				yield obj
			else:
				dead.add(ref)
		cls._instances -= dead


class Country(Base):

	"""
	Model for Country, has an id_num, country, 
	earliestYear, and numberFound

	"""
	__tablename__ = 'Countries'
	_instances = set()

	id_num = Column(Integer, primary_key=True)
	country = Column(String)
	earliestYear = Column(Integer)
	numberFound = Column(Integer)

	def __init__(self, name = None, area = 0, centroid = "0.0, 0.0", meteorite = None):
		self.name = name
		self._instances.add(weakref.ref(self))
		self.area = area #api call goes here
		self.centorid = centroid
		self.meteorites = [meteorite]
		numberFound =  len(meteorites)

	def __repr__(self):
		return '<Country %r>' % (self.Country)

	@classmethod
	def getinstances(cls):
		dead = set()
		for ref in cls._instances:
			obj = ref()
			if obj is not None:
				yield obj
			else:
				dead.add(ref)
		cls._instances -= dead

	def add_meteorite(meteorite):
		country = geolocator.reverse(meteorite.geolocation, language ='en')
		country = country.address.split(',')
		name = country[-1]
		exists = False
		for loc in Country.getinstances():
			if(loc.name == name):
				exists = loc
				break
		if exists is not False:
			exists.meteorites += meteorite
		else:
			exists = Country(name, meteorite)
			session.add(exists)
			session.commit()
		return exists
