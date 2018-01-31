from flask import (
    Blueprint,
    Response,
    request
)
from flask_jwt_extended import jwt_required
from models.user import User
from common.decorators import paginated

import json

user = Blueprint('user', __name__)

@user.route('/search', methods=['GET'])
@jwt_required
@paginated
def query(pag):

    _q = request.args.get('q')

    ## make this a decorator
    if not _q:
        return Response(json.dumps({'msg': 'query string is required'}), 400, mimetype='application/json')

    try:
       raw =  json.loads(_q)
    except ValueError:
        return Response(json.dumps({'msg': 'invalid json'}), 400, mimetype='application/json')

    users = User.objects(
        __raw__=raw
    ).skip(pag['offset']).limit(pag['limit']).exclude("id", "password")

    return Response(users.to_json(), status=200, mimetype='application/json')




@user.route('/', methods=['GET'])
@jwt_required
def index():


    #
    # # no pagination
    users = User.objects.all().exclude("id", "password")
    #
    # # pagination
    # users = User.objects(
    #     __raw__=json.loads(q)
    # ).skip(offset).limit(limit).exclude("id")
    #
    # # JSONDecodeError
    # # BrokenFilesystemWarning



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