""" Se conecta a Drive """

try:
    from .base_api import ServiceAPI
except:
    from base_api import ServiceAPI

import io
from datetime import datetime

from googleapiclient.http import MediaIoBaseDownload


class Drive(ServiceAPI):
    api_service = 'drive'
    api_version = 'v3'

    def __init__(self, secrets_path, scopes):
        super().__init__(secrets_path, scopes)

    def donwload_file(self, file_id, file_name='document'):
        """Descarga un documento de Drive, pero no un
        documento de la suit de Google.

        Args:
            file_id (string): ID del documento a descargar.
        """
        request = self.conn().files().get_media(fileId=file_id)
        fh = io.FileIO(file_name, mode='wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            # print(f"{int(status.progress() * 100)}")
        return downloader

    def get_folder_files(self, folder_id):
        """ Obtiene archivos de un folder """
        files_data = []
        page_token = None
        while True:
            response = self.conn().files().list(
                q=f"'{folder_id}' in parents",
                fields='files(id, name, mimeType, webViewLink)',
                pageToken=page_token
            ).execute()
            for file in response.get('files', []):
                files_data.append({
                    'id': file.get("id"),
                    'name': file.get("name"),
                    'mimeType': file.get("mimeType"),
                    'webViewLink': file.get("webViewLink")
                })
            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
        return files_data

    def get_file(self, file_id):
        """ Obtiene un archivo por su ID """
        dFile = self.conn().files().get(
            fileId=file_id,
            fields='id, name, mimeType, webViewLink',
            supportsAllDrives=True
        ).execute()
        return dFile

    def copy_file(self, file_id, name=f'Copied_{datetime.now()}', parents=[]):
        """ Copia un archivo por su ID """
        dFile = self.conn().files().copy(
            fileId=file_id,
            supportsAllDrives=True,
            fields='id, name, mimeType, webViewLink',
            body={'name': name, 'parents': parents}
        ).execute()
        return dFile

    def move_to_forlder(self, file_id, folder_id):
        """ Mueve un archivo de un folder a otro. """
        # Recupera los folders padres a remover.
        file = self.conn().files().get(
            fileId=file_id,
            fields='parents',
            supportsAllDrives=True
        ).execute()
        previous_parents = ",".join(file.get('parents'))
        # Mueve el archivo al nuevo folder.
        file = self.conn().files().update(
            fileId=file_id,
            addParents=folder_id,
            removeParents=previous_parents,
            fields='id, parents',
            supportsAllDrives=True
        ).execute()


if __name__ == '__main__':
    drive = Drive(
        secrets_path=('/home/sit/Documentos/python/'
                      'Classroom_data_cloner/secrets'),
        scopes=[
            'https://www.googleapis.com/auth/drive.readonly',
            'https://www.googleapis.com/auth/drive.file'
        ]
    )
    drive.conn()
