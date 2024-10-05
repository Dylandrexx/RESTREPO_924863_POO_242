class Customer:
    def __init__(self, name, dni, purchased_car):
        self.__name = name
        self.__dni = dni
        self.__purchased_car = purchased_car

    def get_name(self):
        return self.__name
    def set_brand(self, name):
        self.__name = name    
    def get_dni(self):
        return self.__dni
    def set_dni(self, dni):
        self.__dni = dni     
    
    def __str__(self):
        return f"Customer(name={self.get_name()}, dni={self.get_dni()}"    