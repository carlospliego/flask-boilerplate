from flask import (
    Blueprint,
    Response,
    request
)
from flask_jwt_extended import jwt_required
from models.user import User
import json

user = Blueprint('user', __name__)


@user.route('/')
@jwt_required
def index():
    # todo put this in a library
    # request.query_string
    # request.args.get(?)
    # __raw__={'tags': 'coding'}

    # -----

    '''
    THE get() method
        if q is set:
            if page is set:
                query (q, page)
            else:
                query(q, defaultPage)
        else:
            if page is set:
                query (all, page)
            else:
                query(all, defaultPage)
    '''

    '''
        Pagination
        
        page_nb = 2 
        items_per_page = 10 
        
        offset = (page_nb - 1) * items_per_page
        
        list = Books.objects.skip( offset ).limit( items_per_page )
    '''

    # todo put what you can in the base model

    q = request.args.get('q')
    # todo put json.loads in a try catch
    users = User.objects(__raw__=json.loads(q)).exclude("id") #?q={"username":"carlos2"}




    # users = User.objects().exclude("id")
    resp = Response(users.to_json(), status=200, mimetype='application/json')

    return resp