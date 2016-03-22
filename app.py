#Module containing Flask application
from flask import Flask, send_file, make_response

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
#db = SQLAlchemy(app)


#Use flask to do all RESTful API routing and angular to do user/client routing
@app.route("/")
def index():
    return make_response(open('templates/index.html').read())

if __name__ == '__main__':
    app.run(debug=True)