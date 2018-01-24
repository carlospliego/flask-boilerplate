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
    #laskdjf
    _pre_save_hooks = [
        hash
    ]

    def hash(self):
        print('hash')

    # Put this in some base document 
    def save(self, *args, **kwargs):

        print('hashs ')
        # for hook in self._pre_save_hooks:
        #     # the callable can raise an exception if
        #     # it determines that it is inappropriate
        #     # to save this instance; or it can modify
        #     # the instance before it is saved
            
        #     hook(self)

        super(User, self).save(*args, **kwargs)

    # def __init__(self, username, first, last, password):
    #     self.username = username
    #     self.first = first
    #     self.last = last
        # self.password = pbkdf2_sha256.encrypt(
            # password, rounds=200000, salt_size=16)





