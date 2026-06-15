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

# reshap sirve para cambiar la estructura geometrica de los datos (flilas o columnas)sin alterar el valor de esos datos.
pixeles=np.array([255,0,0,0,255,0,0,0,255])
foto=pixeles.reshape(3,3)

print(foto)

produccion_mensual=np.array([50,30,46,98,100,30,47,89,87,90,10,5])

produccion_trimestral=produccion_mensual.reshape(4,3)
print('\nPRODUCCION TRIMESTRAL')
print(produccion_trimestral)


#unique es buscar numeros repetidos y sacarlos.Cuando matriz de filas y columnas unique va a aplanar los datos y te devuelve un array plano de 1 dimension.
# si quiero eximinar filas o columnas y detectar valores repetidos tengo que usar axis.

#id_cliente y le voy asignar a ese cliente una zona de registro.

registro_clientes=np.array([
[101,3],
[101,3],
[102,5],
[103,5],
[102,5]

])

#buscar filas unicas y cuantas veces se repiten.

clientes_limpios,repeat=np.unique(registro_clientes,axis=0,return_counts=True)

#print(clientes_limpios)# si no uso axis en el metodo unique me devuelve los datos sin repetir pero es una array plano 1 dimension.

print(clientes_limpios,repeat)

#Fraude: existe fraude cuando un patron de transaccion se repite.

transacciones=np.array([
[500,9],
[500,9],
[120,8],
[130,10],
[500,9]
])

trans_alarm,alarm_detect=np.unique(transacciones,axis=0,return_counts=True)

print(trans_alarm,alarm_detect)

#sort y argsort: sort solo ordena columnas de manera individual. Los valores se mezclan.
#argsort trabaja y elige una columna de referencia y se acomodan las columnas en bloque.

#ordenar listas de precios.

listas_precios=np.array([
[150,200],
[90,110],
[320,150]
])

id_precios=np.sort(listas_precios,axis=0)
print(id_precios)

#Propiedades con un codigo de venta y el valor. Agrego los metros cuadrados.

propiedades=np.array([
[1001,85,110000],
[1002,120,220000],
[1003,45,90000]

]
)
indice_precios=np.argsort(propiedades[:,2])

print(indice_precios)

catalago=propiedades[indice_precios]
print(catalago)

#Tabla de posiciones de un torneo e-sports. Ordeno por partidos ganados. Matriz id equipos, partidos_jugados y partidos ganados.

torneos=np.array([
[1,20,14],
[2,20,18],
[3,20,12],
[4,20,10]
])

tabla_posiciones=torneos[np.argsort(-torneos[:,2])]

print(tabla_posiciones)
#cambios, para probar commit con Marca M
