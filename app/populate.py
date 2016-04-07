import json
from models import *
from app import db

def populateMeteorites(meteorites_json_data):
    json_object = json.load(meteorites_json_data)

    for ind_meteorite in json_object:
        meteorite_model = Meteorite(ind_meteorite['name'], ind_meteorite['id'], ind_meteorite['recclass'], ind_meteorite['year'], ind_meteorite['reclong'], ind_meteorite['reclat'])
        db.session.add(meteorite_model)
        db.session.commit()

def populateCountries(countries_json_data):
    json_object = json.load(countries_json_data)

    for ind_country in json_object:
        #queries
        meteorites_count = db.session.query(Meteorite).filter(Meteorite.country == ind_country['name']).count()

        largest_year = db.session.query(db.func.max(Meteorite.year))
        recent_meteorite = db.session(Meteorite).filter(Meteorite.year == largest_year).filter(Meteorite.year == ind_country['name']).all()

        #model creation
        country_model = Country(ind_country['name'], ind_country['area'], ind_country['latlng'], recent_meteorite, meteorites_count)
        db.session.add(country_model)
        db.session.commit()


def populateClassifications(classifications_json_data):
    json_object = json.load(classifications_json_data)

    for ind_classifications in json_object:
        classifications_model = Classification()

