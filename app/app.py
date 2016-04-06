#Module containing Flask application
from flask import Flask, send_file, send_from_directory, make_response, jsonify, json
from flask.ext.sqlalchemy import SQLAlchemy
import requests

#GOOGLE API KEY = AIzaSyCL_AcVa4WucI3grBntaNB7QGxTOQW_iMg
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)



#Flask handles API calls

#Returns a list of dictionaries, each of which contains information about a single meteorite
@app.route('/api/get_meteorites')
def get_meteorites():
    meteorites = requests.get('https://data.nasa.gov/resource/y77d-th95.json').json()

    #these are the only keys we care about.
    meteorite_keys = ['id', 'mass', 'name', 'year', 'reclong', 'recclass', 'reclat']
    m = []
    for meteorite in meteorites:
        meteorite = { meteorite_key : meteorite[meteorite_key] for meteorite_key in meteorite_keys if meteorite_key in meteorite}
        m.append(meteorite)

    return json.dumps(m)


@app.route('/api/get_meteorite/<id>')
def get_meteorite(id) :

    meteorite = requests.get('https://data.nasa.gov/resource/y77d-th95.json?id=' + id).json()
    id = str(meteorite[0]['id'])
    mass = str(meteorite[0]['mass'])
    name = str(meteorite[0]['name'])
    year = str(meteorite[0]['year'])
    classification = str(meteorite[0]['recclass'])
    #TODO: Determine country from geolocation
    #longitude = float(meteorite[0]['reclong'])
    #lattitude = float(meteorite[0]['reclat'])



    return jsonify(id = id, mass = mass, name = name, year = year, classification = classification )

@app.route('/api/get_classifications')
def get_classifications() :
    return 'classifcations'

@app.route('/api/get_classification/<id>')
def get_classification(id) :
    return 'class id'

@app.route('/api/get_countries')
def get_countries():
    countries = requests.get('http://knoema.com/api/1.0/data/observed-meteorite-falls-by-country').json()
    return str(list(countries))

@app.route('/api/get_country/<id>')
def get_country(id):
    return 'country id'



# Use Angular to do user/client routing
@app.route('/meteorites')
@app.route('/countries')
@app.route('/classifications')
@app.route('/about')
#@app.route('/<path:path>')
@app.route('/', defaults={'path': ''})
def index(**kwargs):
    return make_response(open('static/index.html').read())

if __name__ == '__main__':
    app.run(debug=True)