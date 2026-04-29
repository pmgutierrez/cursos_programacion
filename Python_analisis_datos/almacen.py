# Problema: cargo datos.
#como cargo datos 1 paso inputs.
# guardo los datos en un diccionario.
#armo una lista para guardar diccionario.

def agregar_producto(productos):
    nombre=input('Nombre del producto')
    precio=float(input('Precio'))
    stock=int(input('Numero de stock'))

    producto={
        'nombre':nombre,
        'precio':precio,
        'stock':stock
    }
    productos.append()

def mostrar_producto(productos):
    for producto in productos:
        print('Nombre: ',producto['nombre'],'Precio: ',producto["precio"],"Stock: ", producto["stock"])

def separar_precios(productos):
    caros=[]
    ofertas=[]
    for producto in productos:
        if producto['precio']>1000:
            caros.append(producto)
        else:ofertas.append(producto)
    return caros,ofertas

def total_precio_stock(productos):
    total=0
    for producto in productos:
        total= total + producto['precio'] * producto['stock']
    return total

def controlar_stock(productos):
    for producto in productos:
        if producto['stock']>0:
            print(producto["nombre"],producto['stock'])


def vender_producto(productos):
    producto_vendido=input("Producto: ")
    for producto in productos:
        if producto['nombre']==producto_vendido:
            if producto['stock']>0:
                producto['stock'] -= 1
                print('Producto Vendido')
            else:print("No hay stock")
            return
    print("Producto no encontrado.")

opcion = 0    
print("**** Menu - Almacen ****")
print("*   1. Agregar         *")
print("*   2. Mostrar         *")
print("*   3. Separar Precios *")
print("*   4. Total Precios   *") 
print("*   5. Controlar Stock *")
print("*   6. Vender Stock    *")
print("*   7. Salir           *")
print("************************")
opcion = int(input("* Ingrese una opcion: "))
print("************************")
