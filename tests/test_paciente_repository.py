import sqlite3
import unittest

from data_access.paciente_repository import PacienteRepository


class PacienteRepositoryIntegrationTest(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(':memory:')
        self.data_access = type('InMemoryDataAccess', (), {})()
        self.data_access.cursor = self.connection.cursor()
        self.data_access.commit = self.connection.commit
        self.repository = PacienteRepository(self.data_access)

    def tearDown(self):
        self.connection.close()

    def test_registro_y_busqueda_conservan_el_contrato_de_la_vista(self):
        self.repository.add_paciente(
            '12345678',
            'Ana',
            'Gomez',
            '1990-05-17',
            'Calle 1',
            '555-0101'
        )

        paciente = self.repository.get_paciente_by_dni('12345678')

        self.assertEqual(
            paciente,
            (1, '12345678', 'Ana', 'Gomez', '1990-05-17', 'Calle 1', '555-0101')
        )
        self.assertEqual(paciente[0], 1)
        self.assertEqual(paciente[2:], ('Ana', 'Gomez', '1990-05-17', 'Calle 1', '555-0101'))

    def test_busqueda_de_dni_inexistente_devuelve_none(self):
        self.assertIsNone(self.repository.get_paciente_by_dni('99999999'))


if __name__ == '__main__':
    unittest.main()