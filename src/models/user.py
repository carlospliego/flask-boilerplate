# third party modules should be placed first
from mongoengine import *
from datetime import datetime
from passlib.hash import pbkdf2_sha256


# todo put this in a system package
# todo create an interface maybe?
class Model(Document):

    created = DateTimeField()
    updated = DateTimeField(default=datetime.now)

    # limiting model inheritance. Required
    meta = {'abstract': True}

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.now()
        self.updated = datetime.now()
        return super(Model, self).save(*args, **kwargs)

    # get where q?


class User(Model):
    # todo add unique
    username = StringField(required=True, unique=True)
    first = StringField()
    last = StringField()
    password = StringField()

    def clean(self):
        if self.password:
            self.password = pbkdf2_sha256.encrypt(self.password, rounds=80, salt_size=8)



