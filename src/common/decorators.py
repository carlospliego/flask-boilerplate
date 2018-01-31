from functools import wraps
from flask import g, request, jsonify, Response


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
        except ValueError:
            return Response(jsonify({'msg': 'could not parse page and limit'}), 400, mimetype='application/json')

        return f({'offset': offset, 'limit': limit})
    return decorator