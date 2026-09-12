import sqlite3

from data_access.repository import Repository


class PacienteRepository(Repository):
    def __init__(self, data_access):
        super().__init__(data_access)

        # Crear la tabla de pacientes si no existe
        self.data_access.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                dni TEXT NOT NULL,
                nombre TEXT NOT NULL,
                apellido TEXT NOT NULL,
                fecha_nacimiento TEXT NOT NULL,
                direccion TEXT NOT NULL,
                telefono TEXT NOT NULL
            )
        ''')

        self.data_access.commit()

    @staticmethod
    def _mascarar_dni(dni):
        dni = str(dni or '').strip()
        if not dni:
            return ''
        if len(dni) <= 4:
            return '*' * len(dni)
        return f"**{dni[-6:]}"

    @staticmethod
    def _mascarar_texto(valor):
        valor = str(valor or '').strip()
        if not valor:
            return ''
        return f"{valor[0]}***" if len(valor) > 1 else '*'

    @staticmethod
    def _mascarar_telefono(telefono):
        telefono = str(telefono or '').strip()
        if not telefono:
            return ''
        if len(telefono) <= 2:
            return '*' * len(telefono)
        return f"***{telefono[-2:]}"

    def add_paciente(self, dni, nombre, apellido, fecha_nacimiento, direccion, telefono):
        try:
            self.data_access.cursor.execute('''
                INSERT INTO pacientes (dni, nombre, apellido, fecha_nacimiento, direccion, telefono)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (dni, nombre, apellido, fecha_nacimiento, direccion, telefono))
            self.data_access.commit()
        except (sqlite3.Error, TypeError, ValueError) as exc:
            raise ValueError(f'No se pudo registrar el paciente: {exc}') from exc

    def get_paciente_by_dni(self, dni):
        try:
            if not dni:
                raise ValueError('El DNI es obligatorio.')
            self.data_access.cursor.execute('''
                SELECT * FROM pacientes WHERE dni = ?
            ''', (dni,))
            return self.data_access.cursor.fetchone()
        except (sqlite3.Error, TypeError, ValueError):
            return None

    def listar_pacientes_enmascarados(self):
        try:
            self.data_access.cursor.execute('SELECT * FROM pacientes')
            pacientes = self.data_access.cursor.fetchall()
        except sqlite3.Error:
            return []

        pacientes_filtrados = list(filter(lambda paciente: paciente is not None and len(paciente) >= 7, pacientes))
        return list(map(lambda paciente: (
            paciente[0],
            self._mascarar_dni(paciente[1]),
            self._mascarar_texto(paciente[2]),
            self._mascarar_texto(paciente[3]),
            paciente[4],
            paciente[5],
            self._mascarar_telefono(paciente[6]),
        ), pacientes_filtrados))