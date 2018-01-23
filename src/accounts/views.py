from flask import (
    Blueprint, Response
)
from mongoengine import *
from common.system import app

# host needs to be mongodb
connect('flask', host='mongodb')

class User(Document):
    first = StringField(required=True)
    last = StringField()

accounts_app = Blueprint('accounts_app', __name__)

@accounts_app.route('/')
def hello():
    users = User.objects.all().exclude("id")
    resp = Response(users.to_json(), status=200, mimetype='application/json')
    return resp 