lista = []

print(type(lista))

lista.append("Colombia")
print(lista)
lista.append("Peru")
lista.append("Brasil")
print(lista)

lista2 = lista.copy()
print(lista2)

lista2.clear()
print(lista2)

lista2 = lista.copy()
print(lista2.count("Brasil"))
lista2.append("Brasil")
print(lista2.count("Brasil"))
print(lista2)

print(len(lista2))
print(lista2[1])
print(lista2[3])
print(lista2[0])
lista2[3] = "Mexico"
print(lista2)

#Eliminar elementos de una lista

lista2.pop()
print(lista2)

lista2.remove("Peru")
print(lista2)

lista2.append("Brasil")
lista2.append("Brasil")
lista2.append("Brasil")
lista2.append("Brasil")
lista2.remove("Brasil")

print(lista2)

lista2[2] = None
print(lista2)

lista3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
lista3.reverse()
print(lista3)

lista4 = ["u", "e", "a", "i", "o", "A"]
lista4.sort()
print(lista4)