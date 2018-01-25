from flask import Blueprint, Response
from flask_jwt_extended import jwt_required
from models.user import User

user = Blueprint('user', __name__)


@user.route('/list')
@jwt_required
def index():
    users = User.objects.all().exclude("id")
    resp = Response(users.to_json(), status=200, mimetype='application/json')

    return resp