from flask import Flask
from mongoengine import *
from flask_jwt_extended import JWTManager
from common.settings import SETTINGS
from flask_restful import Resource, Api

app = None

api = None

##todo PICKUP here https://flask-restful.readthedocs.io/en/latest/quickstart.html

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


    ### HERE
    class HelloWorld(Resource):
        def get(self):
            return {'hello': 'world'}

    api.add_resource(HelloWorld, '/')

    # load settings
    app.config = {**app.config, **SETTINGS}

    JWTManager(app)
    return app


def connect_db(db_name, host):
    return connect(db_name, host=host)

