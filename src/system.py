from flask import Flask
from flask_pymongo import PyMongo

class System():

    app = None

    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['MONGO_HOST'] = 'mongodb'
        self.app.config['MONGO_DBNAME'] = 'flask'
        self.db = PyMongo(self.app)

    def get_db(self):
        with self.app.app_context():
            return self.db.db


# def create_app():
#     app = Flask(__name__)
#     app.config['MONGO_HOST'] = 'mongodb'
#     app.config['MONGO_DBNAME'] = 'flask'
#     # mongo = PyMongo(app)
#     return app