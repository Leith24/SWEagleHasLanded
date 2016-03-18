#Module containing Flask application
from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("templates/index.html")

if __name__ == '__main__':
    app.run(debug=True)