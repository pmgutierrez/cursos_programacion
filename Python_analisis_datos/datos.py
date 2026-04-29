# carga de datos.
# pedir datos? inputs.
#guardar datos? lista.
# valores combinados usamos diccionarios.

def agregar_personas(personas):
    nombre=input("Cargar nombre: ")
    edad=int(input('Cargar edad: '))

    personas.append({
        "nombre":nombre,
        "edad":edad
    })

personas=[]

for i in range(3):
    print('Vuelta: ',i + 1)
    agregar_personas(personas)


print('\n Listado: ')
for persona in personas:
    print(persona['nombre'], persona['edad'])




