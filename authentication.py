from repository import storeDAO

def login():
    username = input("To login, please enter your username: ")
    password = input("Enter password: ")
    storeDAO.login(username, password)


def register():
    username = input("To register, please enter your username: ")
    password = input("Enter a password: ")
    storeDAO.login(username, password)