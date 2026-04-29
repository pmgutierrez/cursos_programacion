
# for es un bucle que recorre una estructura y me trae los datos. Sintaxis del for: for elemento in bloque
#elemento es la unidad de la estructura.
#bloque es el nombre de la estrutura entera.

for letra in "Python":
    print(letra)

#Ventajas del for: 1- no necesita contador!!!! 2- no tiene condicion. 3- recorre siempre.

numeros=[10,30,45,89]
acumulador = 0

for numero in numeros:
    print(numero)
    acumulador = acumulador + numero
print ('Acumululado: ', acumulador)

# for y metodos.

nombres=['ana','carlos','roberto']


for nombre in nombres:
    print(nombre.title())

# for e if .

enteros=[10,30,10,8,14,40,90]

for e in enteros:
    if e >=18:
        print(e)

for e in enteros:
    if e >=18:
        print("Son mayores a 18 >",e)
    else:print("Son menores a 18 < ",e)

# acumulador y contador.

total=0

for n in [2,15,6]:
    total += n

print('Total lista:', total)

pares=0

for n in [19,10,8,17,21,8]:
    if n % 2==0:
        pares += 1

print('Cantidad de pares:', pares)

#for y diccionario.(muestra contenido diccionario)

perfiles={
    'nombre':'Carlos',
    'edad': 25,
    'Trabajo':'Instructor'
 }

for clave in perfiles.items(): 
    print(clave)

# no solamente el for se usa para recorrer estructuras o conjuntos sino por ej:
#Transforma datos. Genero datos nuevos.

numbers=[4,5,8,10,21]
doble=[]

for n in numbers:
    doble.append(n*2)#append agrega elementos.

print('Imprime dobles:',doble)

#filtrar: con una condicion puedo filtar y generar nuevos conjuntos.Usando if.

datos=[10,30,35,None,4]

for d in datos:
    if d is None:
        print("Dato es invalido.")
    
altos=[]

for a in [150,200,90,70,540]:
    if a > 150:
        altos.append(a)

print(altos)

#acumular: valor final por ej de una suma.

suma=0

for n in [20,4,10]:
    suma= suma + n

print(suma)

# Control del flujo del for: 

for numero in range(10): #range metodo usa rango.
    if numero==7:
        break
print(numero)

#range= repetir n veces.Se usa cuando no tenes lista.

#len= saber tamano. Sirve para saber la cantidad de elemntos.

len([1,3,4]) #resultado 3 elementos.

#enumerate= toma el indice y trae el valor. Sirve por ej para generar un ranking.listado con el indice.

for i,n in enumerate([10,6,7]):
    print(i,n)

#zip: une listas. une datos entre si.

for nombre,edad in zip(["agustin","roberto",'carlos'],[48,101,95]):
    print(nombre,edad)

#max, min y sum=

sum([20,40,30])# salida 90.
max([40,55,90])#salida 90
min([90,10,5])#salida 5.

# quiero saber un numero final= sum,contador.
# quiero armar una nueva lista= append.
#quiero solo algunos datos= condicion uso if.
#quiero que me muestre el indice= enumerate.
# tengo varias listas quiero combinarlas=zip

celsius=[0,10,28,12]
farenheit=[]

for c in celsius:
    f=c*9 / 5 + 32
    farenheit.append(f)
    

print(farenheit)

productos=['buzo','zapatilla','medias']
precios=[20,45,10]

for producto,precio in zip(productos,precios):
    print(producto,precio)

#Contar cuantas veces aparece un dato.

datos=[10,3,2,1,2,50,10,2,1]
repeticion={}

for dato in datos:
    if dato in repeticion: 
        repeticion[dato]+= 1
    else:repeticion[dato]= 1

print(repeticion)


# Analisis de Ventas
#1- Venta total. contador o sum.
#2- ventas mayores a 15 dolares. if condicion.
#3- producto mas vendido. max.
#4- cantidad de productos vendidos.

productos=['pan','leche','gelatina','huevos','leche','huevos','pan','huevos']

precios=[10,20,40,70,20,70,10,70]

total_ventas=0
ventas_altas=[]
repeticion_productos={}

for producto,precio in zip(productos,precios):
    total_ventas= total_ventas + precio

    if precio > 15:
        ventas_altas.append((producto,precio))
    
    if producto in repeticion_productos:
        repeticion_productos[producto] += 1
    else: repeticion_productos[producto] = 1

    mas_vendido=""
    max_cantidad=0

    for producto in repeticion_productos:
        if repeticion_productos[producto]>max_cantidad:
            max_cantidad=repeticion_productos[producto]
            mas_vendido=producto

print('Total de ventas:',total_ventas)
print('Ventas mas altas ',ventas_altas)
print('Producto que mas se repite: ',repeticion_productos)
print('Producto mas vendido: ',mas_vendido)

alumnos=[]