prop = {}

while True:
    print("Bienvenido al programa de registro\n"
          "1. Ingresar propietarios\n"
          "2. Ver resumen\n"
          "3. Buscar por nit\n"
          "4. salir")
    select = input("Ingrese la opcion que desea: ")
    match select:
        case "1":
            amount = int(input("Ingrese la cantidad de registros: "))
            for i in range(amount):
                print(f"registro {i+1}")
                nit = input("Ingrese NIT: ").upper()
                name = input("Ingrese su nombre completo: ").capitalize()
                phone = int(input("Ingrese su numero telefonico: "))
                car_amount = int(input("Ingrese la cantidad de carros que posee: "))
                cars = {}
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
                    "car_amount": cars,
                }


        case "2":
            if not prop:
                print("Aun no hay propietarios")
            else:
                print("----Resumen General----")
                brum = 0
                for nit, value in prop.items():
                    print(f"registro {nit}\n"
                          f"Nombre: {value['name']}\n"
                          f"telefono: {value['phone']}\n"
                          f"cantidad de vehiculos: {value['car_amount']}\n")
                    for placa, a in value["car_amount"].items():
                        print(f"Placa: {placa}\n"
                              f"Marca: {a['branch']}\n"
                              f"Modelo: {a['modelo']}\n"
                              f"Year: {a['year']}\n"
                              f"state: {a['state']}\n")
        case "3":
            if not prop:
                print("Aun no hay propietarios")
            else:
                search = input("Ingrese su NIT: ")
                if search in prop:
                    si = 0
                    no = 0
                    for nit, value in prop.items():
                        for placa, a in value["car_amount"].items():
                            if a["state"] == "si":
                                si += 1
                            else:
                                no += 1

                    print(f"Impuestos pagados por carro: {si}\n"
                        f"Impuestos sin pagar: {no}\n")
                else:
                    print("No existe registros con ese NIT")

        case "4":
            print("Saliendo del programa")
            break


