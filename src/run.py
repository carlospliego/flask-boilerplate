from flask import Flask, Response
from flask_pymongo import PyMongo
from bson.json_util import dumps 
from system import System

sys = System()
app = sys.app
db = sys.get_db()

@app.route('/')
def hello():

    users = db.user.find({'first':'Carlos'})
    resp = Response(dumps(users), status=200, mimetype='application/json')
    return resp 

if __name__ == '__main__':
    app.run(host='0.0.0.0')