from flask import (
    Blueprint, Response
)
from common.system import app
from accounts.models import User;

accounts_app = Blueprint('accounts_app', __name__)

@accounts_app.route('/users')
def index():
    users = User.objects.all().exclude("id")
    resp = Response(users.to_json(), status=200, mimetype='application/json')

    return resp 

@accounts_app.route('/signup', methods=['POST'])
def signup():
    
    return "great"

@accounts_app.route('/', methods=['GET'])
def login():
    return "greetings!"