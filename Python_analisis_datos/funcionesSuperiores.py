#map() recorre y transforma elementos de una lista.

numeros=[3,6,12]

#sumarle a cada elemento 2.

sumados=[]

for numero in numeros:
    sumados.append(numero + 2)

print(sumados)

def sumar(numero):
    return numero + 2

pares=map(sumar,numeros)

print(list((pares)))

#filter: filtra resultados y obtenemos datos de los subconjuntos.

notas=[30,70,98,45,60]

#Aprobados.

aprobados=[]

for nota in notas:
    if nota >=70:
        aprobados.append(nota)

print(aprobados)

#filter.

def aprobar(nota):
    return nota >= 70

aprobados= filter(aprobar,notas)

print(list(aprobados))

#sorted 

lista=[10,8,3,6]

orden=sorted(lista)

print(orden)

# Precios de productos: mayores a 100, descuento de 15% a la lista precios y por ultimo los ordenos.

precios=[100,250,80,400,150,19]

def mayores_100(precio):
    return precio > 100

def descuento(precio):
    return precio * 0.85

mayores= list(filter(mayores_100,precios))

descuentos= list(map(descuento,mayores))

listado_final=sorted(descuentos)

print(listado_final)