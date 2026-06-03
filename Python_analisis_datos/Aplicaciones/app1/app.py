from flask import Flask , render_template, request
 
app=Flask(__name__)

@app.route("/")
def inicio():
    nombre='Agustin'
    edad=48

    productos=[
        "buzo",
        'remera',
        'short'
    ]

    perfil={
        "nombre":'Agustin',
        'dni': 26184083
    }

    return render_template("index.html",
                           nombre=nombre,
                           edad=edad,
                           productos=productos,
                           perfil=perfil
                           )

app.run(debug=True)