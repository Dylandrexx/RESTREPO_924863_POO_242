#Clase Abstracta
class Person:
    def __init__(self, dni, name, lastname, age):
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.age = age
        
class Student(Person):
    def __init__(self, dni, name, lastname, age, code):
        super().__init__(dni, name, lastname, age)
        self.code = code
        self.__subjects = []

    def add_subject(self, subject):
        self.__subjects.append(subject)

    def __str__(self):
        return f"Nombre: {self.name}, Codigo: {self.code}, Asignaturas: {self.__subjects}"

class Professor(Person):
    def __init__(self, dni, name, lastname, age, devices, desktop):
        super().__init__(dni, name, lastname, age)
        self.devices = devices
        self.desktop = desktop

    def __str__(self):
        return f"Nombre: {self.name}, Dispositivo: {self.devices}, Puesto de trabajo: {self.desktop}"

student_1 = Student(1234, "Dylan", "Restrepo", 28, 1233333)
professor_1 = Professor(4321, "James", "Montealegre", 32, "Laptop", 16)

student_1.add_subject("Matemáticas")
student_1.add_subject("Física")

print(student_1)
print(professor_1)

