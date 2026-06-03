from flask import Flask,render_template,request,url_for
import sqlite3

app=Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route('/guardar',methods=['POST'])
def guardar():
    dni=request.form["dni"]
    nombre=request.form["nombre"]
    puesto=request.form["puesto"]
    salario=request.form["salario"]

    conexion=sqlite3.connect('empleados.db')
    cursor=conexion.cursor()

    cursor.execute("""INSERT INTO empleados (dni,nombre,puesto,salario) VALUES(?,?,?,?)""",(dni,nombre,puesto,salario))

    conexion.commit()

    cursor.execute("SELECT * FROM empleados")

    empleados=cursor.fetchall()

    conexion.close()

    return render_template("lista.html",empleados=empleados)
if __name__=="__main__":
    app.run(debug=True)