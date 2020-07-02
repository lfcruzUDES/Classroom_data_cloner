from datetime import datetime

from peewee import IntegrityError

import Settings
from Google import Gss
from Models import PeriodModel, SourceModel


class SourceApp:
    headers = Settings.SS_HEADERS

    def __init__(self):
        self.period = self.get_period()

    def get_period(self):
        return PeriodModel.select()[-1]

    def get_datas(self):
        for data_range in Settings.RANGES_EXTRACT_DATA:
            ss = Gss(Settings.SECRETS_PATH, Settings.SS_SCOPES,
                     Settings.BOOK_EXTRACT_DATAS_ID, data_range)
            values = ss.get_datas()
            for val in values:
                data = self.compress(val)
                self.save(data)

    def compress(self, data):
        first_part_len = len(self.headers[:-2])
        values = data[:first_part_len] + data[-2:]
        return {k: v for k, v in zip(self.headers, values)}

    def save(self, data):
        if ('classroom.google.com' in data['classroom_url']
                and 'drive.google.com' in data['drive_url']):
            slug = (f'{data["plan"]}_{self.period.name}_{data["career"]}_'
                    f'{data["grade"]}{data["group"]}')
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
