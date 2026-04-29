#variables.... guardan informacion.
#variables numericas.
edad=48
experiencia=5

#variables texto o caracteres.
nombre= 'agustin' 
curso= "python"

#variables booleanas.

perfil_activo=True
jubilado=False

#variables con decimales llamadas float.

estatura= 1.85
peso=94.5

#metodos que tiene python para tabular los valores de las variables de manera unica. 
#sintaxis de los metodos: variable.metodo()

#1-lower pasar un texto  a minuscula.

nombre1="AGUSTIN"

print(nombre1.lower())
print("HOLA A TODOS".lower())

#2-upper pasa todo el texto a mayuscula.
ciudad="pergamino"
print(ciudad.upper())
print(f"La ciudad en donde naci y resido: {ciudad.upper()}")

#3-title primera letra de cada palabra sea mayuscula.

frase="el curso es python en Datos"

print(frase.title())

#4-strip borra espacio al principio y al final.

palabra=" python "

print(palabra.strip())

#5-replace reemplaza texto.

cambio="Me gusta Javascript"

print(cambio.replace("Javascript","python"))

#6-count cuantas veces aparece un carectar o numero.

fruta="banana"

print(fruta.count("a"))
print(fruta.count("n"))
print(fruta.count("z"))

# 7 Join une texto.

colores=["rojo","azul","verde"]

print(" ".join(colores))

#8 split separar las elementos del string y armar una lista.

frutas="manzana,pera,guinda"

print(frutas.split(","))

#9 len cantidad de caracteres.

nombre2=' traumatologo '

print(len(nombre2.strip()))


#name=input("Ingrese su nombre aqui: ")
#name=name.strip().title()

#print(f"El nombre ingresado es {name}")

#10 find busca una palabra o la posicion.

text= "Estamos con mis alumnos de Python aprendiendo metodos."

print(text.find("Python"))

registro="  JUAN,PEREZ ,35 ,buenos Aires"

#limpiar los espacios.

registro1=registro.strip().split(',')
print(registro1)

#separar los datos.





#limpia por ciudad.

ciudad=registro1[3].strip().title()
print(ciudad)