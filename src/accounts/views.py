from flask import (
    Blueprint, Response
)
from common.system import app
from accounts.models import User
from passlib.hash import pbkdf2_sha256


accounts_app = Blueprint('accounts_app', __name__)

@accounts_app.route('/users')
def index():
    """docstring"""
    users = User.objects.all().exclude("id")
    resp = Response(users.to_json(), status=200, mimetype='application/json')

    return resp 

# get for testing now
@accounts_app.route('/signup', methods=['GET'])
def signup():
    """docstring"""
    username = "awesomedave"
    
    if not (User.objects(username=username)):
        # user doesn't exist
        password = "dave123"
        
        pwhash = pbkdf2_sha256.encrypt(password, rounds=80, salt_size=8)
        user = User(username=username, first="Dave", last="Roberts", password=pwhash)

        user.save()
    
    return str(User.objects.count())

@accounts_app.route('/', methods=['GET'])
def login():
    """docstring"""
    return "greetings!"
