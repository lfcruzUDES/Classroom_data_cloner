""" Documento de testeo de la clase Drive """

import unittest

import googleapiclient

from gdrive import Drive


class Drive_Test(unittest.TestCase):
    """ Testeo de la clase Drive """

    def setUp(self):
        self.drive = Drive(
            secrets_path='/home/quattroc/Documentos/python/ScholarshipDocuments/secrets',
            scopes=[
                'https://www.googleapis.com/auth/drive.readonly',
                'https://www.googleapis.com/auth/drive.file'
            ]
        )

    def test_connexion(self):
        """ Prueba la conexión al librode datos."""
        service = self.drive.conn()
        self.assertEqual(type(service).__name__, "Resource")

    def test_download_file(self):
        """ Prueba la extracción de datos. """
        file_id = "1DGw78KwrVWHt9sAQlNaZKjq9otzfMQPv"
        self.drive.donwload_file(file_id, "test_doc.pdf")


if __name__ == "__main__":
    unittest.main()
