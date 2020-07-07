""" Spreadsheets """

try:
    from .base_api import ServiceAPI
except:
    from base_api import ServiceAPI


class Gss(ServiceAPI):
    """ This functions manages conexion and data manipulation.

    Args:

        secrets_path (str): Lugar en el que se encuentran los arvhicos
        con lo secretos, el archivo debe llamarse client_secret.json

        scopes (list[scope, ...]): Alcances de la API de Spreadsheet
        ss_id (str): ID del libro de cálculo

        range_name (str): rango del que se traerán los datos.
    """

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

    def append_datas(self, datas, value_input_option='RAW'):
        body = {
            'values': datas
        }
        result = self.conn().spreadsheets().values().append(
            spreadsheetId=self.ss_id,
            range=self.range_name,
            valueInputOption=value_input_option,
            body=body
        ).execute()
        return result.get('updates').get('updatedRows')
