# lambda: define a una funcion anonima.

def duplicar(x):
    return x * 2

duplicar(2)

print(duplicar(2))

#pasamos a funcion anonima: se declara con la palabra lambda. 

lambda x: x * 2

f= lambda x: x * 2

f(5)

print(f(5))

def sumar (a,b):
    return a + b


total= sumar(2,10)

lambda a,b: a + b

sumar= lambda a,b:a+b

print(sumar(5,10))

# como utilizar lambda en funciones mas complejas.

def descuento(precio):
    return precio * 0.15

descuento= lambda precio: precio * 0.15

print(descuento(100000))

# Mayores a 18.

def es_mayor(edad):
    return edad >=18

mayor=lambda edad: edad >=18

print(mayor(20))

producto={
    'nombre':'pelota de basket',
    'precio': 1200

}

obtener_nombre= lambda producto: producto["nombre"]

print(obtener_nombre(producto))

#Calcular el total de precio de un producto.

producto={
    'precio': 1000,
    "stock":3
}

total=lambda producto: producto["precio"]* producto['stock']

print(total(producto))

# funciones de orden superior: funcion dentro de otra funcion. Funcion como parametro.

def aplicar(funcion,numero):
    return funcion(numero)

resultado= aplicar(
    lambda numero: numero * 10,8
)

print(resultado)

# Map(): transforma los elementos de la lista. Reemplaza al for.

numeros=[2,4,6]

# quiero multiplicar por dos todas los elementos.

duplicados= list(
    map(
        lambda numeros: numeros * 2,numeros
    )


)

print(duplicados)

