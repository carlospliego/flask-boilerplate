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



class User(Model):
    # todo add unique
    username = StringField(required=True, unique=True)
    first = StringField()
    last = StringField()
    password = StringField()


    def clean(self):
        if self.password:
            self.password = pbkdf2_sha256.encrypt(self.password, rounds=80, salt_size=8)

    # super(Foo, self)
    # def q(self, *args, **kwargs):
    #     import json
    #     # User.objects(__raw__=json.loads(q)).exclude("id") #?q={"username":"carlos2"}
    #     return User.objects(__raw__={"username":"carlos1"})
    #     # return super(User, self).objects.all()

    # def q(self, *args, **kwargs):
    #     import json
    #     # User.objects(__raw__=json.loads(q)).exclude("id") #?q={"username":"carlos2"}
    #     # return super(User, self).objects(__raw__={"username":"carlos1"})
    #     # return super(User, self).objects.all()
    #     return __class__.objects(*args, **kwargs)
