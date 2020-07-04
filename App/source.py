from datetime import datetime

from peewee import IntegrityError, OperationalError

import Settings
from Google import Gss
from Models import PeriodModel, SourceModel
from exceptions import NoPeriod


class SourceApp:
    """ Clase que trabaja con los datos que extrae del libro
    Settings.BOOK_EXTRACT_DATAS_URL """

    headers = Settings.SS_HEADERS

    def __init__(self):
        self.period = self.get_period()

    @staticmethod
    def set_period(name):
        """ Inserta un periodo en la taba de periodos academicos. """
        return PeriodModel.create(name=name)

    def get_period(self):
        """ Obtiene el útimo periodo académico de la base de datos. """
        try:
            return PeriodModel.select()[-1]
        except IndexError:
            raise NoPeriod

    def get_datas(self):
        """ Obtiene los datos del libro de cálculo que contiene
        las materias y los docentes, según los rangos declarados
        en Settings.RANGES_EXTRACT_DATA. A continuación guarda
        los datos en la base de datos."""
        with Settings.DB.atomic():
            for data_range in Settings.RANGES_EXTRACT_DATA:
                ss = Gss(Settings.SECRETS_PATH, Settings.SS_SCOPES,
                         Settings.BOOK_EXTRACT_DATAS_ID, data_range)
                values = ss.get_datas()
                for val in values:
                    data = self.compress(val)
                    self.save(data)

    def compress(self, data):
        """Crea un diccionario teniendo la lista de encabezados de
        Settoings.SS_HEADERS como claves y data como sus valores.

        Args:
            data (list): Lista de datos que representa una fila.

        Returns:
            list( dict,... ): Lista de obectos.
        """
        first_part_len = len(self.headers[:-2])
        values = data[:first_part_len] + data[-2:]
        return {k: v for k, v in zip(self.headers, values)}

    def save(self, data):
        """Guarda la data en la base de datos, en la tabla
        SourceModel.

        Args:
            data (list): Lista de objetos, en donde las claves están
            indicadas por Settings.SS_HEADERS.
        """
        if ('classroom.google.com' in data['classroom_url']
                and 'drive.google.com' in data['drive_url']):
            slug = (f'{data["plan"]}_{self.period.name}_{data["career"]}_'
                    f'{data["subject_id"]}_{data["grade"]}{data["group"]}')
            defaults = {
                'plan': data["plan"],
                'career': data["career"],
                'grade': data["grade"],
                'group': data["group"],
                'subject_id': data["subject_id"],
                'subject': data["subject"],
                'teacher': data["teacher"],
                'classroom': data["classroom_url"],
                'drive': data["drive_url"]
            }

            source, created = SourceModel.get_or_create(
                slug=slug,
                defaults=defaults
            )

            if source and not created:
                SourceModel.update(**defaults).where(SourceModel.slug == slug)


if __name__ == "__main__":
    s = SourceApp()
    d = s.get_datas()
