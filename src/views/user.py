from flask import (
    Blueprint,
    Response,
    request
)
from flask_jwt_extended import jwt_required
from models.user import User
import json

user = Blueprint('user', __name__)

@user.route('/search', methods=['GET'])
@jwt_required
def query():
    # ----------------------------------------------------------- Put in library ?
    _q = request.args.get('q')
    _page = request.args.get('page')
    _limit = request.args.get('limit')
    _default_page = 1 # put in some sort of constant
    _default_items = 10 # put in some sort of constant

    try:
        page = int(_default_page if not _page else _page)
        limit = int(_default_items if not _limit else _limit)
        offset = (page - 1) * limit
    except ValueError:
        return Response(json.dumps({'msg': 'page and limit must be integers'}), 400, mimetype='application/json')

    # -----------------------------------------------------------

    if not _q:
        return Response(json.dumps({'msg': 'query string is required'}), 400, mimetype='application/json')

    try:
        users = User.objects(
            __raw__=json.loads(_q)
        ).skip(offset).limit(limit).exclude("id", "password")
    except (ValueError, TypeError) as e :
        return Response(json.dumps({'msg': 'invalid json'}), 400, mimetype='application/json')

    return Response(users.to_json(), status=200, mimetype='application/json')




@user.route('/', methods=['GET'])
@jwt_required
def index():



    # no pagination
    users = User.objects.all().exclude("id", "password")

    # pagination
    users = User.objects(
        __raw__=json.loads(q)
    ).skip(offset).limit(limit).exclude("id")

    # JSONDecodeError
    # BrokenFilesystemWarning



    resp = Response(users.to_json(), status=200, mimetype='application/json')

    return resp

    # #--------------------------------------------------------------------------
    #
    # page_number = 1
    # items_per_page = 10
    # offset = (page_number - 1) * items_per_page
    # q = request.args.get('q')
    #
    # # todo put json.loads in a try catch
    # users = User.objects(
    #     __raw__=json.loads(q)
    # ).skip(offset).limit(items_per_page).exclude("id")
    #
    # # --------------------------------------------------------------------------

    # request data
#   page = int(request.args.get('page')) # try catch
#    limit = int(request.args.get('limit')) #try catch
#    offset = (page - 1) * limit

# try:
#     query_json = json.loads(request.args.get('q'))
# except ValueError:


# if q is not None:
#     users = User.objects(
#         __raw__=json.loads(q)
#     ).exclude("id", "password")
# else:
#     users = User.objects.all().exclude("id")


##