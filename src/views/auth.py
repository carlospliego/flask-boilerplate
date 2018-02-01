from mongoengine.errors import NotUniqueError, ValidationError
from flask import (
    Blueprint, request, jsonify
)
from passlib.hash import pbkdf2_sha256
from flask_jwt_extended import create_access_token, jwt_required
from models.user import User
from common.decorators import json_only, composed, json_res

auth = Blueprint('auth', __name__)


@auth.route('/signup', methods=['POST'])
@composed(json_only, json_res)
def signup():

    signup_data = request.get_json()

    try:
        user = User(username=signup_data['username'], first=signup_data['first'],
                    last=signup_data['last'], password=signup_data['password'])
        user.save()
    except NotUniqueError as e:
        return jsonify({"msg": "username is already taken"}), 409
    except ValidationError as e:
        return jsonify({"msg":e.message})

    return user.to_json(), 200


@auth.route('/login', methods=['POST'])
@composed(json_only, json_res)
def login():

    login_data = request.get_json()

    if 'username' not in login_data:
        return jsonify({"msg":"Missing username parameter"}), 400
    if 'password' not in login_data:
        return jsonify({"msg":"Missing password parameter"}), 400

    user = User.objects(username=login_data['username']).first()

    if not user or not pbkdf2_sha256.verify(login_data['password'], user.password):
        return jsonify({"msg":"Bad username or password"}), 401

    access_token = create_access_token(identity=login_data['password'])

    return jsonify(access_token=access_token), 200

@auth.route('/validate', methods=['POST'])
@composed(json_only, json_res, jwt_required)
def validate():
    return jsonify({"msg":"authenticated"}), 200