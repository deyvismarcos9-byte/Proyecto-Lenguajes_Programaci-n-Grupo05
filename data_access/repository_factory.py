from data_access.paciente_repository import PacienteRepository
from data_access.historia_repository import HistoriaRepository
from data_access.cita_repository import CitaRepository
from data_access.atencion_repository import AtencionRepository

class RepositoryFactory:
    def __init__(self, data_access):
        self.data_access = data_access

    def get_paciente_repository(self):
        return PacienteRepository(self.data_access)

    def get_historia_repository(self):
        return HistoriaRepository(self.data_access)

    def get_cita_repository(self):
        return CitaRepository(self.data_access)

    def get_atencion_repository(self):
        return AtencionRepository(self.data_access)