from App import SeekAndExecute, SourceApp
from Models import LogsModel


class FnMenu():
    @staticmethod
    def SE():
        """ Crea una instancia de SeekAndExecute."""
        return SeekAndExecute()

    @staticmethod
    def SU():
        """ Crea una instancia de  """
        return SourceApp()

    @staticmethod
    def set_period(auto_resp=False):
        if FnMenu.confirm(auto_resp):
            period_name = input('Agregar periodo: ')
            period = SourceApp.set_period(period_name)
            print(f'Se ha agregado el periodo {period.name}.')

    @staticmethod
    def get_subjects(auto_resp=False, quiet=False):
        if FnMenu.confirm(auto_resp):
            FnMenu.quiet('Obteniendo datos de las clases...', quiet)
            subjects_len = FnMenu.SU().get_datas()
            resp = f'Se botuvieron {subjects_len} asignaturas.'
            FnMenu.quiet(resp, quiet)
            return resp

    @staticmethod
    def get_info_files(auto_resp=False, quiet=False):
        if FnMenu.confirm(auto_resp):
            FnMenu.quiet(
                'Guardando datos de los archivos de cada carpeta de clase.',
                quiet)
            saved_files = FnMenu.SE().save_info_files()
            resp = f'Se obtuvieron los datos de {saved_files} archivos.'
            FnMenu.quiet(resp, quiet)
            return resp

    @staticmethod
    def make_clones(auto_resp=False, quiet=False):
        if FnMenu.confirm(auto_resp):
            FnMenu.quiet(
                'Copiando archivos de las clases a la carpeta de Repositorio de Asignaturas.',
                quiet)
            copied_files = FnMenu.SE().file_clone_factory()
            resp = f'Se clonaron {copied_files} archivos.'
            FnMenu.quiet(resp, quiet)
            return resp

    @staticmethod
    def send_to_index(auto_resp=False):
        if FnMenu.confirm(auto_resp):
            print('Agregando archivos copiados de las materias al index al index.')
            FnMenu.SE().set_to_index()

    @staticmethod
    def all():
        print('Se va a ejecutar un proceso de extracción y clonado de los archivos de las asignaturas.')
        print('Este proceso puede durar bastante tiempo.')
        auto_resp = FnMenu.confirm()
        if auto_resp:
            FnMenu.get_subjects(auto_resp)
            FnMenu.get_info_files(auto_resp)
            FnMenu.make_clones(auto_resp)
            FnMenu.send_to_index(auto_resp)

    @staticmethod
    def confirm(response=False):
        if not response:
            confirm = input('Desea continuar (s/n): ')
            if confirm == 's':
                return True
            return False
        return response

    @staticmethod
    def quiet(txt, quiet=False):
        if not quiet:
            print(txt)

    @staticmethod
    def instructions():
        logo = """
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
        print('\tperiod', '\t\tAsigna un nuevo periodo académico.')
        print('\tsubjects', '\tObtiene las materias de las que se extraerán los datos.')
        print('\tfiles', '\t\tObtiene los datos de los archivos usados en las clases.')
        print('\tclone', '\t\tClona los archivos de las clases en la carpeta de RecursosAsignaturas.')
        print('\tindex', '\t\tManda los datos de los archivos clonados al index.')
        print('\t--help', '\t\tMuestra la ayuda.')
        print('\n*NOTA: Si no se pasa ningún parámetro se ejecutan todos los procesos en secuencia.')
