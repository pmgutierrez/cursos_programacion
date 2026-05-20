from flask import Flask #flask es un framework de python que me permite crear app de html mas python.

app=Flask(__name__)#a traves de la variable creamos la app. Flask mas __name__ metodo que me permite leer los recursos y archivos que tengo dentro de la app.
#la ruta principal siempre va a estar declarada de esta manera ("/"). Define el url que compronde esa ruta.
@app.route("/") #@app.route es mi primera ruta para acceder a mi url con mi servidor local.
def inicio():
    return "Hola a todos"

@app.route("/bienvenido")
def bienvenido():
    return "<h1>Mi pagina Web</h1>"
#si envio valores o datos a traves de un formulario por ej aclaro que voy usar metodos de envio POST y GET.
#@app.route("/formulario", methods=["POST","GET"])
#def login()
    

app.run(debug=True)