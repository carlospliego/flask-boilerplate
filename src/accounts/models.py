from mongoengine import *

from passlib.hash import pbkdf2_sha256
import jwt
import datetime

#todo note install pip with install -U module...

# class BaseModel(Document):
    

class User(Document):
    username = StringField()
    first = StringField(required=True)
    last = StringField()
    password = StringField()

    def save(self, *args, **kwargs):
        if self.password:
            self.password = pbkdf2_sha256.encrypt(self.password, rounds=80, salt_size=8)
        super(User, self).save(*args, **kwargs)

