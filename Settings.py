from peewee import SqliteDatabase
from os import path

BASE_PATH = path.dirname(path.abspath(__file__))

# Google

# Libro de de datos de las Asignaturas >>>
BOOK_EXTRACT_DATAS_URL = 'https://docs.google.com/spreadsheets/d/1o-fIP1zgJbkevkWdw-XiSaG7LsntbbEfQiqlz1KAAkk/edit'
BOOK_EXTRACT_DATAS_ID = '1o-fIP1zgJbkevkWdw-XiSaG7LsntbbEfQiqlz1KAAkk'
SHEET_EXTRACT_DATAS = 'Extracción'
RANGES_EXTRACT_DATA = ['DI', 'IMA', 'NTR', 'GST', 'AT', 'MTA', 'MBA']
SECRETS_PATH = path.join(BASE_PATH, 'secrets')
SS_HEADERS = ['plan', 'career', 'grade', 'group',
              'subject_id', 'subject', 'teacher', 'classroom_url', 'drive_url']
# ------------------------------------ <<<

# Libro Index >>>
BOOK_INDEX_URL = 'https://docs.google.com/spreadsheets/d/1MHU1cbBE93oJNw_edS-3nn9UhuESxsZGIU15y1qAWSs/edit'
BOOK_INDEX_ID = '1MHU1cbBE93oJNw_edS-3nn9UhuESxsZGIU15y1qAWSs'
RANGE_INDEX = 'index'
# ---------- <<<

# Folder donde se guardan los respaldos >>>
REPO_FOLDER_ID = '1pWnBG1YtJF8UsUMs4pOMtQb_9yVLFLfx'
# -------------------------------------- <<<

# SPREADSHEET SCOPES >>>
SS_SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly',
             'https://www.googleapis.com/auth/spreadsheets']
# ------------------ <<<

# DRIVE SCOPES >>>
DRIVE_SCOPES = [
    'https://www.googleapis.com/auth/drive.readonly',
    'https://www.googleapis.com/auth/drive.file'
]
# ----------- <<<


# Documentos excluidos >>>
EXCLUDED_TYPE = ['application/vnd.google-apps.folder']
# --------------------------- <<<

# DB data
DB_NAME = 'subjects_resourses.db'
DB = SqliteDatabase(DB_NAME)
LOCAL_TABLES = [
    'SourceModel',
    'PeriodModel',
    'ResourceModel',
    'LogsModel',
]
