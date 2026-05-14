import sqlite3

def agregar_pelis():
    con=sqlite3.connect("blockbuster.db")
    cur=con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Peliculas(
                    title TEXT,
                    year INTEGER,
                    score REAL)""")
    print('Agregue su pelicula y califiquela')
    titulo=input('Nombre de la pelicula: ')
    ano=int(input("Ingrese el ano de estreno: "))
    nota=float(input("Califique la pelicula de 1 a 10: "))

    cur.execute("""INSERT INTO Peliculas VALUES(?,?,?)
        """,(titulo,ano,nota))
    
    con.commit()
    print("Sus datos fueron guardados")
    con.close()

agregar_pelis()