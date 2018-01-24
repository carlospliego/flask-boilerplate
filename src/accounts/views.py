"""
    Send authorization token in header as Authorization : Bearer <token>

"""
from mongoengine.errors import NotUniqueError
from flask import (
    Blueprint, Response, request, jsonify
)
# todo note install pip with install -U module...
from common.system import app
from accounts.models import User
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token
)



from botocore.exceptions import ClientError

# Setup the accounts blueprint
accounts_app = Blueprint('accounts_app', __name__)

# TODO move this to a configuration file.
# TODO change 'accounts_app' to 'authorization' or something
# TODO protect against known security vulnerabilities


# Initialize the JWT Manager for the applciation
jwt = JWTManager(app)


@accounts_app.route('/users')
def index():
    """docstring"""
    users = User.objects.all().exclude("id")
    resp = Response(users.to_json(), status=200, mimetype='application/json')

    return resp 


# get for testing now
@accounts_app.route('/signup', methods=['POST'])
def signup():
    """docstring"""

    # todo implement decorator for is json
    # validate incoming json
    if not request.is_json:
        # todo make messaging interface
        return jsonify({"msg": "Missing Json in request"}), 400



    # TODO create a common library for messages

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    first = request.json.get('first', None)
    last = request.json.get('last', None)

    try:
        user = User(username=username, first=first, last=last, password=password)
        user.save()
    except NotUniqueError:
        return "username is already taken"

    return str(User.objects.count())


@accounts_app.route('/login', methods=['POST'])
def login():

    # validate incoming json
    if not request.is_json:
        return jsonify({"msg":"Missing Json in request"}), 400

    # get username and password from the request body
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # check if username and password are not empty
    if not username:
        return jsonify({"msg":"Missing username parameter"}), 400
    if not password:
        return jsonify({"msg":"Missing password parameter"}), 400

    # get user
    user = User.objects(username=username).first()

    if not user or not pbkdf2_sha256.verify(password, user.password):
        return jsonify({"msg":"Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@accounts_app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    return "you made it"