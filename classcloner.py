#!/home/quattroc/Documentos/python/Classroom_data_cloner/env/bin/python

from App import SeekAndExecute, SourceApp
from Models import LogsModel
from sys import argv
from exceptions import NoPeriod


class Executor():
    @staticmethod
    def SE():
        return SeekAndExecute()

    @staticmethod
    def SU():
        return SourceApp()

    @staticmethod
    def set_period(auto_resp=False):
        if Executor.confirm(auto_resp):
            period_name = input('Agregar periodo: ')
            period = SourceApp.set_period(period_name)
            print(f'Se ha agregado el periodo {period.name}.')

    @staticmethod
    def get_subjects(auto_resp=False):
        if Executor.confirm(auto_resp):
            print('Obteniendo datos de las clases...')
            Executor.SU().get_datas()

    @staticmethod
    def get_info_files(auto_resp=False):
        if Executor.confirm(auto_resp):
            print('Guardando datos de los archivos de cada carpeta de clase.')
            Executor.SE().save_info_files()

    @staticmethod
    def make_clones(auto_resp=False):
        if Executor.confirm(auto_resp):
            print(
                'Copiando archivos de las clases a la carpeta de Repositorio de Asignaturas.')
            Executor.SE().file_clone_factory()

    @staticmethod
    def send_to_index(auto_resp=False):
        if Executor.confirm(auto_resp):
            print('Agregando archivos copiados de las materias al index al index.')
            Executor.SE().set_to_index()

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
        logo="""
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0kdlc;'..           ..;cd0NMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXOdc;..                         ,dXMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxl;.                            .',,';xNMM
MMMMMMMMMMMMMMMMMMMMMMMMWXkl,.                             .:c:;.   .oNM
MMMMMMMMMMMMMMMMMMMMMW0d;.                             .,col;.       .OM
MMMMMMMMMMMMMMMMMMWKd;.                             .;ldl;.          .xM
MMMMMMMMMMMMMMMMXx;.                             .;oxd;.             .xM
MMMMMMMMMMMMMW0l.       .co;                  .;dkxc.                ,KM
MMMMMMMMMMMMXc.        ;KWM0'               ,oOOo'                  .xWM
MMMMMMMMMN0KX:        .xMMNo.            .cOKx;.                   .oNMM
MMMMMMMW0:.cNK;        ;xd;           .;xXKo'                     .oNMMM
MMMMMMXo.  '0MXc                   .;dKN0l.                      .xWMMMM
MMMMW0,    .kMMNd.             .,cxKWW0c.                       ;0WMMMMM
MMMWx.      dMMMW0l.     ..,:lxKWMMWKc.                       .dNMMMMMMM
MMWx.       dMMMMMWXOkkkO0XWMMMMMMXo.                       .oXMMMMMMMMM
MWx.        dMMMMMMMMMMMMMMMMMMMWk'                       .lKMMMMMMMMMMM
MK,         oWMMMMMMMMMMMMMMMMMXc.                      'dKMMMMMMMMMMMMM
Md          cNMMMMMMMMMMMMMMMWO,                     .:kNMMMMMMMMMMMMMMM
Wl          ,KMMMMMMMMMMMMMMWx.                   .,dKWMMMMMMMMMMMMMMMMM
Wo          .kMMMMMMMMMMMMMNo.                 .;o0WMMMMMMMMMMMMMMMMMMMM
M0'          lWMMMMMMMMMMMWo.               'cxKWMMMMMMMMMMMMMMMMMMMMMMM
MWk'         .OMMMMMMMMMMWx.            .:oONMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMKl.        cNMMMMMMMMM0'        .;lx0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMXxc'.    .dWMMMMMMMWl  ..;cox0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMNKkxolcoXMMMMMMMW0k0KNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
00000000XWMMMNK000000OOO000XNWMMMMMWXKKXXXXKKKKKKXNMMMMMN0OkO0XKXWMMMMMM
Oc. . ,xKWMMMN0c.   'lool:;'';oONMMWKx,...'cooooc'dWMMKo:cool:,.lWMMMMMM
MO.   cNMMMMMMMO.   cNMMMWXk:.  ,xNMMX:   '0MMMMNooNMO' lWMMMNk'cWMMMW0K
MO.   cWMMMMMMMO.   cNMMMMMMWx.   cXMN:   '0MMMMMNXWX:  ,OWMMMM00WMMMXcd
MO.   cWMMMMMMMO.   cNMMMMMMMWo    lNN:   '0MMMMXXWMNc   .;dKWMMMMMMMXcd
MO.   cWMMMMMMMO.   cNMMMMMMMM0'   '0N:   .okkkd;dMMMKc.    .;dXWMMMMWko
MO.   cWMMMMMMMO.   :NMMMMMMMMK,   '0N:   .cdooc'dMMMMW0l'     .oXMMMMMN
MO.   :NMMMMMMMk.   cWMMMMMMMMk.   :XN:   '0MMMMKKMMMMMMMNOl'    lNMMMN0
MX:   .kWMMMMMXc    :NMMMMMMMK;   ,0MN:   '0MMMMMMXXXxKMMMMMNd.  ;XMMXol
MMO,   .cxOOko:,.   ,KMMMMMXx,  .lKMMN:   .OMMMMMKcx0,;0WMMMMK, .xWMMO:k
MMMXd;.   ..':OO,   .;lollc;',cxKWMWXx'   .,loool'.kO;';coddl;,cOWMMMNxl
MMMMMWX0kkO0XWMWKO000OOOOO0KXWMMMMMWX0OO0OOOOOOOOO0NNXNX0OkkO0NMMMMMMMWX
"""
        title = """
----------------------------------------------------------------
╔═╗╦  ╔═╗╔═╗╔═╗╦═╗╔═╗╔═╗╔╦╗  ╔═╗╦  ╔═╗╔═╗╔═╗  ╔═╗╦  ╔═╗╔╗╔╔═╗╦═╗
║  ║  ╠═╣╚═╗╚═╗╠╦╝║ ║║ ║║║║  ║  ║  ╠═╣╚═╗╚═╗  ║  ║  ║ ║║║║║╣ ╠╦╝
╚═╝╩═╝╩ ╩╚═╝╚═╝╩╚═╚═╝╚═╝╩ ╩  ╚═╝╩═╝╩ ╩╚═╝╚═╝  ╚═╝╩═╝╚═╝╝╚╝╚═╝╩╚═
----------------------------------------------------------------
"""
        print(logo)
        print(title)
        print('By SIT UDES, LUIS FERNANDO CRUZ CARRILLO 2020\n')
        print('Parámetros:')
        print('\tperiod', '\tAsigna un nuevo periodo académico.')
        print('\tsubjects', '\tObtiene las materia de las que se extraerán los datos.')
        print('\tfiles', '\t\tObtiene los datos de los archivos de usados en las clases.')
        print('\tclone', '\t\tClona los archivos de las clases en la carpeta de RecursosAsignaturas.')
        print('\tindex', '\t\tManda los datos de los archivos clonados al index.')
        print('\t--help', '\t\tMuestra la ayuda.')
        print('\n*NOTA: si no se pasa ningún parámetro ejecuta todos los procesos.')


try:
    if argv[1] == 'period':
        Executor.set_period()
    elif argv[1] == 'subjects':
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
except NoPeriod:
    print('No hay un periodo académico al cual asignar las clases que serán extraidas. favor de agregar uno.')
    Executor.set_period()
except IndexError:
    Executor.all()
