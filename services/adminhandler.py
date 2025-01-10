from colorama import Fore
import repository.storeDAO as dao

class AdminHandler:

    def __init__(self):
        self.__dao = dao

    def modify(self):
        print("\nCurrent inventory has parts of type " + Fore.CYAN,"cpu" + Fore.RESET,", " + Fore.CYAN,"gpu" + Fore.RESET,", and " + Fore.CYAN,"motherboard" + Fore.RESET,".", sep="")
        type = input("Which type of part would you like to change the price of? ")
        while(type != "cpu" and type != "gpu" and type != "motherboard"):
            print(Fore.RED,"Invalid part type specified. Please try again." + Fore.RESET,"")
            type = input("Which type of part would you like to search for? ")
        if(type == "cpu"): result = self.__dao.get_parts("CPU")
        elif(type == "gpu"): result = self.__dao.get_parts("GPU")
        elif(type == "motherboard"): result = self.__dao.get_parts("Motherboard")
        print("\n")
        for part in result:
            print("Brand: " + part['brand'] + " | " + "Model:" + Fore.CYAN,part['model'] + Fore.RESET,"| " + "Type: " + part['type'] + " | " + "Price: " + str(part['price']))
        model = input("\nWhich model would you like to change the price of? ")
        result = self.__dao.get_model(model)
        while(result == None):
            print(Fore.RED,"Invalid model specified. Please try again." + Fore.RESET,"")
            model = input("Which model would you like to change the price of? ")
            result = self.__dao.get_model(model)
        print("\nBrand: " + result['brand'] + " | Model: " + result['model'] + " | Type: " + result['type'] + " | Price:" + Fore.MAGENTA,str(result['price']), Fore.RESET,"\n")
        while(True):
            try:
                new_price = input("What would you like to set the price to? ")
                self.__dao.change_price(model, int(new_price))
                print(Fore.GREEN,"Price successfully updated!" + Fore.RESET,"")
                break
            except ValueError:
                print(Fore.RED,"You must enter a number." + Fore.RESET,"")
                continue