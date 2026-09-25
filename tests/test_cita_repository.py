import sqlite3
import unittest

from data_access.cita_repository import CitaRepository


class CitaRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(':memory:')
        self.connection.execute('CREATE TABLE pacientes (id INTEGER PRIMARY KEY)')
        self.connection.executemany(
            'INSERT INTO pacientes (id) VALUES (?)', ((1,), (2,))
        )
        self.data_access = type('InMemoryDataAccess', (), {})()
        self.data_access.cursor = self.connection.cursor()
        self.data_access.commit = self.connection.commit
        self.repository = CitaRepository(self.data_access)

    def tearDown(self):
        self.connection.close()

    def test_lista_citas_solo_del_paciente_y_en_orden_cronologico(self):
        self.repository.add_cita(1, '2026-10-12', '09:00', 'Control')
        self.repository.add_cita(2, '2026-10-10', '08:00', 'Consulta de otro paciente')
        self.repository.add_cita(1, '2026-10-10', '11:30', 'Seguimiento')

        self.assertEqual(
            self.repository.get_citas_by_paciente_id(1),
            [
                (3, '2026-10-10', '11:30', 'Seguimiento'),
                (1, '2026-10-12', '09:00', 'Control'),
            ]
        )


if __name__ == '__main__':
    unittest.main()