from data_access.repository import Repository

class AtencionRepository(Repository):
    def __init__(self, data_access):
        super().__init__(data_access)