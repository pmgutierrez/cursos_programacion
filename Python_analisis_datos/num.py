import numpy as np

precios_lista=[100,250,68,90]
precios_iva=[]

for precio in precios_lista:
    precios_iva.append(precio * 1.21)

print(precios_iva)

#Numpy me permite usar estructuras mas rapidas y menos pesadas por ej para calculos matematicos a gran escala.


precios_nplista=np.array([100,250,68,90])#primer array de np. Mantiene homogeneidad de datos.
precios_npiva= precios_nplista * 1.21

print(precios_npiva)
#que pasa cuando no mantengo los valores del mismo tipo.
arreglo_raro=np.array([10,30,4.5])

print(arreglo_raro)

#1 dimension.

dimension_una=np.array([5.5,6.7,10.0,3.8])

#2 dimensiones: columnas y filas. muy usado cuando tenemos base de batos.
#ej: meses: enero/febrero/marzo
dimension_dos=np.array([
[1000,2000,3000], #Vendedor0 
[300,400,5000],#Vendedor1
[500,8000,640]#Vendedor2
])
bloque_ventas=dimension_dos[1:2,2:3]
print('Ventas de marzo ',bloque_ventas)
#dimension3: agregamos otro bloque de datos.
#filas:dias, columnas: cursos(codigo1,codigo2)
dimension_tres=np.array([
[[22,18],[24,19]],
[[34,8],[23,34]]
])
print(dimension_una)
print(dimension_dos)
print(dimension_tres)

#creamos array estructurales.

m_pesos=np.ones((3,5))

print(m_pesos)

#generar id con rangos marcados.

m_rangos=np.arange(100,112)
#generar secuencia de datos. 0 a 24 horas. Cada 6 horas.
m_horario=np.arange(0,24,6)
print(m_rangos)
print(m_horario)

#Dentro del formato filas y columnas buscamos valores especificos. 

# filas pacientes.
#columnas: edad,presion,colesterol

pacientes=np.array([
    [23, 120, 80],#paciente 0
    [87, 135, 900],#paciente 1
    [56,110,76]#paciente 2


])
#quiero saber el colesterol del paciente que tiene edad 87. Dato unico.
paciente_uno=pacientes[1,2]
 
print(paciente_uno)

#Toda columna. todo colesterol.

columna_colesterol=pacientes[:,2]

print(columna_colesterol)

#filas y columnas.Segmentar la matriz.

datos_internos=pacientes[0:2,0:2]

print(datos_internos)

#tablero con sensores.

tablero=np.array([
[0,0,0,0],
[0,9,9,0],
[0,9,9,0],
[0,0,0,0]
])

tablero_on=tablero[1:4,1:3]
print("Tablero encendido: ",tablero_on)

precios_fijos=np.array([19,39,5])
precios_descuento=precios_fijos -2.5

print("Precios descuentos",precios_descuento)

#Podemos combinar dos arrays distintos.Siempre y cuando tengo la misma extension.

ingresos=np.array([5000,7000,9000])
costos=np.array([400,300,850])
ganancias=ingresos - costos

print("Mis ganancias fueron: ",ganancias)

notas=np.array([10,8,5])
tp=np.array([4,5,1])
notas_final=notas + tp
print("notas final :",notas_final)


#Condicionales en numpy: Filtrar y traer datos.
#Como responde numpy a una pregunta: True/False.

# Dentro de un grupo de datos.... detectar deudas mayores a 1000.

deudas=np.array([1000,2000,600,1500,800])

deudas_peligrosas= deudas[deudas>1000]

print("Deudores peligrosos: ",deudas_peligrosas)

temperaturas=np.array([34.5,38.3,34,37.7])

fiebre=temperaturas[temperaturas>= 37.5]
print("Fiebre: ",fiebre)

# Reemplazar valores por error carga o mal armado de la tabla. 

#Detector de valores de velocidad maxima.Velocidad maxima permitida 120.

velocidades=np.array([100,82,130,101,150,120])

#mi radar tiene como limitante de medicion el numero 120.
#si mi radar pasa su limite de medicion... da error.

velocidades[velocidades>120]=120

print("Es todo tuyo Juez de Falta: ",velocidades)

#Datos de crecimiento de poblacion de E-coli.
#y mi dato es que cuando tengo un numero negativo el crecimiento se estanco.

poblacion_ecoli=np.array([22.5,10.2,-99.0,-8.5,39.4,-99.0])

poblacion_ecoli[poblacion_ecoli== -99.0]=0

print('Crecimiento de Ecoli con indicador de estancamiento: ',poblacion_ecoli)

# Segmentacion.Promedio.Limpieza de datos.
#axis=1 la segmentacion es horizontal.Lee filas
#axis=0 la segmentacion es vertical.Lee columnas.

#Tienda 3 sucursales(filas)y 4 dias (columnas)

