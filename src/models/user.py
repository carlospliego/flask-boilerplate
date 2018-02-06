from passlib.hash import pbkdf2_sha256
from .model import *


class User(Model):
    username = StringField(required=True, unique=True)
    first = StringField()
    last = StringField()
    password = StringField()

    def clean(self):
        if self.password:
            self.password = pbkdf2_sha256.using(rounds=80, salt_size=8).hash(self.password)
