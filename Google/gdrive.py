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

    def get_files(self, folder_id):
        files_data = []
        page_token = None
        while True:
            response = self.conn().files().list(
                q=f"'{folder_id}' in parents",
                fields='nextPageToken, files(id, name, mimeType, webViewLink)',
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
