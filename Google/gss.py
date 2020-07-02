""" Spreadsheets """

try:
    from .base_api import ServiceAPI
except:
    from base_api import ServiceAPI


class Gss(ServiceAPI):
    """ This functions manages conexion and data manipulation. """

    api_service = 'sheets'
    api_version = 'v4'

    def __init__(self, secrets_path, scopes, ss_id, range_name,):
        super().__init__(secrets_path, scopes)
        self.ss_id = ss_id
        self.range_name = range_name

    def get_datas(self, ss_id='', range_name=''):
        # Call the Sheets API
        sheet = self.conn().spreadsheets()
        result = sheet.values().get(
            spreadsheetId=self.ss_id,
            range=self.range_name
        ).execute()
        return result.get('values', [])
