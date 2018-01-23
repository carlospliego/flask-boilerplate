from mongoengine import *

class User(Document):
    first = StringField(required=True)
    last = StringField()