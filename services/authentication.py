import repository.storeDAO as dao

def login():
    username = input("To login, please enter your username: ")
    password = input("Enter password: ")
    dao.login(username, password)


def register():
    username = input("To register, please enter your username: ")
    password = input("Enter a password: ")
    dao.login(username, password)