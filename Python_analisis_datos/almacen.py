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
    productos.append(producto)

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

productos=[]

while True:
    print("\n1.Agregar producto")
    print('2.Mostrar productos')
    print("3.Ver productos especiales y ofertas")
    print("4.Total del stock")
    print('5.Control de stock')
    print('6.Vender producto')
    print("7.SALIR")

    opciones=int(input("Elije una opcion"))

    if opciones == 1:
        agregar_producto(productos)
    elif opciones == 2:
        mostrar_producto(productos)
    elif opciones == 3:
        caros,ofertas=separar_precios(productos)
        print("Productos Especiales: ")
        for caro in caros:
            print(caro['nombre'],caro['precio'],caro['stock'])
        print("Productos en oferta: ")
        for o in ofertas:
            print(o["nombre"],o["precio"],o["stock"])
    
    elif opciones==4:
        print(total_precio_stock(productos))

    elif opciones==5:
        controlar_stock(productos)
    elif opciones==6:
        vender_producto(productos)

    elif opciones==7:
        break



        
