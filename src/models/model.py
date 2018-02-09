from datetime import datetime
from mongoengine import *

import sys
from pprint import pprint

class Model(Document):

    created = DateTimeField()
    updated = DateTimeField(default=datetime.now)

    meta = {'abstract': True}  # limiting model inheritance. Required

    def save(self, *args, **kwargs):
        if not self.created:
            self.created = datetime.now()
        self.updated = datetime.now()
        return super(Model, self).save(*args, **kwargs)

    # so you tried this one before. The Document context is actually unaware of the context User?

    # TODO does not need to extend Document anymore since you're just passing the context in
    def where(ctx, *args, **kwargs):
        # pprint(ctx, file=sys.stderr)
        # print(ctx.objects(**kwargs), *args, file=sys.stderr)
        return ctx.objects(**kwargs)
        # pass
        # return 'brains'
        