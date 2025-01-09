import repository.storeDAO as dao

class Authentication:

    def __init__(self):
        self.__dao = dao

    @property
    def dao(self):
        return self.__dao

    def login(self):
        username = input("To login, please enter your username: ")
        password = input("Enter password: ")
        return self.__dao.login(username, password)


    def register(self):
        username = input("To register, please enter your username: ")
        password = input("Enter a password: ")
        return self.__dao.register(username, password)