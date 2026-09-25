import presentation.views.login as login
from data_access import DataAccess

if __name__ == "__main__":
    data_access = DataAccess()
    login.show(data_access)
    data_access.close_connection()