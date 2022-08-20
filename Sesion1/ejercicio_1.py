"""
Ingresar Datos de empleado: nombre, horas trabajo, pago hora y calcular
sueldo básico, descuento 12% y sueldo neto.
"""

def problema1(nombre,horas,pago):
    basico=horas*pago
    descuento=basico*0.12
    sueldo=basico-descuento
    print('- - - - - - - - - - - - - - - - -')
    print('Empleado: ',nombre)
    print('Sueldo basico: S/',basico)
    print('Descuento: S/',descuento)
    print('Sueldo Neto: S/',sueldo)
    print('- - - - - - - - - - - - - - - - -')

problema1('Juan Jose', 30, 40)
problema1('Sebastian Marquez', 100, 35)