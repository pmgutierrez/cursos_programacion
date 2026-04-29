#if= es genara una condicion con la logica de true/false.
#if sirve para: saber que quiero detectar, que valores tengo dentro de ese conjunto y tambien puede generar comparaciones a esos datos.
#los condicionales usan operadores para comporar
#== exactamente igual...
#!= distinto o desigual. Campos vacios,errores,valores no permitidos.
#mayor > si es mayor o igual >=
#menor < si es menor o igual <=

#nota=float(input("Ingrese su nota"))

#if nota>=70:
    #print('Usted esta aprobado')
#else:print('Usted es un burro')

# Usamos menos 70pts burro, 70 aprobado y mas 70 zafaste bien.

#notas=int(input('Indique su nota: '))

#if notas >70:
   # print("USTED PROMOCIONO LA MATERIA SATISFACTORIAMENTE")
#elif notas==70:
    #print('USTED SOLAMENTE APROBO')

#else:print('USTED DEBE SEGUIR INTENTANDO')

#DOS VARIABLES.
#edad=20
#anotado=True



#if edad>=18:
#print("Puedo anotarse a la materia Programacion.")
#else:print("No tiene edad suficiente para anotarse.")

name=input("Ingrese su nombre: ")
age=int(input("Ingrese su edad: "))

if age>=21:
    print(f"Hola {name}, usted es mayor a 21")
else: print(f"Hola {name},usted es menor a 21 ")

edad_jubilarse= 65 - age

if edad_jubilarse>=0:
    print(f" te faltan {edad_jubilarse} años")
else: print(f"usted tiene edad para jubilarse.")

#condicional desigual o distinto != . Operador logico sirve para separar datos.

tipo_socio="normal"

if tipo_socio != 'vip':
    print("Los socios que me genero la busqueda son normales.")
else:print(" al final era false.")

edades=[23,43,36,19,33,19,19]

#quiero que me muestre solo los valores que no estan repetidos.

#for edad in edades:
 #   if edad !=19:
 #       print(edad)

cliente={
"nombre":"Ana",
"saldo":1200

 }

#Verificar si ana tieen saldo 0.

if cliente["saldo"]!=0:
    print("Saldo se descontara para pagar la tarjeta.")

datos=['Roberto',[8,7,6],"Pergamino"]

if datos[1][2]!=6:
    print('Notas diferentes de 6')

#AND(y): unir dos condiciones.Doble filtro de datos.
#Or(o): tengo dos condiociones para comparar datos. 

edad=28 
nombre='Agustin'
ventas=12000

if edad>30:
    print("Es mayor 30")
elif edad>=18:
    print("es mayor a 18")
else:print("Es menor a 18.")

if nombre !="":
    print("Campo cargado correctamente")
else:print('Campo obligatorio')

if nombre != None:
    print("Dato correcto")

#while: bucle. Repite bloques de codigo mientras la condicion sea verdadera o true. while= mientras. 
contador=1
while contador <=5:
    print("Numero: ",contador)
    contador += 2
