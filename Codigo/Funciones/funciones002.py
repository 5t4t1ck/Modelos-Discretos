def saludar(nombre="Juanito", apellido="Peres"):
    print("Hello", nombre, apellido)

def nombreApellido(*nombre):
    print("Su nombre es", nombre)

def nombreApellido2(*nombre):
    print("Su nombre es", nombre[0])

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

def nombreCompleto2(**kwargs):
    print(kwargs["nombre"], kwargs["apellido"])

def funcionLista(lista):
    for el in lista:
        print(el)

if __name__ == "__main__":
    # saludar("Diego", "Lopez")
    # saludar("Juan", "Ramirez")
    # saludar("Pedro")
    # saludar()
    nombreApellido("Diego", "Saavedra", "Garia")
    nombreApellido2("Diego", "Saavedra", "Garia")
    nombreCompleto(nombre="Diego", apellido="Saavedra")
    nombreCompleto2(nombre="Diego", apellido="Saavedra")
    funcionLista(["Diego", "Saavedra", "Juan", "Bautista"])
