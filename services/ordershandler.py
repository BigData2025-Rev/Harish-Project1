from colorama import Fore
import repository.storeDAO as dao

class OrdersHandler:

    def __init__(self):
        self.__dao = dao

    @property
    def dao(self):
        return dao
    
    def history(self, name):
        result = self.__dao.get_order_history(name)
        if(len(result) == 0):
            print(Fore.RED,"No orders found.")
        else:
            for order in result:
                print("Order: " + order["ObjectId"] + " | Specs: " + order["specs"] + " | Price: " + str(order['price']))