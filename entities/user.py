class User:

    def __init__(self, name, password, admin):
        self.__name = name
        self.__password = password
        self.__admin = admin

    @property
    def name(self):
        return self.__name
    
    @property
    def password(self):
        return self.__password
    
    @property
    def admin(self):
        return self.__admin