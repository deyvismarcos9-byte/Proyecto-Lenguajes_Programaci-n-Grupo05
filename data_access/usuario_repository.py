import hashlib
import hmac
import os
import sqlite3

from data_access.repository import Repository


class UsuarioRepository(Repository):
    _ITERACIONES = 260000

    def __init__(self, data_access):
        super().__init__(data_access)
        self.data_access.cursor.execute('''
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre_usuario TEXT NOT NULL COLLATE NOCASE UNIQUE,
                sal TEXT NOT NULL,
                hash_contrasena TEXT NOT NULL
            )
        ''')
        self.data_access.commit()

    def has_users(self):
        self.data_access.cursor.execute('SELECT 1 FROM usuarios LIMIT 1')
        return self.data_access.cursor.fetchone() is not None

    def add_usuario(self, nombre_usuario, contrasena):
        nombre_usuario = str(nombre_usuario or '').strip()
        if not nombre_usuario:
            raise ValueError('El nombre de usuario es obligatorio.')
        if not contrasena or len(contrasena) < 8:
            raise ValueError('La contraseña debe tener al menos 8 caracteres.')

        sal = os.urandom(16)
        hash_contrasena = hashlib.pbkdf2_hmac(
            'sha256', contrasena.encode('utf-8'), sal, self._ITERACIONES
        )
        try:
            self.data_access.cursor.execute('''
                INSERT INTO usuarios (nombre_usuario, sal, hash_contrasena)
                VALUES (?, ?, ?)
            ''', (nombre_usuario, sal.hex(), hash_contrasena.hex()))
            self.data_access.commit()
        except sqlite3.IntegrityError as exc:
            raise ValueError('Ese nombre de usuario ya está registrado.') from exc
        except sqlite3.Error as exc:
            raise ValueError(f'No se pudo registrar el usuario: {exc}') from exc

    def authenticate(self, nombre_usuario, contrasena):
        nombre_usuario = str(nombre_usuario or '').strip()
        if not nombre_usuario or not contrasena:
            return None

        self.data_access.cursor.execute('''
            SELECT id, nombre_usuario, sal, hash_contrasena
            FROM usuarios WHERE nombre_usuario = ?
        ''', (nombre_usuario,))
        usuario = self.data_access.cursor.fetchone()
        if usuario is None:
            return None

        sal = bytes.fromhex(usuario[2])
        hash_ingresado = hashlib.pbkdf2_hmac(
            'sha256', contrasena.encode('utf-8'), sal, self._ITERACIONES
        )
        if not hmac.compare_digest(hash_ingresado.hex(), usuario[3]):
            return None
        return usuario[0], usuario[1]