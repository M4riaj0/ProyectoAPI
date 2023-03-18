def pedirDepartamento():
    # Pide al usuario el nombre del departamento
    departamento = input("Por favor, ingrese el nombre del departamento: ")

    return departamento.upper()

def pedirMunicipio():
    # Pide al usuario el nombre del municipio
    municipio = input("Por favor, ingrese el nombre del municipio: ")

    return municipio.upper()

def pedirCultivo():
    # Pide al usuario el nombre del cultivo
    cultivo = input("Por favor, ingrese el nombre del cultivo: ")
    print("\n")
    cultivo = cultivo.lower()  # convierte todas las letras a minúsculas
    return cultivo.capitalize()

def pedirNumRegistros():
    while True:
        num_registros = input("Ingrese el número de registros que desea consultar (máximo 10000): ")
        try:
            num_registros = int(num_registros)
            if num_registros > 0 and num_registros <= 10000:
                return num_registros
            else:
                print("Por favor ingrese un número entre 1 y 10000.")
        except ValueError:
            print("Por favor ingrese un número válido.")

