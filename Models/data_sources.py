""" Modelo de la hoja extracción. """
from peewee import *
from unidecode import unidecode

from Settings import DB

from .utils import clear_txt

from datetime import datetime

# Año	Oferta	Sem	Grupo	Id Asig	Asignatura	Docente


class SourceModel(Model):
    slug = CharField(max_length=100, unique=True)
    plan = CharField(max_length=10)
    career = CharField(max_length=100)
    grade = CharField(max_length=3)
    group = CharField(max_length=3)
    subject_id = CharField(max_length=20)
    subject = CharField(max_length=200)
    teacher = CharField(max_length=200)
    # status: 1 -> Analisar, 2 -> No analisar
    status = SmallIntegerField(default=1)
    classroom = TextField()
    drive = TextField()
    _created = DateTimeField(default=datetime.now())
    _updated = DateTimeField(default=datetime.now())

    class Meta:
        database = DB

    def save(self, *args, **kwargs):
        if not self.slug:
            period = PeriodModel.select()[-1]
            self.slug = (f'{self.plan}_{period.name}_{self.career}_'
                         f'{self.grade}{self.group}')
        self.slug = clear_txt(self.slug, delallspaces=True, uni_decode=True)
        self.plan = clear_txt(self.plan, delallspaces=True, uni_decode=True)
        self.career = clear_txt(self.career, uni_decode=True)
        self.grade = clear_txt(self.grade, delallspaces=True, uni_decode=True)
        self.group = clear_txt(self.group, delallspaces=True, uni_decode=True)
        self.subject_id = clear_txt(self.subject_id, delallspaces=True, uni_decode=True)
        self.subject = clear_txt(self.subject, uni_decode=True)
        self.teacher = clear_txt(self.teacher)
        self._updated = datetime.now();

        super(SourceModel, self).save(*args, **kwargs)


class PeriodModel(Model):
    name = CharField(max_length=20, unique=True)

    class Meta:
        database = DB

    def save(self, *args, **kwargs):
        if self.name:
            self.name = clear_txt(
                self.name,
                delallspaces=True,
                uni_decode=True
            )
        super(PeriodModel, self).save(*args, **kwargs)
