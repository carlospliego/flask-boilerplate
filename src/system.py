from flask import Flask
from mongoengine import *
from flask_jwt_extended import JWTManager
from common.settings import SETTINGS

app = None


def create_app():
    global app

    if not app:
        app = Flask(__name__)

    from views.user import user
    app.register_blueprint(user, url_prefix='/user')
    from views.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    # load settings
    app.config = {**app.config, **SETTINGS}

    JWTManager(app)
    return app


def connect_db(db_name, host):
    return connect(db_name, host=host)

