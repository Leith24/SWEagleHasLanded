import json
import dateutil.parser as parser
import re
from models import *
from db import db
from geopy.geocoders import Nominatim

geolocator = Nominatim()

def populateCountries(countries_json_data):
    countries_json_object = json.load(countries_json_data)

    for ind_country in countries_json_object:
        #queries
        meteorites_count = db.session.query(Meteorite).filter(Meteorite.country == ind_country['name']).count()

        largest_year = db.session.query(db.func.max(Meteorite.year))
        recent_meteorite = db.session(Meteorite).filter(Meteorite.year == largest_year).filter(Meteorite.year == ind_country['name']).all()

        #model creation
        country_model = Country(ind_country['name'], ind_country['area'], ind_country['latlng'], recent_meteorite, meteorites_count)
        db.session.add(country_model)
        db.session.commit()


def populateClassifications(classifications_json_data):
    class_json_object = json.load(classifications_json_data)

    for ind_classifications in class_json_object:
        classifications_model = Classification(ind_classifications['name'], ind_classifications['pclass'],
        ind_classifications['composition'], ind_classifications['origin'])
        db.session.add(classifications_model)
        db.session.commit()


def populateMeteorites(meteorites_json_data):
    meteorites_json_object = json.load(meteorites_json_data)

    for ind_meteorite in meteorites_json_object:
        lat = ind_meteorite['reclat']
        lng = ind_meteorite['reclong']
        clname = ind_meteorite['recclass']
        parsed_clname = parseRecclass(clname)
        geolocation = lat + ', ' + lng
        cname = locate(geolocation)
        country = countries.query.filter(Country.name ==  cname)
        classify = classifications.query.filter(Classification.name == parsed_clname)
        parsed_year = parseYear(ind_meteorite['year'])

        meteorite_model = Meteorite(ind_meteorite['name'], ind_meteorite['mass'], classify, parsed_year,
            country, lat, lng, geolocation)
        db.session.add(meteorite_model)
        db.session.commit()

def locate(geolocation):
    country = geolocator.reverse(geolocation, language ='en')
    country = country.address.split(',')
    return country[-1]

def parseYear(year):
    year_parsed = parser.parse(year).year
    return year_parsed

def parseRecclass(recclass):
    recclass_parsed = re.sub("\d+", "", recclass)
    return recclass_parsed


populateCountries('countries.json')
populateClassifications('classes.json')
populateMeteorites('meteorites.json')