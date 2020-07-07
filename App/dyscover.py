from Google import Drive, Gss
import Settings
from Models import SourceModel, ResourceModel, LogsModel
from datetime import datetime
from googleapiclient import errors


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
        """ Guarda los datos de los archivos que se encuentran dentro de
        cada carpeta de classroom almacenada en SourceModel"""
        folders = SourceModel.select().where(SourceModel.status == 1)
        files_saved_len = 0
        for folder in folders:
            folder_id = self.get_id_from_url(folder.drive)
            try:
                data_items = self.drive.get_folder_files(folder_id)
                with Settings.DB.atomic():
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
                            if created:
                                files_saved_len += 1
            except Exception as e:
                LogsModel.create(
                    error=e
                )
            return files_saved_len

    def file_clone_factory(self):
        """ De los datos almacenados en ResourceModel se obtienen
        los ID de los archivos objetivo, se los copy y la copia de
        manda a la carpeta Settings.BOOK_INDEX_URL, de estos se
        obtiene la URL e ID que se guarda en la misma tabla y que
        indica que ya se han creado las copias y evita que en la
        próxima iteración se hagan más copias. """
        files = ResourceModel.select().join(SourceModel).where(
            ResourceModel.repoFileId.is_null(True)
        ).where(
            ResourceModel.source.status == 1
        )

        for file_data in files:
            cloned_files = 0
            with Settings.DB.atomic():
                if not 'concentrado' in file_data.name.lower().strip():
                    file_id = file_data.fileId
                    file_name = file_data.name
                    slug = file_data.source.slug
                    new_name = f'{slug}_{file_name}'
                    try:
                        new_file = self.drive.copy_file(
                            file_id=file_id,
                            name=new_name,
                            parents=[Settings.REPO_FOLDER_ID]
                        )
                        file_data.repoFileId = new_file.get('id')
                        file_data.repoViewLink = new_file.get('webViewLink')
                    except errors.HttpError as e:
                        LogsModel.create(
                            error=e,
                            other=f'From: ResourceModel id:{file_data.id} SourceModel:{file_data.source.id}'
                        )
                    else:
                        cloned_files += 1
                        file_data.save()
            return cloned_files

    def set_to_index(self):
        """ Se revisan los registros de la tabla ResourceModel,
        los que estén completos, es decir, que ya hayan sido copiados
        y que por lo tanto tengan llenos los campos de repoViewLink y
        repoFileId, entonces estos registros completos se suben a al
        Spreadsheet Settings.BOOK_INDEX_URL. """
        datas = []
        files = ResourceModel.select().where(
            ResourceModel.ssUploaded == 0
        ).where(
            ResourceModel.repoFileId.is_null(False)
        )

        for row in files:
            datas.append(
                [str(datetime.now()), row.source.plan, row.source.career, row.source.grade,
                 row.source.group, row.source.subject_id, row.source.subject,
                 row.source.teacher, row.name, row.repoViewLink]
            )
        try:
            rows = self.ss.append_datas(datas)
        except Exception as e:
            LogsModel.create(
                error=e,
                other='Error al cargar archivos al index.'
            )
        else:
            update = ResourceModel.update(ssUploaded=True).where(
                ResourceModel.ssUploaded == 0
            ).where(
                ResourceModel.repoFileId.is_null(False)
            )
            update.execute()
        return rows


if __name__ == "__main__":
    print('Iniciando proceso.')
    se = SeekAndExecute()
    print('Guardando los datos de los archivos.')
    se.save_info_files()
    print('Clonando archivos.')
    se.file_clone_factory()
    print('Subiendo datos al Index.')
    se.set_to_index()
    print('Proceso terminado.')
