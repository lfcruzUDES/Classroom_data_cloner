#!/home/quattroc/Documentos/python/Classroom_data_cloner/env/bin/python

from exceptions import NoPeriod
from sys import argv

from fnMenu import FnMenu

if __name__ == "__main__":
    try:
        if argv[1] == 'period':
            FnMenu.get_period_books()
        elif argv[1] == 'subjects':
            FnMenu.get_subjects()
        elif argv[1] == 'files':
            FnMenu.get_info_files()
        elif argv[1] == 'clone':
            FnMenu.make_clones()
        elif argv[1] == 'index':
            FnMenu.send_to_index()
        elif argv[1] == '--help':
            FnMenu.instructions()
        else:
            print('No se encontró ingún parámetro válido.')
            print('Pruebe con alguno de los siguientes parámetros.\n')
            FnMenu.instructions()
    except IndexError:
        FnMenu.all_process()
    except Exception as e:
        print(e)
