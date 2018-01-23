from flask import (
    Blueprint, Response
)
from bson.json_util import dumps 
from flask_pymongo import PyMongo
from system import create_mongo, get_mongo
create_mongo()
mongo = get_mongo()

accounts_app = Blueprint('accounts_app', __name__)

@accounts_app.route('/')
def hello():
    users = mongo.db.user.find({'first':'Carlos'})
    resp = Response(dumps(users), status=200, mimetype='application/json')
    return resp 