# models.py
from app import db
#from sqlalchemy import Metadata, Table, Column, Integer, String, Float, ForeignKey, create_engine
#from sqlalchemy.orm import sessionmaker, relationship
#from sqlalchemy.ext.declarative import declarative_base
from geopy.geocoders import Nominatim

#engine = create_engine('sqlite:///')
#session = sessionmaker()
#session.configure(bind=engine)

#Base = declarative_base()
geolocator = Nominatim()

class Meteorite(db.Model):

	"""
	Model for Meteorites, has an name mass, recclass, year, and country

	"""
	name = db.Column(db.String(50), primary_key=True)
	mass = db.Column(db.Float)
	recclass = db.Column(db.String(50))
	reclong = db.Column(db.Float)
	reclat = db.Column(db.Float)
	year = db.Column(db.Integer)
	geolocation = db.Column(db.String(50))
	
	#One to many relationship between Meteorites and Countries
	country = db.Column(db.String(50), db.ForeignKey('country.name'))

	#One to many relationship between Meteorites and Classifications
	recclass = db.Column(db.String(50), db.ForeignKey('classification.name'))

	def __init__(self, name = None, mass = 0, recclass = None, year = None, reclong = 0.0, reclat = 0.0):
		self.name = name
		self.mass = mass
		self.recclass = recclass
		self.year = year
		self.reclong = reclong
		self.reclat = reclat
		self.geolocation = str(reclat) + ', ' + str(reclong)
		self.country = locate(geolocation)

	def __repr__(self):
		return '<Meteorite %r>' % (self.name)

	def locate(geolocation):
		country = geolocator.reverse(geolocation, language ='en')
		country = country.address.split(',')
		return country[-1]


class Classification(db.Model):

	"""
	Model for Classification, has an id, compostion, parentBody,
	numberFound, and meteorites

	"""
	name = db.Column(db.String(50), primary_key = True)
	pclass = db.Column(db.String(50))
	composition = db.Column(db.String(50))
	origin = db.Column(db.String(50))
	numberFound = db.Column(db.Integer)

	#Many to one relationship btwn Classifications and Meteorites
	meteorites= db.relationship('Meteorite',backref='recclass', lazy='dynamic')

	def __init__(self, name = None, class_id = None, composition = None, parentBody = None):
		
		self.name = name
		self.parent_class = class_id
		self.composition = composition
		self.origin = parentBody
		self.numberFound = numberFound

	def __repr__(self):
		return '<Classification %r>' % (self.name)


class Country(db.Model):

	"""
	Model for Country, has an id_num, country, 
	earliestYear, and numberFound

	"""
	name = db.Column(db.String(50), primary_key=True)
	area = db.Column(db.Integer)
	centroid = db.Column(db.String(50))
	numberFound = db.Column(db.Integer)
	recent = db.Column(db.String(50))

	#Many to one relationship btwn Countries and Meteorites
	meteorites= db.relationship('Meteorite',backref='country', lazy='dynamic')

	def __init__(self, name, area = 0, centroid = "0.0, 0.0", recent= "None", numberFound = 0):
		self.name = name
		self.area = area 
		self.centroid = centroid
		self.recent = recent
		self.numberFound = numberFound

	def __repr__(self):
		return '<Country %r>' % (self.name)

	# def add_meteorite(meteorite):
	# 	country = geolocator.reverse(meteorite.geolocation, language ='en')
	# 	country = country.address.split(',')
	# 	name = country[-1]
	# 	exists = False
	# 	for loc in Country.getinstances():
	# 		if(loc.name == name):
	# 			exists = loc
	# 			break
	# 	if exists is not False:
	# 		exists.meteorites += meteorite
	# 		exists.set_recent(meteorite)
	# 	else:
	# 		exists = Country(name, meteorite)
	# 		session.add(exists)
	# 		session.commit()
	# 	return exists

	# def set_recent(meteorite):
	# 	if self.recent.year < meteorite.year:
	# 		self.recent = meteorite
