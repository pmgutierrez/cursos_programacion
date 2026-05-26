#TRABAJO PRÁCTICO — CRUD CON SQLITE y PYTHON(en clase y terminar en casa)

import sqlite3
conexion=sqlite3.connect("biblioteca.db") #abre o crea la base de datos si no existe y devuelve un objeto "Connection" que se asigna a la variable  "conexion".
cursor=conexion.cursor() #crea un cursor a partir dela conexion SQLite, que se utiliza para ejecutar comandos SQL y manipular la base de datos. El cursor es un objeto que permite interactuar con la base de datos a través de consultas y comandos SQL.
cursor.execute("PRAGMA foreign_keys= ON")
cursor.execute("DROP TABLE IF EXISTS libros")
cursor.execute("DROP TABLE IF EXISTS categorias")
cursor.execute("""
            CREATE TABLE IF NOT EXISTS categorias(
            id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_categoria TEXT NOT NULL UNIQUE
            )""")
cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros(
            id_libro INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            fecha_publicacion DATE,
            id_categoria INTEGER,
            FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria))""")

print("Tablas categorias y libros creadas con exito.")

#INSERTAR DATOS EN LAS TABLAS.
def agregar_libro():
    categorias=[("Aventuras",),("Accion",),("Ciencia Ficción",)]
    cursor.executemany("""INSERT INTO categorias(nombre_categoria) VALUES (?)""",categorias)
    libros=[
    ("El Hobbit","J.R.R. Tolkien","1937-09-21",1),
    ("Dune","Frank Herbert","1965-08-01",3),
    ("El Codigo Da Vinci","Dan Brown","2003-03-18",2),
    ("El Señor de los Anillos","J.R.R. Tolkien","1954-07-29",1),
    ]
    #VALIDAMOS LA INSERCION DE DATOS.
    cursor.executemany("""INSERT INTO libros(titulo, autor, fecha_publicacion, id_categoria) VALUES (?,?,?,?)""",libros)
    conexion.commit()
    print("Datos insertados con exito.")

#CONSULTAR LOS DATOS DE LAS TABLAS.
#Mostrar todos los libros utilizando SELECT.
#Realizar una consulta relacional utilizando JOIN.
#Mostrar título, autor y categoría.
def mostrar_libros():
    query="""SELECT libros.titulo,libros.autor,categorias.nombre_categoria FROM libros
    JOIN categorias ON libros.id_categoria = categorias.id_categoria"""

    cursor.execute(query)
    for fila in cursor.fetchall():
        print(fila) 

#UPDATE edita datos de la tabla.
#Modificar el precio de un libro utilizando UPDATE.
#Guardar cambios utilizando commit().
def modificar_libro():
    cursor.execute("""UPDATE libros SET autor = 'J.R.R. Tolkien' WHERE id_libro = 1""")
    conexion.commit()
    print("Datos actualizados con exito.")

#DELETE elimina datos de la tabla.
#Eliminar un libro utilizando DELETE y WHERE.
def eliminar_libro():
    cursor.execute("""DELETE FROM libros WHERE id_libro = 2""")
    conexion.commit()
    print("Datos eliminados con exito.")

#MOSTRAR RESULTADOS
#Mostrar el estado final de la tabla libros.
def  mostrar_resultados():
    cursor.execute("SELECT * FROM libros")
    for fila in cursor.fetchall():
        print(fila)

#CERRAR CONEXION
def cerrar_conexion():
    conexion.close()

#Hacer un menu para mostrar en pantalla las opciones de CRUD y que el usuario pueda elegir la opcion a realizar.
print("Bienvenido a la biblioteca, elija una opcion: ")
print("1. Agregar libro")
print("2. Mostrar libros")
print("3. Modificar libro")
print("4. Eliminar libro")
opcion=int(input("Ingrese una opcion: "))

if opcion==1:
    agregar_libro()
elif opcion==2:
    mostrar_libros()
elif opcion==3:
    modificar_libro()
elif opcion==4:
    eliminar_libro()
else:
    print("Opcion no valida")









