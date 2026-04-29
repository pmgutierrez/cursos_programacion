#while: bucle que repite contenido si la condicion es true.
#sintaxis: while condicion: 
#            contenido
#          contador(permite que el bucle sume unidades a la variable de inicio.)

numero=5
while numero>=0:
    print(numero)
    numero=numero - 2

suma=0

while suma<=20:
    suma= suma + 3
    print("La suma controlada: ",suma)


#strings: vamos a recorrer una palabra con while.

saludo="hola como estan?"

i=0

while i < len(saludo):
    print(saludo[i])
    i= i + 1

palabra="neuquen"
i= len(palabra)-1 #porque necesito que cuente desde la ultima posicion.

while i >= 0:
    print(palabra[i])
    i= i - 1

mensaje= 'Bienvenido'
contador=0
#quiero que le de la bienvenida 3 veces.

while contador < 3:
    print(mensaje)
    contador= contador + 1

# while+ if: while controlar la repeticion. if decide que accion se toma.
# vamos a buscar numeros pares de un conjunto de numeros.

contador=1
while contador<=20:
    if contador %2==0:
        print("Es numero par: ",contador)
    else:print("Es numero impar: ",contador)
    contador=contador + 1

# la condicion del if es resto de 0 entonces es par.

#while + metodos:

texto=" miercoles "
contador=0

while contador <=2:
    print(texto.strip().upper())
    contador= contador + 1

#while + if + metodos.

frase= "javascript"
contador=1

while contador <=4:
    if contador % 2==0:
        print(frase.upper())
    else:print(frase.title())
    contador= contador + 1

# recorrer variables con varios valores y sabe cuanto va a iterar.

# Sumar ingresos.

ingresos=[10,30,35,40,56]

i=0
total=0

while i < len(ingresos):
    total= total + ingresos[i]
    i= i + 1
print('Mi sueldo en dolares: ',total)

#recorro una lista y trato de encontrar un valor.

productos=[100,200,300,400,500,600]

i=0

while i < len(productos) and productos[i] != 300:
    i= i + 1
print('La posicion de 300 es: ',i)

# lista para recorrer con while y usar operaciones. Para sacar un promedio de variables de una lista.

notas=[8,7,10,5,3,6]

i=0
total=0

while i<len(notas):
    total= total + notas[i]
    i= i + 1
    promedio=total / len(notas)


print('Promedio del alumno: ',promedio)

# while lista if. 
# encontrar aprobados.

notas=[30,55,75,80,98,65,71]

i=0
aprobados=0

while i < len(notas):
    if notas[i]>=70:
        aprobados= aprobados + 1
    i = i + 1

print('Cantidad de alumnos aprobados: ',aprobados)


edades=[10,34,57,12,15,45,21,18]

i=0
mayores=0
menores=0

while i < len(edades):
    if edades[i] >=18:
        mayores= mayores + 1
    else: menores= menores + 1
    i= i + 1

print('Mayores: ',mayores)
print("Menores: ", menores)

# while recorriendo set.

numbers={-4,10,-5,6}

number=list(numbers)

i=0

while i < len(number):
    if number[i]<0:
        print(number[i])
    i += 1

#while diccionarios.

perfil={
    'Agustin':48,
    'Roberto':78,
    'Marta':35
}

claves=list(perfil.keys())

i=0

while i < len(claves):
    nombre= claves[i]
    if perfil[nombre]>=40:
        print(nombre)
    i += 1

# sumar edades.

edades={
'juan': 15,
'Roberto':100,
'Ana':40,
'Ariel':48,
'Caro':78

}

claves=list(edades.keys())

i=0
suma=0

while i<len(claves):
    suma=suma + edades[claves[i]]
    i += 1

print(suma)
