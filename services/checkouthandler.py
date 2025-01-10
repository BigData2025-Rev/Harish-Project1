from colorama import Fore
import repository.storeDAO as dao

class CheckoutHandler:

    def __init__(self):
        self.__dao = dao

    @property
    def dao(self):
        return self.__dao
    
    def checkout(self, cart, name, price):
        self.__dao.add_order(cart, name, price)
        print(Fore.GREEN,"Checkout successful! Your order has been saved to your account." + Fore.RESET,"")