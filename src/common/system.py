from flask import Flask
from mongoengine import *
from flask_jwt_extended import JWTManager


app = None


def create_app():
    global app
    app = Flask(__name__)
    
    from common.accounts.views import accounts_app
    app.register_blueprint(accounts_app)

    app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this! reference config object

    JWTManager(app)
    return app


def connect_db(db_name, host):
    return connect(db_name, host=host)
