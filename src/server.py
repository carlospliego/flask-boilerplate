from flask import Flask, Response
from flask_pymongo import PyMongo
from bson.json_util import dumps 

app = Flask(__name__)
app.config['MONGO_HOST'] = 'mongodb'
app.config['MONGO_DBNAME'] = 'flask'

mongo = PyMongo(app)

# with app.app_context():
#     users = mongo.db.users.find({'name':'Carlos'})
#     for u in users:
#         print(u)

@app.route('/')
def hello():
    users = mongo.db.user.find({'first':'Carlos'}) 
    # print('effort')
    # print(dumps(users)) 
    resp = Response(dumps(users), status=200, mimetype='application/json')
    return resp 

if __name__ == '__main__':
    app.run(host='0.0.0.0')