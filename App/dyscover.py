from Google import Drive
import Settings
from Models import SourceModel, ResourceModel

class SeekAndExecute:

    def get_id_from_url(self, url):
        return url.split('/')[-1]

    def get_files_info_in_forlder(self, id):
        drive = Drive(Settings.SECRETS_PATH, Settings.DRIVE_SCOPES)
        return drive.get_files(id);

    def save_info_files(self):
        folders = SourceModel.select()
        for folder in folders:
            folder_id = self.get_id_from_url(folder.drive)
            data_items = self.get_files_info_in_forlder(folder_id)
            for item in data_items:
                if not '.folder' in item.get('webViewLink'):
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

                    if resource and not created:
                        ResourceModel.update(**defaults).where(ResourceModel.fileId == fileId)

if __name__ == "__main__":
    se = SeekAndExecute()
    se.save_info_files()
