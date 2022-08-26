"""
Ingresar el precio de un producto, la cantidad de cuotas a pagar y el interés
a cobrar.

Mostrar el pago por cuotas, pago neto que pago y diferencia de pago si pagaba
al contado.
"""

def problema8(producto,precio,cuotas,interes):
    #(1+interes/100) calcular interes desde un numero entero 
    precioTotal = precio*(1+interes/100)
    Pcuotas = round(precioTotal/cuotas,1)
    diferencia = precioTotal - precio
    print('Producto: ',producto)
    print('Precio total es S/', precioTotal)
    print('Pago por cuotas: S/',Pcuotas)
    print('Diferencia de pago es: S/', diferencia)

problema8("Laptop",7500,15,10)