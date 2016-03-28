#Module containing Flask application
from flask import Flask, send_file, send_from_directory, make_response


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
#db = SQLAlchemy(app)


#Use flask to do all RESTful API routing



# Use Angular to do user/client routing
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(**kwargs):
    return make_response(open('static/index.html').read())

if __name__ == '__main__':
    app.run(debug=True)