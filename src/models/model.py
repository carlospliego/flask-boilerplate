from datetime import datetime
from mongoengine import *


class Model(Document):

    created = DateTimeField()
    updated = DateTimeField(default=datetime.now)

    meta = {'abstract': True}  # limiting model inheritance. Required

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.now()
        self.updated = datetime.now()
        return super(Model, self).save(*args, **kwargs)