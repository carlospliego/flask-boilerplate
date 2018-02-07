from functools import wraps
from flask import g, request, jsonify, make_response, Response
import json

def composed(*decs):
    def deco(f):
        for dec in reversed(decs):
            f = dec(f)
        return f
    return deco

def json_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            request.get_json()
        except:
            return Response(jsonify({"msg": "Missing Json in request"}), 400, mimetype='application/json')

        return f(*args, **kwargs)
    return decorated_function


def paginated(f):

    @wraps(f)
    def decorator(*args, **kwargs):
        _page = request.args.get('page')
        _limit = request.args.get('limit')
        _default_page = 1  # put in some sort of constant
        _default_items = 10  # put in some sort of constant

        try:
            page = int(_default_page if not _page else _page)
            limit = int(_default_items if not _limit else _limit)
            offset = (page - 1) * limit

            # todo add something a little more definative rather than 999999999
            if offset > 999999999:
                return jsonify({'msg': 'paging input is too large'}), 400,

        except ValueError:
            return jsonify({'msg': 'could not parse page and limit'}), 400

        return f(*args, {'offset': offset, 'limit': limit})
    return decorator


def query(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        _q = request.args.get('q')

        if not _q:
            return jsonify({'msg': 'query string is required'}), 400
        try:
            raw = json.loads(_q)
        except ValueError:
            return jsonify({'msg': 'invalid json'}), 400

        return f(*args, raw)
    return decorator


def add_response_headers(headers={}):
    """This decorator adds the headers passed in to the response"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = make_response(f(*args, **kwargs))
            h = resp.headers
            for header, value in headers.items():
                h[header] = value
            return resp
        return decorated_function
    return decorator


def json_res(f):
    @wraps(f)
    @add_response_headers({'Content-Type':'application/json'})
    def decorated(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated

