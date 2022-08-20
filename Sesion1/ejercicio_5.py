"""
Una tienda ha puesto en oferta la venta de un producto ofreciendo un 11% de
descuento sobre el importe de la compra. Diseñe un algoritmo que determine el
importe de la compra, el importe del descuento y el importe a pagar por la
compra de cierta cantidad de unidades del producto.
"""
def problema5(producto,cantidad,precio):
    subtotal = cantidad * precio
    descuento=subtotal*0.11
    total=subtotal-descuento
    print('- - - - - - - - - - - - - - - - -')
    print('Producto: ',producto)
    print('El subtotal es : S/',subtotal)
    print('El descuento es: S/',descuento)
    print('Importe a pagar es: S/',total)
    print('- - - - - - - - - - - - - - - - -')

problema5("Laptop",10,5600)