ventas_locales=np.array([
[1000,3000,5000,7000],
[500,3000,700,150],
[1320,900,8400,8432]
])

#Ventas promedio eligiendo un dia.

promedio_ventas=ventas_locales.mean(axis=0)

print('Promedio de ventas por dia jueves,viernes,sabado y domingo: ',promedio_ventas)

#Sumar ventas por local.

ventas_total=ventas_locales.sum(axis=1)

print('Ventas totales por locales: ',ventas_total)

#Buscar un valor a traves de una funcion pero que la devolucion sea el indice en donde esta ubicado ese valor.
#argmax()

#Mayor indice de inflacion por mes.

inflacion_mes=np.array([2.6,3.4,3.6,2.4,2.3,4.0])

mes_picoinflacion=inflacion_mes.argmax()

print('mes de mayor inflacion: ',mes_picoinflacion)

#Recorridos y condicionales en matrices de 2 dimensiones.
#edad,score,facturacion columnas, filas son los clientes.

tabla_clientes=np.array([
[34,710,1500],
[28,620,2000],
[52,800,4200]
])

columna_facturacion=tabla_clientes[:,2]

#condicion que la facturacion sea mayor a 2500.
#se enmascara en una variable la condicion.
mascara_vip=columna_facturacion>2500
#Luego en otra variable con la condicion recorremos la matriz orignal.
clientes_vip=tabla_clientes[mascara_vip,:]

print(clientes_vip)

#Matriz 3x3 filas de zonas geograficas y columnas con rangos de temperatura.

temperaturas_zonas= np.array([
[22.1,26.4,28.9],
[17.3,21.5,28.1],
[25.,27.3,22.9]
])
#las temperaturas que sean mayores a 25 grados las declaro como MAYORES y el resto NORMAL.

reporte_zonal=np.where(temperaturas_zonas>25,'Alta','Normal')

print(reporte_zonal)

# medicos id antiguedad y rendimiento.

medicos=np.array([
[1001, 3 , 85],
[1002, 5, 95],
[1003,1,70],
[1004,10,92]
])

# Evaluar el rendimiento de estos medicos siendo mayor a 90 el excelente.
# la condicion sera aplicada a la columna numero 2.
#condicion es [:,2]>90

mascara_excelentes=medicos[:,2]>=90

rendimiento_excelente=medicos[mascara_excelentes,:]

print("Medicos premiados: ",rendimiento_excelente)

#Limpieza de datos con una condicion.
#Matriz de ventas semanales. Mi empleado carga datos de dias donde no hay ganancia con numeros negativos.
#Pero el sistema no acepta numeros negativos tira error.
# Agregue una condicion al sistema que reemplaza los numeros negativos por 0.

ventas_cerveceria=np.array([
    [150,-999,300],
    [-999,420,200],
    [180,34,50]
])

ventas_cerveceria[ventas_cerveceria== -999]=0

print('Balance final de fin de semana en los tres turnos',ventas_cerveceria)

#Creciemiento poblacional de un virus en una 3 poblaciones de regiones lejanas entre si.
#el numero de la poblacion esta en millones.
#Tengo que generar un reporte de zonas con Peligro y zonas permitidas. Mas de 25>peligro.


poblacion_virus=np.array([
[22.1,26.5,23.0],
[18.9, 21.5,28.1],
[25.0,27.3,22.9],
])

reporte_seguridad=np.where(poblacion_virus>25.0,'Peligro','Ok')

print('Reporte del Congo: ',reporte_seguridad)

#Valores Maximos y Minimos en matrices dobles entrada fila y columna.

#1 Global: aplastar las matriz y genera un numero puedo el maximo o minimo y te la posicion matriz.

#Ventas 2 locales en Enero,Febrero y Marzo.

sucursales_pergamino=np.array([
    [100,89,190],
    [140,77,290]
])

#Sucursal 0 y 1. Si la "estiro"indices: 0,1,2,3,4,5

mayor_trimestral=np.argmax(sucursales_pergamino)

print("Mayor venta trimestral: ",mayor_trimestral)

#Por columnas. axis=0

#Sucursal con mas ventas.

sucursal_ganadora=np.argmax(sucursales_pergamino,axis=0)

print("Sucursal con mas ventas",sucursal_ganadora)
#tomo las filas.
peores_ventas=np.argmin(sucursales_pergamino,axis=1)

print("Peores ventas:",peores_ventas)

#Peligro del NaN que representa un dato roto,vacio o no del tipo de valor esperado.
#Si yo tengo que calcular el promedio de una matriz y tengo un valor NaN el resultado es NaN

consumo_diario=np.array([
    [120,170],
    [80,np.nan]
])

promedio_diario=consumo_diario.mean()
print(promedio_diario)

#Limpiar datos erroneos.

promedio_diario_real=np.nanmean(consumo_diario)

print('Promedio sin datos erroneos: ',promedio_diario_real)
