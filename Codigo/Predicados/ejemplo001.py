
def unificar(term1, term2, unificador):
    if term1 == term2:
        return True
    elif term1[0] == '?' and term2[0] != '?':
        unificador[term1] = term2
        return True
    elif term1[0] != '?' and term2[0] == '?':
        unificador[term2] = term1
        return True
    return False

unificador = {}
term1 = "Maria"
term2 = "John"

if unificar(term1, term2, unificador):
    print("Unificacion exitosa!")
    print("Valores asignados:")
    for key, value in unificador.items():
        print(key, "=", value)
else:
print("No se pudo unificar los terminos.")