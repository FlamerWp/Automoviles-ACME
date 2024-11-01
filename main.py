from models.model import registrarVehiculo

carro = {}
while True:
    print ("1). Registrar vehiculos")
    print ("2). Registrar ventas")
    print ("3). Lista de los vehiculos en exhibicion")
    print ("4). Reporte de vehiculos vendidos")
    print ("0). Saliendo")

    opc = input("Ingrese una opcion ")

    match opc:
        case "1":
            registrarVehiculo(carro)
        case "2":
            print("Segundo opcion")
        case "3":
            print("Tercero opcion")
        case "4":
            print("Cuarta opcion")
        case "0":
            print ("Saliendo")
            break
        case _:
            print ("Selecciones una opcion valida")
            