import json
import dateutil.parser as parser
import re
from models import *
from db import db
from geopy.geocoders import Nominatim

geolocator = Nominatim()

def populateCountries(countries_json_data):

    with open(countries_json_data) as data_file:
          cjo = json.load(data_file)

    for c in cjo:
        #The other code breaks it because there are no relations, let alone meteorites, made yet. 
        meteorites_count = 0 #db.session.query(Meteorite).filter(Meteorite.country == c['name']).count()

        #this was never right, I think this may need to be done another way
        #largest_year = db.session.query(db.func.max(Meteorite.year))
        #recent_meteorite =  db.session(Meteorite).filter(Meteorite.year == largest_year).filter(Meteorite.year == c['name']).all()
        centroid = str(c['latlng'])
        n = len(centroid)
        #model creation
        country_model = Country(c['name'], c['area'], centroid[1:n-1], meteorites_count)
        db.session.add(country_model)
        db.session.commit()


def populateClassifications(classifications_json_data):
    with open(classifications_json_data) as data_file:
        cjo = json.load(data_file)

    for c in cjo:
        cmodel = Classification(c['name'], c['pclass'], c['composition'], c['origin'], 0)
        

        db.session.add(cmodel)
        db.session.commit()


def populateMeteorites(meteorites_json_data):
    with open(meteorites_json_data) as data_file:
        mjo = json.load(data_file)

    for m in mjo:
        lat = m['reclat']
        lng = m['reclong']
        clname = m['recclass']
        parsed_clname = parseClass(clname)
        geolocation = lat + ', ' + lng
        cname = locate(geolocation)

        country = countries.query.filter(Country.name ==  cname)
        classify = classifications.query.filter(Classification.name == parsed_clname)
        parsed_year = parseYear(m['year'])

        meteorite_model = Meteorite(m['name'], m['mass'], classify.name, parsed_year,
            country, lat, lng, geolocation, country_id, classification_id)

        country.meteorites.append(meteorite_model)
        classify.meteorites.append(meteorite_model)
        db.session.add(meteorite_model)
        db.session.commit()

def locate(geolocation):
    country = geolocator.reverse(geolocation, language ='en')
    country = country.address.split(',')
    return country[-1]

def parseYear(year):
    year_parsed = parser.parse(year).year
    return year_parsed

def parseClass(clname):
    parsed = re.sub("\d+", "", clname)
    return parsed

def createdb():
    db.drop_all()
    db.create_all()
    populateClassifications('classes.json')
    populateCountries('countries.json')
    populateMeteorites('meteorites.json')

createdb()
