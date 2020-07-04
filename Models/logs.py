from peewee import *

from Settings import DB

from datetime import datetime

class LogsModel(Model):
    error = TextField()
    other = CharField(max_length=250, null=True)
    _created = DateTimeField(default=datetime.now())

    class Meta:
        database = DB
