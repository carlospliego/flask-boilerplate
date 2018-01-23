from flask import Flask, Response
from flask_pymongo import PyMongo
from bson.json_util import dumps 
from common.system import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')