from utils import abrirArchivoDatos, modificarArchivoDatos

def registrarVehiculo(carro):
    carro.clear()
    abrirArchivoDatos(carro) 

    codigo = input("Ingrese el código del producto: ")
    
    # Verificar si el código ya existe
    if codigo not in carro:
        marca = input("Ingrese la marca del carro: ")
        modelo = input("Ingrese el modelo del carro: ")
        año = input("Ingrese el año del carro: ")
        carro[codigo] = {"Codigo": codigo, "nombreProducto": marca, "nombreProvedor": modelo, "año": año}
        modificarArchivoDatos(carro)  # Guardar los carros en el archivo JSON
        print("Se ha registrado el producto")
    else:
        print("El código del producto ya se encuentra registrado")