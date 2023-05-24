class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre 
        self.edad = edad 

    def __str__(self) -> str:
        return "Este es un objeto de la clase Perro"
    
    def ladrar(self):
        return "Yo soy", self.nombre,"y te muerdo"
    
perro1 = Perro("Leo", 2)
print(perro1.nombre)
print(perro1.ladrar())
print(perro1.__str__())