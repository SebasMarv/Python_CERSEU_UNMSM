"""
Condicional
Condicional Simple: Evaluar verdad
Bicondicional: Evaluar verdad y falso
Condicional Anidado: Evaluar varios terminos de verdad 
"""

numero = 10
#indicar si es positivo
if numero>0:
    print('Numero positivo')


numero = -10
#indicar si es positivo o negativo
if numero>0:
    print('Numero positivo')
else:
    print('Numero negativo')


numero = 0
#indicar si es positivo o negativo o neutro
if numero > 0:
    print('Numero positivo')
elif numero < 0:
    print('Numero negativo')
else:
    print('Numero neutro')
    

print('------------------------------------')
"""
Ingresar Datos de empleado: nombre, horas trabajo, pago hora, sistema de pensiones y calcular
sueldo básico, descuento y sueldo neto.
"""

def problemaCondicional(nombre,horas,pago,pensiones):
    basico = horas * pago
    if pensiones=='ONP':
        descuento=basico*0.12
    else:
        descuento=basico*0.13
    neto=basico-descuento
    print('Empleado: ',nombre)
    print('Sueldo basico: S/',basico)
    print('Descuento: S/',round(descuento,1))
    print('Sueldo Neto: S/',round(neto,1))

problemaCondicional('Juan Jose',80,30,'ONP')
problemaCondicional('Juan Alonso',80,30,'AFP')

print('---------------------------------------')

"""
Una tienda ha puesto en oferta la venta de un producto ofreciendo un 11% de
descuento sobre la cantidad mayor de 10 a llevar. Diseñe un algoritmo que determine el
importe de la compra, el importe del descuento y el importe a pagar por la
compra de cierta cantidad de unidades del producto.
"""
def problema5(producto,cantidad,precio):
    subtotal=cantidad*precio 
    descuento=0
    if cantidad>10:
        descuento=subtotal*0.11
    total=subtotal-descuento 
    print("Producto ",producto)
    print("Subtotal es s/",subtotal)
    print("Descuento es s/",descuento)
    print("Total es s/",total)

problema5("Laptop",10,5600)
problema5("Laptop",15,5600)