""" Se conecta a Drive """

try:
    from .base_api import ServiceAPI
except:
    from base_api import ServiceAPI

import io
from googleapiclient.http import MediaIoBaseDownload
from os import path


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
