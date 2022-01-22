import cloudinary
import cloudinary.uploader

from dotenv import load_dotenv
from os import getenv

from flask import Flask

from .views.main import main

from extensions import *

load_dotenv()

def create_app():
    # Initialize app
    app = Flask(__name__)
    
    # Initialize config
    app.config.from_object('config.DevelopmentConfig')
    cloudinary.config(
        cloud_name = getenv('CLOUD_NAME'),
        api_key = getenv('API_KEY'),
        api_secret = getenv('API_SECRET')
    )
    
    # Initialize extensions
    db.init_app(app)
    bootstrap.init_app(app)
    #csrf.init_app(app)
    
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    with app.app_context():
        # Register blueprints
        app.register_blueprint(main)
    
    return app