class Madre:
    
    def __init__(self, apellidoMaterno) -> None:
        self.apellidoMaterno = apellidoMaterno

class Padre:
    
    def __init__(self, apellidoPaterno) -> None:
        self.apellidoPaterno = apellidoPaterno

class Hijo(Madre, Padre):
    
    def __init__(self, apellidoPaterno, apellidoMaterno):
        Padre.__init__(self, apellidoPaterno)
        Madre.__init__(self, apellidoMaterno)

Jorge = Hijo("Suarez", "Martinez")
print(Jorge.apellidoMaterno)
print(Jorge.apellidoPaterno)