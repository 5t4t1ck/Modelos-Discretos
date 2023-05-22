tupla = ()
print(type(tupla))

# tupla.append("Juan")
# print(tupla)

tupla1 = ("Juan", "Pedro", "Maria")

print(tupla1.count("Pedro"))
print(tupla1.index("Pedro"))
print(tupla1)
lista = list(tupla1)
print(lista)

lista.append("Mariano")
tupla1 = tuple(lista)
print(tupla1)

print(tupla1[0])

#Range

rango = range(6)
print(rango)
print(type(rango))

# Set
conjunto = {1,2,3,3,3,4,4,4,4,5,5,5,55,5,6,6,6,7,7,8}
print(conjunto)

#Diccionarios

cliente001 = {
    "nombre":"Diego",
    "apellido":"Saavedra",
    "celular": "0993621621",
    "edad": 35
}

print(cliente001["edad"])

cliente001["nombre"] = "Juan"
print(cliente001)

cliente001["estadoCivil"] = "viudo"
print(cliente001)

print(cliente001.get("celular"))

print(len(cliente001))

cliente001.popitem()
print(cliente001)

cliente001.pop("edad")
print(cliente001)

del cliente001["nombre"]
print(cliente001)

cliente002 = cliente001.copy()
print(cliente002)

cliente003 = dict(cliente002)
print(cliente003)

perros = {
  "Tobby":{
    "name": "Tobby",
    "age": 6
    },
  "Leo":{
    "name": "Leo",
    "age": 1
    }
}
print(perros)

Tobby = {
    "name": "Tobby",
    "age": 6
    }
Leo = {
    "name": "Leo",
    "age": 1
    }
perros = {
    "Tobby": Tobby,
    "Leo":Leo
}
print(perros)