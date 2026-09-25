import sqlite3
import unittest

from data_access.usuario_repository import UsuarioRepository


class UsuarioRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.connection = sqlite3.connect(':memory:')
        self.data_access = type('InMemoryDataAccess', (), {})()
        self.data_access.cursor = self.connection.cursor()
        self.data_access.commit = self.connection.commit
        self.repository = UsuarioRepository(self.data_access)

    def tearDown(self):
        self.connection.close()

    def test_guarda_y_autentica_usuario_sin_exponer_contrasena(self):
        self.repository.add_usuario('operador', 'clave-segura-1')

        self.assertTrue(self.repository.has_users())
        self.assertEqual(self.repository.authenticate('OPERADOR', 'clave-segura-1'), (1, 'operador'))
        self.assertIsNone(self.repository.authenticate('operador', 'incorrecta'))

        self.data_access.cursor.execute('SELECT sal, hash_contrasena FROM usuarios')
        sal, password_hash = self.data_access.cursor.fetchone()
        self.assertNotEqual(password_hash, 'clave-segura-1')
        self.assertNotEqual(sal, '')

    def test_rechaza_usuario_duplicado_sin_distinguir_mayusculas(self):
        self.repository.add_usuario('operador', 'clave-segura-1')

        with self.assertRaises(ValueError):
            self.repository.add_usuario('OPERADOR', 'otra-clave-2')

    def test_rechaza_contrasena_corta(self):
        with self.assertRaises(ValueError):
            self.repository.add_usuario('operador', 'corta')


if __name__ == '__main__':
    unittest.main()