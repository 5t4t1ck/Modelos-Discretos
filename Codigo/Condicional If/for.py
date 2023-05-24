# personas = ["Juan", "Pedro", "María"]

# for persona in personas:
#     print(persona)

# persona = "Juan"

# for caracter in persona:
#     print(caracter)

# personas = ["Juan", "Pedro", "Felipe", "Juana"]

# for persona in personas:
#     if persona == "Felipe":
#         break
#     print(persona)

# personas = ["Juan", "Pedro", "Felipe", "Juana"]

# for persona in personas:
#     if persona == "Pedro":
#         continue
#     print(persona)

# for x in range(10, 21, 2):
#     print(x)

# for x in range(10, 20, 2):
#     print(x)
# else:
#     print("Se ha terminado la ejecución")

personas = ["Juan", "Maria", "Pedro", "Luis"]
edades = [5, 27, 14, 35]
i = 0
# for persona in personas:
#     for edad in edades:
#         print(persona, edad)

for persona in range(len(personas)):
    print(personas[persona], edades[persona])
    
for edad in range(len(edades)):
    print(personas[edad], edades[edad])