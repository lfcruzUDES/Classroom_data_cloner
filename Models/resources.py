from peewee import *
from unidecode import unidecode

from Settings import DB

from .utils import clear_txt

from datetime import datetime

from .data_sources import SourceModel


class ResourceModel(Model):
    source = ForeignKeyField(SourceModel, on_delete='CASCADE', backref='source')
    fileId = CharField(max_length=250, unique=True)
    name = CharField(max_length=250)
    mimeType = CharField(max_length=250)
    webViewLink = CharField(max_length=250)
    repoViewLink = CharField(max_length=250, null=True)
    repoFileId = CharField(max_length=250, null=True)
    ssUploaded = BooleanField(default=False)
    _created = DateTimeField(default=datetime.now())
    _updated = DateTimeField(default=datetime.now())

    class Meta:
        database = DB

    def save(self, *args, **kwargs):
        self._updated = datetime.now()
        super(ResourceModel, self).save(*args, **kwargs)
