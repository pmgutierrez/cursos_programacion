import numpy as np

#TABLA CON PILOTOS DE F1 ID VELOCIDAD Y INFRACCIONES.

pilotos=np.array([
[10,290,2],
[11,310,0],
[12,280,5],
[13,300,2]
])

print("-----TABLA DE PILOTOS-----")
print(pilotos)

nuevo_piloto=np.array([[14,305,1]])

pilotos_actualizados=np.vstack((pilotos,nuevo_piloto))

print('------Listas de pilotos Actualizada Nuevo Turno----')
print(pilotos_actualizados)

#Agregar una columna que me de datos de experiencia de los pilotos en simuladores por ano.

experiencia=np.array([[3],[5],[4],[1],[2]])

dataset_completo=np.hstack((pilotos_actualizados,experiencia))

print("-----Nueva informacion con datos de Anos en simuladores-----")
print(dataset_completo)

#Info que recibo de pista de los puntajes de cada uno de los pilotos en la prueba.

puntajes_prueba=np.array([80,95,40,85,90])

print("FORMA ORIGINAL QUE RECIBO LOS DATOS: ",puntajes_prueba.shape)

#puntajes=puntajes_prueba.reshape(5,1)
#numpy calcule automaticamente la cantidad de filas por datos existentes.

puntajes=puntajes_prueba.reshape(-1,1)

#Auditar las penalizaciones. Que cantidad de errores cometen los pilotos habitualmente y cual es el error mas comun.
# voy a usar unique.
penalizaciones=dataset_completo[:,2]
