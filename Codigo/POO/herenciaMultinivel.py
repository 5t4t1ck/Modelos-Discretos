class Abuelo:
    
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Padre(Abuelo):
    
    def __init__(self, nombre, apellido, profesion):
        super().__init__(nombre, apellido)
        self.profesion = profesion

class Hijo(Padre):
    
    def __init__(self, nombre, apellido, profesion, especializacion):
        super().__init__(nombre, apellido, profesion)
        self.especializacion = especializacion

Juanito = Hijo("Juan", "Mendoza", "Medico", "Ortodoncia")
print(Juanito.profesion)