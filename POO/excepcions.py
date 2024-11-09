n=0
while True:
    number_1 = input("Digite un numero: \n")
    number_2 = input("Digite otro numero \n")

    try:
        result = int(number_1)/int(number_2)
        print(f"El resultado es: {result}")

        except Exception as e:
            print(f"Se produjo un error del tipo {e}")

        finally:
            print("Programa terminado")

    result = int(number_1)/int(number_2)

    print(f"")