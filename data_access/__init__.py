import sqlite3
from data_access.repository_factory import RepositoryFactory

# Singleton
class DataAccess:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(DataAccess, cls).__new__(cls)
        return cls.__instance

    def __init__(self) -> None:
        self.__connection = sqlite3.connect('database/database.db')
        self.cursor = self.__connection.cursor()

        self.repository_factory = RepositoryFactory(self)
        self.paciente_repository = self.repository_factory.get_paciente_repository()
        self.historia_repository = self.repository_factory.get_historia_repository()
        self.cita_repository = self.repository_factory.get_cita_repository()

    def commit(self):
        self.__connection.commit()

    def close_connection(self):
        self.__connection.close()
