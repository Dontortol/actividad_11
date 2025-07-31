prop = {}
cars = {}
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
                print(f"registro {i+1}")
                nit = input("Ingrese NIT: ")
                name = input("Ingrese su nombre completo: ")
                phone = int(input("Ingrese su numero telefonico: "))
                car_amount = int(input("Ingrese la cantidad de carros que posee: "))
                for car in range(car_amount):
                    print(f"Registro carro {car+1}")
                    placa = input("Ingrese la placa del vehiculo: ").upper()
                    branch = input("Ingrese la marca del vehiculo: ")
                    modelo = input("Ingrese el modelo del vehiculo: ")
                    year = int(input("Ingrese el año del vehiculo: "))
                    state = input("Impuesto del vehiculo Si/No: ").lower()
                    cars[placa] = {
                        "branch": branch,
                        "modelo": modelo,
                        "year": year,
                        "state": state,

                    }
                prop[nit] = {
                    "name": name,
                    "phone": phone,
                    "car_amount": car_amount,
                }

        case "2":
            print("----Resumen General----")
            for nit, value in prop.items():
                print(f"registro {nit}\n"
                      f"Nombre: {value['name']}\n"
                      f"telefono: {value['phone']}\n"
                      f"cantidad de vehiculos: {value['car_amount']}\n")
                for placa, key in cars.items():
                    print("Carro individual")
                    print(f"Placa: {placa}\n"
                          f"Marca: {key['branch']}\n"
                          f"Modelo: {key['modelo']}\n"
                          f"Year: {key['year']}\n"
                          f"Estado de impuesto: {key['state']}\n")


