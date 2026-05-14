import sqlite3
from flask import Flask
#Importamos la clase Flask de la biblioteca flask
#Creamos una aplicacion a partir de la variable app
#__name__ es el metodo que me permite leer archivo(app.py)recursos,los templates.
app= Flask(__name__)
conexion=sqlite3.connect("mitienda.db")
cursor=conexion.cursor()


cursor.execute("PRAGMA foreign_keys= ON")

cursor.execute("""CREATE TABLE IF NOT EXISTS Clientes(              id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
               nombre TEXT NOT NULL,
               tel INTEGER NOT NULL,
               dni INTEGER UNIQUE,
               direccion TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS Pedidos(
               id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
               cantidad INTEGER,
               precio REAL,
               descripcion TEXT,
               id_cliente INTEGER,
               FOREIGN KEY (id_cliente)
               REFERENCES Clientes(id_cliente))
""")

print("Tablas creadas con exito.")

#INSERTAR DATOS.

clientes=[
("Ricardo Carrera",1134479755,26184083,"Florida 804"),
("Roberto Goyeneche",1167879755,3985123,"Av. Gavilan 110"),
("Tita Merello",1145903211,2784011,"Av. Santa Fe 1000")
]

cursor.executemany("""INSERT INTO Clientes(nombre,tel,dni,direccion) VALUES (?,?,?,?)
""",clientes)

pedidos=[
    (3,87,"Combo1",2),
    (1,40,"Combo2",1),
    (6,30,"Combo3",3),
    (1,87,"Combo1",1),
    (2,30,"Combo2",2)
]

cursor.executemany("""INSERT INTO Pedidos (cantidad,precio,descripcion,id_cliente) VALUES(?,?,?,?)""",pedidos)

conexion.commit()

print("Datos Insertados")
               
#SELECCION DE DATOS.

print("\nTodos mis clientes")

cursor.execute("SELECT * FROM Clientes")

for fila in cursor.fetchall():
    print(fila)

print("\n Pedidos Mayores a 2")

cursor.execute("SELECT descripcion,precio FROM Pedidos WHERE cantidad > 2 ")

for fila in cursor.fetchall():
    print(fila)

# LIKE trae de datos que coinciden con la condicion. Por ejemplo valores que empiecen con x letra.

print("\n Clientes que empiecen con la letra R ")

cursor.execute("""SELECT nombre,direccion FROM Clientes WHERE nombre LIKE 'R%' """)

print(cursor.fetchall())

#JOIN

print("\n Clientes + Pedidos")

cursor.execute("""SELECT Clientes.nombre,Pedidos.cantidad,Pedidos.descripcion FROM Clientes
               JOIN Pedidos
               ON Clientes.id_cliente= Pedidos.id_cliente""")

for fila in cursor.fetchall():
    print(fila)

cursor.execute("""UPDATE Pedidos SET precio= 50 WHERE
               descripcion="Combo1"

""")

conexion.commit()

print("\nPrecios Actualizados")

cursor.execute("""DELETE FROM Pedidos WHERE cantidad=2

""")
conexion.commit()

print('Pedido eliminado')

conexion.close()