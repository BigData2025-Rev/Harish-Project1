class Part:

    def __init__(self, brand, model, type, price):
        self.__brand = brand
        self.__model = model
        self.__type = type
        self.__price = price
    
    @property
    def brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model
    
    @property
    def type(self):
        return self.__type
    
    @property
    def price(self):
        return self.__price