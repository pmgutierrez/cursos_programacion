#funciones transcriben bloques de codigos solo llamando al nombre de la funcion. sintaxis: 
# def nombre de la funcion():
#       bloque de codigo.

def clasificar_edad (edad):
    if edad>=18:
        print("Sos mayor")
    else:print("Sos menor")

clasificar_edad(34)
clasificar_edad(15)
clasificar_edad(67)

def sumar(a,b):
    resultado= a + b 
    return resultado

print(sumar(4,10))

def rango_edad(edad):
    if edad >=18:
        return "Mayor"
    else: return "Menor"

edad= rango_edad(34)
print(edad)

#Recorrer una lista con una funcion.Lista es alumnos y notas. Los valores estan dentro de un diccionario y quiero solo los aprobados en una lista.

def aprobados(alumnos):
    alumnos_aprobados=[]

    for alumno in alumnos:
        if alumno["nota"]>=70:
            alumnos_aprobados.append(alumno['nombre'])
    return alumnos_aprobados
    
alumnos= [{"nombre":"Agustin","nota":100},
            {"nombre":"Martin" ,'nota':80},
            {"nombre":"Eugenia","nota":40}]

print(aprobados(alumnos))

 
    