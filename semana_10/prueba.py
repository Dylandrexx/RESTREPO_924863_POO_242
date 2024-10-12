# class Coche:
#     def __init__(self, marca, modelo, año):
#         self.marca = marca
#         self.modelo = modelo
#         self.año = año

#     def __str__(self):
#         return f"Coche: {self.marca} {self.modelo}, Año: {self.año}"

#     def __repr__(self):
#         return f"Coche(marca='{self.marca}', modelo='{self.modelo}', año={self.año})"


# coche1 = Coche("Toyota", "Corolla", 2022)
# coche2 = Coche("KIA", "Picanto", 2020)

# print(coche1)       
# print(repr(coche1))    
# print(coche2)
# print(repr(coche2))

class CuentaBancaria:
    def __init__(self, titular):
        self.titular = titular 
        self.__saldo = 0 

    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print(f"Depósito exitoso de {monto}. Saldo actual: {self.__saldo}")
        else:
            print("El monto a depositar debe ser mayor que 0.")

    def retirar(self, monto):
        if 0 < monto <= self.__saldo:
            self.__saldo -= monto
            print(f"Retiro exitoso de {monto}. Saldo actual: {self.__saldo}")
        else:
            print("Fondos insuficientes o monto inválido para retirar.")

    def mostrar_saldo(self):
        return self.__saldo


cuenta = CuentaBancaria("Juan Pérez")
cuenta.depositar(1000)
cuenta.retirar(500)


saldo_actual = cuenta.mostrar_saldo()
print(f"Saldo actual: {saldo_actual}")
