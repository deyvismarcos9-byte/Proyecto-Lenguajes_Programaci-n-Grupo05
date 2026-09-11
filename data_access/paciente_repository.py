from data_access.repository import Repository

class PacienteRepository(Repository):
    def __init__(self, data_access):
        super().__init__(data_access)

    def add_paciente(self, dni, nombre, apellido, fecha_nacimiento, direccion, telefono):
        self.data_access.cursor.execute('''
            INSERT INTO pacientes (dni, nombre, apellido, fecha_nacimiento, direccion, telefono)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (dni, nombre, apellido, fecha_nacimiento, direccion, telefono))
        self.data_access.commit()