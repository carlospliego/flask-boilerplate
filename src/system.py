from flask import Flask
from mongoengine import *
from flask_jwt_extended import JWTManager
from common.settings import SETTINGS
from flask_restful import Resource, Api

app = None

api = None


def create_app():
    global app
    global api

    if not app:
        app = Flask(__name__)

    if not api:
        api = Api(app)

    from views.user import user
    app.register_blueprint(user, url_prefix='/user')
    from views.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    app.config = {**app.config, **SETTINGS}  # load settings

    JWTManager(app)
    return app


def connect_db(db_name, host):
    return connect(db_name, host=host)

