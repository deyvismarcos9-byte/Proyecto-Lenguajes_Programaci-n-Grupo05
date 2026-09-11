import sqlite3

# Singleton
class DataAccess:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DataAccess, cls).__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        self.__connection = sqlite3.connect('database/database.db')
        self.pacientes_cursor = self.__connection.cursor()

        self.pacientes_cursor.execute('''
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

        self.__connection.commit()

    def add_paciente(self, dni, nombre, apellido, fecha_nacimiento, direccion, telefono):
        self.pacientes_cursor.execute('''
            INSERT INTO pacientes (dni, nombre, apellido, fecha_nacimiento, direccion, telefono)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (dni, nombre, apellido, fecha_nacimiento, direccion, telefono))
        self.__connection.commit()

    def close_connection(self):
        self.__connection.close()
