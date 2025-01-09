from colorama import Fore
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
        print("Are you an admin? Type " + Fore.CYAN,"1" + Fore.RESET," for yes or " + Fore.CYAN,"2" + Fore.RESET," for no.")
        admin = input("Admin?: ")
        print(str(admin))
        while(admin != '1' and admin != '2'):
            print(Fore.RED,"Invalid choice entered. Please try again." + Fore.RESET,"")
            admin = input("Admin?: ")
        return self.__dao.register(username, password, admin)