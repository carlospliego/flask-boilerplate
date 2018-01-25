from flask import Flask
from mongoengine import *
from flask_jwt_extended import JWTManager


app = None


def create_app():
    global app
    app = Flask(__name__)

    from views.user import user
    app.register_blueprint(user, url_prefix='/user')
    from views.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    #todo reference env variable
    app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!

    JWTManager(app)
    return app


def connect_db(db_name, host):
    return connect(db_name, host=host)
