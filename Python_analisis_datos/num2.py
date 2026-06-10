import numpy as np
#FUSION DE ESTRUCTURAS.
#Vamos a fusionar estructuras completas en matrices planas y dos dos direcciones(filas y columnas.)
#Vertical Stack: adherir filas con nuevos registros.Pega matrices una arriba de la otra. Atencion para logar que se unan deben si o si tener las misma cantidad de columnas. Sintaxis es np.vstack()
#Horizontal Stack: Pegar matrices una al lado de la otra. anadir columnas nuevas a mi tabla.Atencion deben tener la misma cantidad de filas. Sintaxis np.hstack()

turno_manana=np.array([[101,8],[28,4]])
turno_tarde=np.array([[202,6],[403,8]])

total_empleados=np.vstack((turno_manana,turno_tarde))

print(total_empleados)

examen_1=np.array([[10],[8],[4]])
examen_2=np.array([[6],[8],[1]])

notas_finales=np.hstack((examen_1,examen_2))

print(notas_finales)

# reshap sirve para cambiar la estructura geometrica de los datos (filas o columnas)sin alterar el valor de esos datos.
pixeles=np.array([255,0,0,0,255,0,0,0,255])
foto=pixeles.reshape(3,3)

print(foto)

produccion_mensual=np.array([50,30,46,98,100,30,47,89,87,90,10,5])

produccion_trimestral=produccion_mensual.reshape(4,3)
print('\nPRODUCCION TRIMESTRAL')
print(produccion_trimestral)