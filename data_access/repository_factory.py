from data_access.paciente_repository import PacienteRepository
from data_access.cita_repository import CitaRepository
from data_access.usuario_repository import UsuarioRepository

class RepositoryFactory:
    def __init__(self, data_access):
        self.data_access = data_access

    def get_paciente_repository(self):
        return PacienteRepository(self.data_access)

    def get_cita_repository(self):
        return CitaRepository(self.data_access)

    def get_usuario_repository(self):
        return UsuarioRepository(self.data_access)