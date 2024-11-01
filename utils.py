import json 

def abrirArchivoDatos(carro):
    try:
        with open("Json/datos.json", "r") as file:
            datos = json.load(file)
            carro.update(datos)
    except FileNotFoundError:
        carro.update({})

def modificarArchivoDatos(carro):
    with open("Json/datos.json", "w") as outfile:
        json.dump(carro, outfile, indent=4)