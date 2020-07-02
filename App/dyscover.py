from Google import Drive, Gss
import Settings
from Models import SourceModel, ResourceModel
from datetime import datetime

class SeekAndExecute:
    drive = Drive(Settings.SECRETS_PATH, Settings.DRIVE_SCOPES)
    ss = Gss(Settings.SECRETS_PATH, Settings.SS_SCOPES,
             Settings.BOOK_INDEX_ID, Settings.RANGE_INDEX)

    def get_id_from_url(self, url):
        """ Extrae el id de URLs de Google del tipo:
        https://google.com/aplication/d/id

        En donde la id es siempre el último elemento de la URL """
        return url.split('/')[-1]

    def save_info_files(self):
        """ Extrae los datos de los archivos de cada carpeta
        de Classroom almacenadas (las URLs) en la tabla SourceModel,
        estos datos son guardados en la tabla ResourceModel. Se evita
        guardar los datos de las subcarpetas."""
        folders = SourceModel.select()
        for folder in folders:
            folder_id = self.get_id_from_url(folder.drive)
            data_items = self.drive.get_folder_files(folder_id)
            for item in data_items:
                if (not item.get('mimeType') in Settings.EXCLUDED_TYPE
                        and not 'concentrado' in item.get('name').lower().strip()):
                    fileId = item.get('id')
                    defaults = {
                        'source': folder,
                        'name': item.get('name'),
                        'mimeType': item.get('mimeType'),
                        'webViewLink': item.get('webViewLink'),
                    }
                    resource, created = ResourceModel.get_or_create(
                        fileId=fileId,
                        defaults=defaults
                    )

                    # if resource and not created:
                    #     ResourceModel.update(**defaults).where(ResourceModel.fileId == fileId)

    def file_clone_factory(self):
        """ De los datos almacenados en ResourceModel se obtienen
        los ID de los archivos objetivo, se los copy y la copia de
        manda a la carpeta Settings.BOOK_INDEX_URL, de estos se
        obtiene la URL e ID que se guarda en la misma tabla y que
        indica que ya se han creado las copias y evita que en la
        próxima iteración se hagan más copias. """
        files = ResourceModel.select().where(
            (ResourceModel.repoFileId == '') | (
                ResourceModel.repoFileId == None)
        )
        for file_data in files:
            if not 'concentrado' in file_data.name.lower().strip():
                file_id = file_data.fileId
                file_name = file_data.name
                slug = file_data.source.slug
                new_name = f'{slug}_{file_name}'
                new_file = self.drive.copy_file(
                    file_id=file_id,
                    name=new_name
                )
                self.drive.move_to_forlder(
                    file_id=new_file.get('id'),
                    folder_id=Settings.REPO_FOLDER_ID
                )
                file_data.repoFileId = new_file.get('id')
                file_data.repoViewLink = new_file.get('webViewLink')
                file_data.save()

    def set_to_index(self):
        """ Se revisan los registros de la tabla ResourceModel,
        los que estén completos, es decir, que ya hayan sido copiados
        y que por lo tanto tengan llenos los campos de repoViewLink y
        repoFileId, entonces estos registros completos se suben a al
        Spreadsheet Settings.BOOK_INDEX_URL. """
        datas = []
        files = ResourceModel.select().where(
            (ResourceModel.ssUploaded == '') | (
                ResourceModel.ssUploaded == None)
        )
        for row in files:
            datas.append(
                [str(datetime.now()), row.source.plan, row.source.career, row.source.grade,
                 row.source.group, row.source.subject_id, row.source.subject,
                 row.source.teacher, row.name, row.repoViewLink]
            )
            row.ssUploaded = True
            row.save()
        rows = self.ss.append_datas(datas)
        return rows


if __name__ == "__main__":
    se = SeekAndExecute()
    se.save_info_files()
    se.file_clone_factory()
    se.set_to_index()
