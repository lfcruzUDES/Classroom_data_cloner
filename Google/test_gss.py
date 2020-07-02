""" Documento de testeo de la clase GSS """

import unittest

import googleapiclient

from gss import GSS


class GSS_Test(unittest.TestCase):
    """ Testeo de la clase GSS """

    def setUp(self):
        self.gs = GSS(
            ss_id='1MO_vot62pY2SFnpIfeJLYP2mxrhVC88282MmRHoWlL4',
            range_name='Documentos',
            secrets_path='/home/quattroc/Documentos/python/ScholarshipDocuments/secrets',
            scopes=['https://www.googleapis.com/auth/spreadsheets.readonly']
        )

    def test_connexion(self):
        """ Prueba la conexión al librode datos."""
        service = self.gs.conn()
        self.assertEqual(type(service).__name__, "Resource")

    def test_get_values(self):
        """ Prueba la extracción de datos. """
        datas = self.gs.get_datas()
        self.assertEqual(type(datas), list)


if __name__ == "__main__":
    unittest.main()
