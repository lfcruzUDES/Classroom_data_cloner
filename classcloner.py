#!/home/quattroc/Documentos/python/Classroom_data_cloner/env/bin/python

from App import SeekAndExecute, SourceApp
from Models import LogsModel
from sys import argv


class Executor():
    _SE = SeekAndExecute()
    _SU = SourceApp()

    @staticmethod
    def get_subjects(auto_resp=False):
        if Executor.confirm(auto_resp):
            print('Obteniendo datos de las clases...')
            Executor._SU.get_datas()

    @staticmethod
    def get_info_files(auto_resp=False):
        if Executor.confirm(auto_resp):
            print('Guardando datos de los archivos de cada carpeta de clase.')
            Executor._SE.save_info_files()

    @staticmethod
    def make_clones(auto_resp=False):
        if Executor.confirm(auto_resp):
            print(
                'Copiando archivos de las clases a la carpeta de Repositorio de Asignaturas.')
            Executor._SE.file_clone_factory()

    @staticmethod
    def send_to_index(auto_resp=False):
        if Executor.confirm(auto_resp):
            print('Agregando archivos copiados de las materias al index al index.')
            Executor._SE.set_to_index()

    @staticmethod
    def all():
        print('Se va a ejecutar un proceso de extracción y clonado de los archivos de las asignaturas.')
        print('Este proceso puede durar bastante tiempo.')
        auto_resp = Executor.confirm()
        if auto_resp:
            Executor.get_subjects(auto_resp)
            Executor.get_info_files(auto_resp)
            Executor.make_clones(auto_resp)
            Executor.send_to_index(auto_resp)

    @staticmethod
    def confirm(response=False):
        if not response:
            confirm = input('Desea continuar (s/n): ')
            if confirm == 's':
                return True
            return False
        return response
    @staticmethod
    def instructions():
        title = 'C L A S S R O O M  C L A S S  C L O N E R'
        print('-' * len(title))
        print(title)
        print('-' * len(title))
        print('By SIT UDES, LUIS FERNANDO CRUZ CARRILLO 2020\n')
        print('Parámetros:')
        print('\tsubjects', '\tObtiene las materia de las que se extraerán los datos.')
        print('\tfiles', '\t\tObtiene los datos de los archivos de usados en las clases.')
        print('\tclone', '\t\tClona los archivos de las clases en la carpeta de RecursosAsignaturas.')
        print('\tindex', '\t\tManda los datos de los archivos clonados al index.')
        print('\t--help', '\t\tMuestra la ayuda.')
        print('\n*NOTA: si no se pasa ningún parámetro ejecuta todos los procesos.')


try:
    if argv[1] == 'subjects':
        Executor.get_subjects()
    elif argv[1] == 'files':
        Executor.get_info_files()
    elif argv[1] == 'clone':
        Executor.make_clones()
    elif argv[1] == 'index':
        Executor.send_to_index()
    elif argv[1] == '--help':
        Executor.instructions()
    else:
        print('No se encontró ingún parámetro válido.')
        print('Pruebe con alguno de los siguientes parámetros.\n')
        Executor.instructions()
except IndexError:
    Executor.all()
