# Singleton
class Business:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Business, cls).__new__(cls)
        return cls.__instance