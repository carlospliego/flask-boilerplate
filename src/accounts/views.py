from flask import (
    Blueprint, Response
)
from common.system import app
from accounts.models import User;

accounts_app = Blueprint('accounts_app', __name__)

@accounts_app.route('/')
def index():
    users = User.objects.all().exclude("id")
    resp = Response(users.to_json(), status=200, mimetype='application/json')

    return resp 