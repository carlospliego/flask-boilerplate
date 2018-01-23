from flask import Flask, Response
from flask_pymongo import PyMongo
from bson.json_util import dumps 

app = Flask(__name__)

# database stuff
app.config['MONGO_HOST'] = 'mongodb'
app.config['MONGO_DBNAME'] = 'flask'
mongo = PyMongo(app)

@app.route('/')
def hello():
    users = mongo.db.user.find({'first':'Carlos'})
    resp = Response(dumps(users), status=200, mimetype='application/json')
    return resp 

if __name__ == '__main__':
    app.run(host='0.0.0.0')