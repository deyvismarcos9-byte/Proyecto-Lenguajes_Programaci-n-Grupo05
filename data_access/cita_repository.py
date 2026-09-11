from data_access.repository import Repository

class CitaRepository(Repository):
    def __init__(self, data_access):
        super().__init__(data_access)

        # Crear la tabla de citas si no existe
        self.data_access.cursor.execute('''
            CREATE TABLE IF NOT EXISTS citas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                paciente_id INTEGER NOT NULL,
                fecha TEXT NOT NULL,
                hora TEXT NOT NULL,
                motivo TEXT NOT NULL,
                FOREIGN KEY (paciente_id) REFERENCES pacientes (id)
            )
        ''')