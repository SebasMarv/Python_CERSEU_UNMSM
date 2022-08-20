"""
Una empresa paga a sus vendedores un sueldo básico mensual de S/.300. El
sueldo bruto es igual al sueldo básico más una comisión, que es igual al 9% del
monto total vendido. Por ley, todo vendedor se somete a un descuento del 11%.
Diseñe un programa que calcule la comisión, el sueldo bruto, el descuento y el
sueldo neto de un vendedor de la empresa
"""

def problema7(venta):
    comision=venta*0.09
    sueldo=300+comision
    descuento=sueldo*0.11
    neto=sueldo-descuento
    print('Comision: S/',comision)
    print('Sueldo: S/',sueldo)
    print('Descuento: S/',descuento)
    print('Sueldo neto: S/',neto)

problema7(50000)