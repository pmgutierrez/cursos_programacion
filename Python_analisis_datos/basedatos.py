import sqlite3 # importo la biblioteca.
# Conectar al archivo que contiene la base de datos.

con=sqlite3.connect("peliculas.db")

#cursor:permitia dar ordenes para empezar a utilizar los comandos sql.

cur= con.cursor()

#crear la primera tabla de mi base datos peliculas.
#CREATE: comando de sql que crea.
#TIPO DE VALORES: TEXT: campos que tienen texto.INTEGER: numero entero.REAL: permite valores con decimales.
                 
#execute: ejecuta las ordenes dadas por el cursor.

cur.execute(""" CREATE TABLE IF NOT EXISTS movie(
            title TEXT,
            year INTEGER,
            score REAL)
        """)

#CARGA DE DATOS.

data_peliculas=[
    ("Monty Python and Holy Grail",1975,8.8),
    ("And now For Something",1971,7.5),
    ("Monty Python live at Hollywood Bowl",1982,8),
    ('Monty Python the meaning of life',1983,7.5),
    ('Monty Python Life of Brian',1979,10)
]

#Insertar datos en la tabla movie.
#INSERT: permite insertar datos en las tablas. 
#INSERT INTO ...NOMBRE DE LA TABLA... VALUES()
#executemany: ejecutar varias ordenes.
#commit(): guardar los datos permanentes en los discos.

cur.executemany("""INSERT INTO movie VALUES(?,?,?)""",data_peliculas)

con.commit()
print("Los datos fueron cargados.")

#SELECT: me permite seleccionar un conjunto de datos dentro de la base.

for row in cur.execute("SELECT title,year FROM movie"):
    print(row)

con.close()