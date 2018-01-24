"""
    Send authorization token in header as Authorization : Bearer <token>

"""
from flask import (
    Blueprint, Response, request, jsonify, current_app
)

from common.system import app
from accounts.models import User
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


accounts_app = Blueprint('accounts_app', __name__)

# Setup the Flask-JWT-Extended extension
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this!
jwt = JWTManager(app)


@accounts_app.route('/users')
def index():
    """docstring"""
    users = User.objects.all().exclude("id")
    resp = Response(users.to_json(), status=200, mimetype='application/json')

    return resp 


# get for testing now
@accounts_app.route('/signup', methods=['GET'])
def signup():

    # todo make primary keys in the models.
    """docstring"""
    username = "awesomedave"
    user = User.objects(username=username)
 
    if not user:
        # user doesn't exist
        password = "dave123"

        password_hash = pbkdf2_sha256.encrypt(password, rounds=80, salt_size=8)
        user = User(username=username, first="Dave", last="Roberts", password=password_hash)

        user.save()

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