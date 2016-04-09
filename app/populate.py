import json
import dateutil.parser as parser
import re
from models import Country, Meteorite, Classification
from db import db
from geopy.geocoders import Nominatim

geolocator = Nominatim()

def populateCountries(countries_json_data):

    with open(countries_json_data) as data_file:
          cjo = json.load(data_file)

    for c in cjo:
        centroid = str(c['latlng'])
        n = len(centroid)
        country_model = Country(c['name'], c['area'], centroid[1:n-1], 'None', 0)
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
        name = m['name']
        print(name)

        mass = m['mass']
        lat = m['reclat']
        lng = m['reclong']
        clname = m['recclass']
        parsed_clname = parseClass(clname)
        geolocation = lat + ', ' + lng
        cname = locate(geolocation)
        cname = parseCname(cname)
        #print (cname)
        #print(parsed_clname)
        classify = Classification.query.filter(Classification.name == parsed_clname).first()
        #print(classify.name)
        if "Atlas Buoy" in cname or "Grande Terre" in cname or "Europe" == cname:
            continue
        elif "United States" == cname or "India" == cname:
            country = Country.query.filter(Country.name == cname)
        else
            country = Country.query.filter(Country.name.contains(cname)).first()
        #print(country.name)
        parsed_year = parseYear(m['year'])
        meteorite_model = Meteorite(name, mass, classify.name, parsed_year, country.name, lat, lng, geolocation)

        country.meteorites.append(meteorite_model)
        classify.meteorites.append(meteorite_model)
        db.session.add(meteorite_model)
        db.session.commit()

def populateRelations():
    for c in Country:
        #recent
        recent = session.query(c.meteorites, db.func.max(Meteorite.year))
        c.recent = recent.name
        #num
        num = session.query(c.meteorites).count()
        c.numberFound = num
        db.session.commit()
    for c in Classification:
        num = session.query(c.meteorites).count()
        c.numberFound = num
        db.session.commit()


def locate(geolocation):
    country = geolocator.reverse(geolocation, language ='en')
    country = country.address.split(',').strip(' ')
    return country[-1]

def parseYear(year):
    year_parsed = parser.parse(year).year
    return year_parsed

def parseClass(clname):
    parsed = re.sub("\d+", "", clname)
    parsed = parsed.partition("-")[0]
    parsed = parsed.partition("/")[0]
    parsed = re.sub("\.", "", parsed)
    parsed = re.sub("\?", "", parsed)
    if parsed == 'Martian (chassignite)':
        parsed = 'Chassignites'
    if parsed == 'Martian (nakhlite)':
        parsed = 'Nakhlites'
    if parsed == 'Martian (shergottite)':
        parsed = 'Shergottites'
    if parsed == 'Iron, IIF':
        parsed = 'Iron, ungrouped'
    return parsed

def parseCname(cname):
    if cname == 'Congo-Kinshasa':
        cname = 'Democratic Republic of the Congo'
    elif cname == 'United States of America':
        cname = 'United States'
    elif cname == 'Russian Federation':
        cname = 'Russia'
    elif cname == 'RSA':
        cname = 'South Africa'
    elif cname == 'The Netherlands':
        cname = 'Netherlands'
    elif cname == 'Islamic Republic of Iran':
        cname = 'Iran'
    return cname

def createdb():
    db.drop_all()
    db.create_all()
    populateClassifications('classes.json')
    populateCountries('countries.json')
    populateMeteorites('meteorites.json')
    populateRelations()

createdb()
