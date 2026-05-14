# CRUD: CREAT READ UPDATE DELETE
import sqlite3

conexion=sqlite3.connect("empleados.db")
cursor=conexion.cursor()
#antes de crear necesito validar la estructura llave foranea que me permite tablas relacionados.
cursor.execute("PRAGMA foreign_keys= ON")
#DROP BORRA ESTRUCTURAS Y DATOS. DELETE DATOS.
cursor.execute("DROP TABLE IF EXISTS empleados")
cursor.execute("DROP TABLE IF EXISTS departamentos")
#Necesito validar los campos para generar consistencia en la tabla y que los valores no se repitan y en caso de repetirse no los agregue.
#PARA MARCAR EL CAMPO DE VALORES NO REPETIDOS VOY A USAR EL COMANDO UNIQUE.
#CREO UNA TABLA NUEVA PADRE PARA PODER RELACIONAR CON LA TABLA LLAMADA EMPLEADOS.

cursor.execute("""
            CREATE TABLE IF NOT EXISTS        departamentos(
            id_depto INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_depto TEXT NOT NULL UNIQUE
               )""")

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS empleados
               (id_empleados  INTEGER PRIMARY KEY AUTOINCREMENT,
               dni INTEGER UNIQUE NOT NULL,
               nombre TEXT NOT NULL,
               puesto TEXT,
               salario REAL,
               fecha_nacimiento DATE,
               id_depto INTEGER,
               FOREIGN KEY (id_depto) REFERENCES departamentos(id_depto))""")

print('1.Tablas departamentos y empleados creada con existo.')

#INSERTO VALORES.
#primero cargo datos en la tabla departamentos que es mi tabla padre.

sectores=[("Secretario",),("Preceptor",),("Director",)]

cursor.executemany("INSERT INTO departamentos(nombre_depto)VALUES(?)",sectores)


#INSERTAR DATOS DE LA SEGUNDA TABLA.

nuevos_empleados=[
(3000000,'Roberto Galan','Secretario',670,'1910-08-12'),
(4908876,'Gonzalez Rivero','Preceptor',620,'1908-08-08'),
(7542987,'Nacha Guevera','Directora',890,'1925-10-26'),
(4509876,'Ana Martinez','Portera',250,'1960-05-10')
]
#VALIDAMOS LA INSERCION DE DATOS.
cursor.executemany("""INSERT INTO empleados(dni,nombre,puesto,salario,fecha_nacimiento)VALUES(?,?,?,?,?)""",nuevos_empleados)

conexion.commit()# GUARDO LOS DATOS INSERTADOS.
print("2.Datos Insertados correctamente")

#CONSULTAR LAS DOS TABLAS.
#INNER JOIN CONSULTA RELACIONAL.
query="""
SELECT empleados.dni,empleados.nombre,empleados.puesto,empleados.id_depto FROM empleados 
JOIN departamentos 
ON empleados.id_depto = departamentos.id_depto
"""
cursor.execute(query)



#LECTURA DE DATOS.
#fetch all trae varias filas.
#where me permite en la seleccion de datos generar una condicion.
#ORDER BY ORDENA ASC ASCENDENTE Y DESC DESCENDENTE.

cursor.execute("""SELECT nombre,puesto FROM empleados WHERE salario > 620 ORDER BY  salario DESC
""")

for nombre,puesto in cursor.fetchall():
    print(f"{nombre}-{puesto}")

#UPDATE edita datos de la tabla.

# voy a aumentar el sueldo de carlitos gardel 200.

#nuevo_sueldo=1050
#nombre_empleado="Carlos Gardel"

#cursor.execute("""UPDATE empleados SET salario=? WHERE nombre=?""",(nuevo_sueldo,nombre_empleado))
#conexion.commit()



#DELETE borra datos.

#despedimos a nacha guevera por carpeta psiquiatrica.

eliminar_id= 1 #elimina datos buscando el id.

cursor.execute("""DELETE FROM empleados WHERE id_empleados=?
""",(eliminar_id,))

conexion.commit()
print("Empleado con id: ",eliminar_id,"despedido")

print("Estado final de la tabla empleados" )

cursor.execute("SELECT id_empleados,nombre,salario FROM empleados")

for empleado in cursor.fetchall():
    print(f"ID:{empleado[0]},Nombre: {empleado[1]},Salario: {empleado[2]}")

conexion.close()


