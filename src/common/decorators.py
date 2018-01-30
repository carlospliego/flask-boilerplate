from functools import wraps
from flask import g, request, jsonify


def json_only(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            request.get_json()
        except:
            return jsonify({"msg": "Missing Json in request"}), 400

        return f(*args, **kwargs)
    return decorated_function