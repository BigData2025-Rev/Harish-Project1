from colorama import Fore
import repository.storeDAO as dao

class OrdersHandler:

    def __init__(self):
        self.__dao = dao

    @property
    def dao(self):
        return dao
    
    def history(self, name):
        cursor = self.__dao.get_order_history(name)
        result = list(cursor)
        if(len(result) == 0):
            print(Fore.RED,"No orders found." + Fore.RESET,"")
        else:
            for order in result:
                print("Order: " + str(order["_id"]) + " | Specs: " + order["specs"] + " | Price: " + str(order['price']))