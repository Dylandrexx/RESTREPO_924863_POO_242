# Inicializamos listas vacías para cada tipo de persona
estudiantes = []
colaboradores = []
seguridad = []

def registrar_persona():
    while True:
        print("Seleccione su rol:")
        print("1. Estudiante")
        print("2. Colaborador")
        print("3. Seguridad")
        print("4. Salir")
        
        opcion = input("Ingrese el número correspondiente: ")
        
        if opcion in ["1", "2", "3"]:
            # Pedimos los datos comunes
            nombre = input("Ingrese su nombre: ")
            identificacion = input("Ingrese su ID: ")
            edad = input("Ingrese su edad: ")
            
            # Creamos un diccionario con la información
            persona = {
                "nombre": nombre,
                "id": identificacion,
                "edad": edad,
                "rol": opcion
            }
            
            # Almacenamos en la lista correspondiente
            if opcion == "1":
                estudiantes.append(persona)
                print(f"Estudiante {nombre} registrado.\n")
            elif opcion == "2":
                colaboradores.append(persona)
                print(f"Colaborador {nombre} registrado.\n")
            elif opcion == "3":
                seguridad.append(persona)
                print(f"Personal de seguridad {nombre} registrado.\n")
        
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Por favor, intente nuevamente.\n")
            continue
        
        # Preguntamos si quiere registrar otra persona
        otra_persona = input("¿Desea agregar otra persona? (si/no): ").lower()
        if otra_persona != "si":
            break

# Llamamos a la función para que inicie el registro
registrar_persona()

# Al finalizar, mostramos las listas con las personas registradas
print("\nPersonas registradas:")
print("Estudiantes:", estudiantes)
print("Colaboradores:", colaboradores)
print("Seguridad:", seguridad)
