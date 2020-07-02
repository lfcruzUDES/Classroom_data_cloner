#!/home/quattroc/Documentos/python/Classroom_data_cloner/env/bin/python
""" Manage basic DB functions """

from Settings import DB as DB, LOCAL_TABLES
from Models import *
from sys import argv


class Manage:
    db = DB
    tables_str = LOCAL_TABLES

    @staticmethod
    def table_str_to_model():
        models = [eval(c) for c in Manage.tables_str]
        return models

    @staticmethod
    def migrate(table=None):
        """ Migrate the models. """
        model_tables = Manage.table_str_to_model()
        Manage.db.connect()
        Manage.db.create_tables(model_tables)

    @staticmethod
    def drop(table=None):
        """ Drop model tables from DB. """
        model_tables = Manage.table_str_to_model()
        Manage.db.drop_tables(model_tables)


if __name__ == "__main__":
    try:
        if argv[1] == 'migrate':
            Manage.migrate()
        elif argv[1] == 'drop':
            Manage.drop()
    except IndexError:
        print("Add a valid parameter.")
