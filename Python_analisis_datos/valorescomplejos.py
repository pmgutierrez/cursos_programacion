#listas: es que se ordenan dentro de [],ordenadas y mutables/permite valores duplicados.

frutas=['manzana','pera','frutilla','kiwi','pera']

#print(frutas[4])#busca el elemento por posicion.
frutas[2]='sandia'#cambia el valor.
#print(frutas)

#tuple : las tuples se marcan (),ordenas y no mutables/permiten valores duplicados.

rangos=(10,20,40,60)
#print(rangos[0])
#rangos[3]=100 es erroneo porque no son mutables.

#diccionarios. estructura de llave: valor. Se encierran entre {}

perfil={
'nombre':'Agustin',
'edad':48,
"altura":1.85,
'profesion':"Instructor"
}

#print(perfil['altura'])#trae el valor de la clave altura.
perfil['profesion']="Basquetbolista"#entro a la variable y cambio un valor.
#print(perfil)

#Conjuntos o Set: tambien se definen por llaves.No permite elemntos duplicados no esta ordenada. No tiene indice.

deportes={'basket','futbol','rugby','golf','rugby','kodiak'}

print(deportes)


#Metodos que usan los valores complejos.

productos=['mouse','teclado','monitor']


#append() agrega un elemento a la lista al final.

productos.append('auriculares')
print(productos)



#remove() buscarlo y eliminar elemento.

productos.remove('teclado')
print(productos)

#pop() borrar por posicion.

productos.pop(1)
print(productos)

number=[10,4,29,35,0,10]
#sort() ordenar los numeros de una lista.

number.sort()
print(number)
productos.sort()
print(productos)

#reverse()invertir el orden de los elementos.

number.reverse()
print(number)

#count()me cuenta cuantas veces aparece el valor indicado.

print(number.count(11))

#index()posicion del valor o dato.

print(number.index(10))#posicion 2 
print(productos.index('mouse'))


#len()cantidad total de valores.

print('La cantidad total de productos es:'+ str(len(number)))


#Set...elimina los repetidos.

nombres={'agustin','juan','martin','oriana','juan'}

#add() agrega elementos.

nombres.add('Lucia')
print(nombres)

#remove quita elemento.

nombres.remove('juan')
print(nombres)

#union() une conjuntos.

a={1,2,5,6}
b={2,6,8,10}

print(a.union(b))

#intersection: interseccion entre dos conjuntos valores repetidos entre los dos conjuntos.

print(a.intersection(b))

#Diccionarios.

cliente={
    'nombre':'Hector',
    'saldo':1000,
    'compras':4

}

#keys()llamo a las llaves.
print(cliente.keys())

#values() llamo a los valores.

print(cliente.values())

#items() trae llave y valores
print(cliente.items())

#get() buscar elementos dentro del diccionario. Busqueda segura.
print(cliente.get("compras"))#llamo por llave.
print(cliente.get("Hector"))#llamo por valor.

#update() actualiza algun de los datos.

cliente.update({'compras':10})
print(cliente)
 

 ################PRACTICA##############################


# GESTION DE USUARIOS DE UNA RED.

seguidores={'Ana','Jorge','Juan'}
seguidos={'Juan','Carlos','Estela','Ana'}

#Toda la lista de usuarios.

print(seguidores.union(seguidos))

#quien me sigue y yo sigo. 

print(seguidores.intersection(seguidos))


datos=['juan',30,False]
print(datos)

#Listas dentro de listas.

datos=['juan',[9,12,10],'Pergamino']
print(datos)

print(datos[1])

print(datos[1].sort())

datos[1].sort()
print(datos)

print(datos[1][1])

#lista dentro de un diccionario.

alumno={
'nombre':'Raul',
'notas':[10,3,7]
}

print(alumno['notas'])
print(alumno.values())

valores=list(alumno.values())

print(valores[1])

#PROBLEMA1.

#Armar perfil de alumno que tenga su nombre,notas,cursos y modulos aprobadas.

perfil_alumno={
"nombre":'martin',#str
"notas":[9,8,5,7],#int,lista
'cursos':(" Programacion ","Turno mañana"),#str,tupla
"modulos_aprobados":{"HTML","CSS","Base de datos"}#str,set o conjunto.


}

#Si el dato cambio mucho lista.
#Si el dato queda fijo tupla.
#Si no queres traer valores repetidos set o conjunto.

#Metodos primero lo que voy a chequear es de que tipo son esos datos.

print(perfil_alumno['nombre'].title())

perfil_alumno['notas'].append(4)
notas=perfil_alumno['notas'].append(10)

print(perfil_alumno['notas'])
print(notas)

perfil_alumno['notas'].sort()

print(perfil_alumno['notas'])

perfil_alumno['modulos_aprobados'].add("Javascript")

print(perfil_alumno['modulos_aprobados'])




