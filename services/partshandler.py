from colorama import Fore
import repository.storeDAO as dao

class PartsHandler:

    def __init__(self):
        self.__dao = dao

    @property
    def dao(self):
        return dao
    
    def add(self):
        print("We carry parts of type " + Fore.CYAN,"cpu" + Fore.RESET,", " + Fore.CYAN,"gpu" + Fore.RESET,", and " + Fore.CYAN,"motherboard" + Fore.RESET,".", sep="")
        type = input("What type of part would you like to search for? ")
        while(type != "cpu" and type != "gpu" and type != "motherboard"):
            print(Fore.RED,"Invalid part type specified. Please try again." + Fore.RESET,"")
            type = input("What type of part would you like to search for? ")
        