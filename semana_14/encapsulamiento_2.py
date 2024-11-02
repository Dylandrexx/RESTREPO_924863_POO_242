#Decoradores

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self,age):
        self.__age = age

person_1 = Person("Marcelita", 18) 

print(person_1.age)