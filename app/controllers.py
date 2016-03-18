#Where the views will go
from flask import render_template, make_response
from app import app

#use send_file for caching, make_response for development
@app.route('/')
@app.route('/index')
def index():
    return make_response(open('templates/index.html').read())
