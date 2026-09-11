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

    def add_paciente(self, dni, nombre, apellido, fecha_nacimiento, direccion, telefono):
        self.data_access.cursor.execute('''
            INSERT INTO pacientes (dni, nombre, apellido, fecha_nacimiento, direccion, telefono)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (dni, nombre, apellido, fecha_nacimiento, direccion, telefono))
        self.data_access.commit()

    def get_paciente_by_dni(self, dni):
        self.data_access.cursor.execute('''
            SELECT * FROM pacientes WHERE dni = ?
        ''', (dni,))
        return self.data_access.cursor.fetchone()