class Car:
    def __init__(self, brand, model, year, price):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price
    
    def get_brand(self):
        return self.__brand
    def set_brand(self, brand):
        self.__brand = brand    
    def get_model(self):
        return self.__model
    def set_model(self, model):
        self.__model = model  
    def get_year(self):
        return self.__year    
    def set_year(self, year):
        self.__year = year
    def get_price(self):
        return self.__price
    def set_price(self, price):
        self.__price = price

    def apply_discount():
        pass
    
    def __repr__(self):
        return f"Car(brand={self.get_brand()}, model={self.get_model()}, year={self.__year}, price={self.__price}"           