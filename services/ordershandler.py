from colorama import Fore
import repository.storeDAO as dao

class OrdersHandler:

    def __init__(self):
        self.__dao = dao

    @property
    def dao(self):
        return dao
    
    