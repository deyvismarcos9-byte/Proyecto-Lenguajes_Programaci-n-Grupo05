import presentation
from data_access import DataAccess

if __name__ == "__main__":
    presentation.index.show()

    data_access = DataAccess()
    data_access.close_connection()