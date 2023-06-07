class Padre:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self):
        return f"{self.nombre} es de apellido {self.apellido}."
    
class Hijo(Padre):

    def __init__(self, nombre, apellido, profesion):
        super().__init__(nombre, apellido)
        self.profesion = profesion

Jorge = Hijo("Juan", "Gonzaga", "Arquitecto")
print(Jorge.apellido)
print(Jorge.profesion)
print(Jorge.saludar())