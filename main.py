prop = {}

while True:
    print("Bienvenido al programa de registro\n"
          "1. Ingresar propietarios\n"
          "2. Ver resumen\n"
          "5. salir")
    select = input("Ingrese la opcion que desea: ")
    match select:
        case "1":
            amount = int(input("Ingrese la cantidad de registros: "))
            for i in range(amount):
                nit = input("Ingrese NIT: ")
                name = input("Ingrese su nombre completo: ")
                phone = int(input("Ingrese su numero telefonico: "))
                car_amount = int(input("Ingrese la cantidad de carros que posee: "))
                for car in range(car_amount):
                    placa = input("Ingrese la placa del vehiculo: ")
                    branch = input("Ingrese la marca del vehiculo: ")
                    modelo = input("Ingrese el modelo del vehiculo: ")
                    year = input("Ingrese el año del vehiculo: ")


