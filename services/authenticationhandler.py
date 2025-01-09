from colorama import Fore
import repository.storeDAO as dao
import entities.user as userent

class Authentication:

    def __init__(self):
        self.__dao = dao

    @property
    def dao(self):
        return self.__dao

    def login(self):
        username = input("To login, please enter your username: ")
        password = input("Enter password: ")
        result = self.__dao.login(username, password)
        if(result == None): return None
        else: return userent.User(result['name'], result['password'], result['admin'])



    def register(self):
        username = input("To register, please enter a username: ")
        password = input("Enter a password: ")
        print("Are you an admin? Type " + Fore.CYAN,"1" + Fore.RESET," for yes or " + Fore.CYAN,"0" + Fore.RESET," for no.", sep="")
        admin = input("Admin: ")
        while(admin != '1' and admin != '0'):
            print(Fore.RED,"Invalid choice entered. Please try again." + Fore.RESET,"")
            admin = input("Admin: ")
        self.__dao.register(username, password, admin)
        return username, password, admin