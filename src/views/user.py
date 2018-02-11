from flask import (
    Blueprint
)
from flask_jwt_extended import jwt_required
from models.user import User
from common.decorators import paginated, query, composed, json_res

user = Blueprint('user', __name__)


@user.route('/where', methods=['GET'])
@composed(jwt_required, paginated, query, json_res)
def where(pag, q):

    users = User.objects(
        __raw__=q
    ).skip(pag['offset']).limit(pag['limit']).exclude("id", "password")

    return users.to_json(), 200


@user.route('/', methods=['GET'])
@composed(jwt_required, paginated, json_res)
def index(pag):

    users = User.objects.all().skip(pag['offset']).limit(pag['limit']).exclude("id", "password")

    return users.to_json(), 200
