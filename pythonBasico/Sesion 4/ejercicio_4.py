"""
4.- Desarrolle un programa que muestre el listado de productos y sus precios. El
cliente selecciona el producto e ingresa la cantidad a llevar. Se muestra el
subtotal, igv y neto de la venta realizada.
"""

def problema4():
    productos=['Laptop','Notebook','Tablet','PC']
    precios=[8500,4500,2500,5500]
    for x in range(len(productos)):
        print(productos[x],' ==> S/', precios[x])
    articulo=input('Seleccione el producto: ')
    cantidad=eval(input('Ingrese la cantidad: '))
    try:
        posicion=productos.index(articulo)
    except:
        posicion=-1
    if posicion==-1:
        print('No vendemos producto')
    else:
        subtotal=cantidad*precios[posicion]
        igv=subtotal*0.18
        total=subtotal+igv
        print('Subtotal s/', subtotal)
        print('Igv s/',igv)
        print('Neto s/',total)

problema4()
