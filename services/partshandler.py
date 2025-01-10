from colorama import Fore
import repository.storeDAO as dao

class PartsHandler:

    def __init__(self):
        self.__dao = dao

    @property
    def dao(self):
        return dao
    
    def add(self):
        print("\nWe carry parts of type " + Fore.CYAN,"cpu" + Fore.RESET,", " + Fore.CYAN,"gpu" + Fore.RESET,", and " + Fore.CYAN,"motherboard" + Fore.RESET,".", sep="")
        type = input("Which type of part would you like to search for? ")
        while(type != "cpu" and type != "gpu" and type != "motherboard"):
            print(Fore.RED,"Invalid part type specified. Please try again." + Fore.RESET,"")
            type = input("Which type of part would you like to search for? ")
        if(type == "cpu"): result = self.__dao.get_parts("CPU")
        elif(type == "gpu"): result = self.__dao.get_parts("GPU")
        elif(type == "motherboard"): result = self.__dao.get_parts("Motherboard")
        print("\n")
        for part in result:
            print("Brand: " + part['brand'] + " | " + "Model:" + Fore.CYAN,part['model'] + Fore.RESET,"| " + "Type: " + part['type'] + " | " + "Price: " + str(part['price']))
        model = input("\nWhich model would you like to purchase? ")
        result = self.__dao.get_model(model)
        while(result == None):
            print(Fore.RED,"Invalid model specified. Please try again." + Fore.RESET,"")
            model = input("Which model would you like to purchase? ")
            result = self.__dao.get_model(model)
        print(Fore.GREEN,"Part added to cart!" + Fore.RESET,"")
        return result