import presentation
from data_access import DataAccess

presentation.index.show()

data_access = DataAccess()
data_access.close_connection()