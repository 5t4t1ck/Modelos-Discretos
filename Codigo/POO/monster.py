class Monster:

    def __init__(self, nombre, categoria):
        self.nombre = nombre
        self.categoria = categoria

    def myFunc(self):
        return "Hey, soy un " + self.categoria

monster1 = Monster("Sullyvan", "Asustador")
print(monster1.nombre, monster1.categoria)
print(monster1.myFunc())

