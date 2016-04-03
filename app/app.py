#Module containing Flask application
from flask import Flask, send_file, send_from_directory, make_response, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import requests

#GOOGLE API KEY = AIzaSyCL_AcVa4WucI3grBntaNB7QGxTOQW_iMg
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)



#Flask handles API calls
@app.route('/api/get_meteorites')
def get_meteorites() :
    #TODO: refine GET to only return relevant data
    #meteorites = requests.get('https://data.nasa.gov/resource/y77d-th95.json').json()

    #meteorite = requests.get('https://data.nasa.gov/resource/y77d-th95.json?id=' + id).json()
    #id = str(meteorite[0]['id'])
    #mass = str(meteorite[0]['mass'])
    #name = str(meteorite[0]['name'])
    #year = str(meteorite[0]['year'])
   # classification = str(meteorite[0]['recclass'])
    #TODO: Determine country from geolocation
    #longitude = float(meteorite[0]['reclong'])
    #lattitude = float(meteorite[0]['reclat'])

    return 'meteorites'

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
def get_countries() :
    return 'country'

@app.route('/api/get_country/<id>')
def get_country(id) :
    return 'country id'



# Use Angular to do user/client routing
@app.route('/', defaults={'path': ''})
#@app.route('/<path:path>')
def index(**kwargs):
    return make_response(open('static/index.html').read())

if __name__ == '__main__':
    app.run(debug=True)