#listas: es que se ordenan dentro de [],ordenadas y mutables/permite valores duplicados.

frutas=['manzana','pera','frutilla','kiwi','pera']

print(frutas[4])#busca el elemento por posicion.
frutas[2]='sandia'#cambia el valor.
print(frutas)

#tuple : las tuples se marcan (),ordenas y no mutables/permiten valores duplicados.

rangos=(10,20,40,60)
print(rangos[0])
#rangos[3]=100 es erroneo porque no son mutables.

#diccionarios. estructura de llave: valor. Se encierran entre {}

perfil={
'nombre':'Agustin',
'edad':48,
"altura":1.85,
'profesion':"Instructor"
}

print(perfil['altura'])#trae el valor de la clave altura.
perfil['profesion']="Basquetbolista"#entro a la variable y cambio un valor.
print(perfil)

#Conjuntos: tambien se definen por llaves.No permite elemntos duplicados no esta ordenada. No tiene indice.

deportes={'basket','futbol','rugby','golf','rugby','kodiak'}

print(deportes)