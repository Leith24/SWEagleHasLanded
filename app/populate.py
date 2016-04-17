import json
import dateutil.parser as parser
import re
from models import Country, Meteorite, Classification
from db import db


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
        mass = m['mass']
        lat = m['reclat']
        lng = m['reclong']
        cname = m['cname']
        clname = m['recclass']
        geolocation = m['geolocation']
        parsed_clname = parseClass(clname)
        # print (cname + ' = cname after locating')
        #print(parsed_clname)
        classify = Classification.query.filter(Classification.name == parsed_clname).first()
        #print(classify.name)
        if "Atlas Buoy" in cname or "Grande Terre" in cname or "Europe" == cname:
            continue
        elif "United States" == cname or "India"  == cname:
            country = Country.query.filter(Country.name == cname).first()
        else:
            country = Country.query.filter(Country.name.contains(cname)).first()
        # print(country.name + ' = country.name ')
        parsed_year = parseYear(m['year'])
        print(cname)
        meteorite_model = Meteorite(name, mass, classify.name, parsed_year, country.name, lat, lng, geolocation)

        country.meteorites.append(meteorite_model)
        classify.meteorites.append(meteorite_model)
        db.session.add(meteorite_model)
        db.session.commit()

def populateRelations():
    for c in Country.query.all():
        #recent
        recent = db.session.query(Meteorite).filter(Meteorite.cname == c.name).order_by(Meteorite.year).first()
        if recent:
            c.recent = recent.name
        else: 
            c.recent = 'None'
        #num found
        num = c.meteorites.count()
        c.numberFound = num
        db.session.commit()
    for c in Classification.query.all():
        num = c.meteorites.count()
        c.numberFound = num
        db.session.commit()

def parseYear(year):
    year_parsed = parser.parse(year).year
    return int(year_parsed)

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

def createdb():
    db.drop_all()
    db.create_all()
    populateClassifications('classes.json')
    populateCountries('countries.json')
    populateMeteorites('meteorites.json')
    populateRelations()

if __name__ == '__main__':
    createdb()
