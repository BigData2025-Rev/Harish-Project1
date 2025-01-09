class Order:

    def __init__(self, user, specs, price):
        self.__user = user
        self.__specs = specs
        self.__price = price
    
    @property
    def user(self):
        return self.__user
    
    @property
    def specs(self):
        return self.__specs
    
    @property
    def price(self):
        return self.__price