from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"

@views.route('/homepage')
def homepage():
    return "<p>homepage</p>"