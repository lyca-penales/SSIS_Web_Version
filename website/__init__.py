from flask import Flask

def create_ssis():
    ssis = Flask(__name__)
    ssis.config['SECRET KEY'] = 'SSIS Web App'

    from .views import views
    from .auth import auth

    ssis.register_blueprint(views, url_prefix = '/')
    ssis.register_blueprint(auth, url_prefix = '/')
    
    return ssis
