"""
1. Ingresar producto, costo materia prima, costo mano de obra, otros gastos, cantidad
producida e interés a ganar. 
cantidad < 100 --- 15%
cantidad < 200 --- 12%
cantidad < 300 --- 10%
Mostrar el detalle mas costo de precio de venta de
producto y ganancia.
"""

def problema1(producto,materiaprima,manobra,otros,cantidad):
    costoproduccion = materiaprima + manobra + otros
    if cantidad < 100:
        costototal = costoproduccion * 1.15
    elif cantidad < 200:
        costototal = costoproduccion * 1.12
    else:
        costototal = costoproduccion * 1.1
    precioventa = round(costototal/cantidad,1)
    ganancia=costototal-costoproduccion
    print('Producto: ',producto)
    print('Costo de produccion es: S/',costoproduccion)
    print('Venta total es: S/',round(costototal,1))
    print('Ganancia es: S/',round(ganancia,1))

problema1('Laptop',4500,5000,2500,50)
problema1('Cargador',300,400,100,50)