from flask import Flask
from flask_pymongo import PyMongo


_app = Flask(__name__)
_mongo = None
def create_mongo():
    global _mongo
    _mongo = PyMongo(_app)
    return None

def get_mongo():
    return _mongo

def create_app():
    # if you change host you must also change the running database name too
    _app.config['MONGO_HOST'] = 'mongodb'

    _app.config['MONGO_DBNAME'] = 'flask'
    
    from accounts.views import accounts_app
    _app.register_blueprint(accounts_app)

    return _app