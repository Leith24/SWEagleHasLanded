import json
from models import *
from db import db

def populateMeteorites(meteorites_json_data):
    meteorites_json_object = json.load(meteorites_json_data)

    for ind_meteorite in meteorites_json_object:
        meteorite_model = Meteorite(ind_meteorite['name'], ind_meteorite['mass'], ind_meteorite['recclass'], ind_meteorite['year'], ind_meteorite['reclat'], ind_meteorite['reclong'])
        db.session.add(meteorite_model)
        db.session.commit()

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
        classifications_model = Classification(ind_classifications, ind_classifications['Class_ID'], ind_classifications['Compositional_Type'], ind_classifications[''])
        db.session.add(classifications_model)
        db.session.commit()

def create_tracks_album(countries_json_data):

    countries_json_object = json.load(countries_json_data)
    for country in countries_json_object:
        for meteorite_model in Meteorite.query.filter(Meteorite.country == country['name']):
            if meteorite_model == None:
                i=1
            else:
                for track in album['tracks']['items']:
                    artist_name=''
                    count=0
                    for artist in track['artists']:
                        if count >=1:
                            artist_name+=', '
                        artist_name+=artist['name']
                        count=count+1
                    track_exist= Track.query.filter(Track.title == track['name']).first()
                    if track_exist ==None:

                        tracks_model=Track(track['name'],artist_name,album_db.release_date,album_db.name,album_db.images,track['duration_ms'],track['uri'],track['id'],album_db.id,album_db.col_img,track['href'])
                        artist_in_track= re.split(', ', artist_name)
                        for art_tr in artist_in_track:
                            artist= Artist.query.filter(Artist.name == art_tr).first()
                            if artist ==None:
                                i=1
                            else:
                                tracks_model.artists2.append(artist)
                        db.session.add(tracks_model)
                        db.session.commit()


populateMeteorites('meteorites.json')
populateCountries('countries.json')
populateClassifications('classes.json')
