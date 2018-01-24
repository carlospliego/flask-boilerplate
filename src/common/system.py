from flask import Flask
from mongoengine import *

app = None


def create_app():
    global app
    app = Flask(__name__)
    
    from accounts.views import accounts_app
    app.register_blueprint(accounts_app)
    
    return app


def connect_db(db_name, host):
    return connect(db_name, host=host)
