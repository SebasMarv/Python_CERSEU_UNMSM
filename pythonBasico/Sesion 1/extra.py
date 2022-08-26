
#Utilizando input y eval
#Eval puede utilizarse para convertir caracteres de una cadena de ingreso
#a una entero o real segun lo ingresado en la entrada.
def planilla():
    empleado = input('Ingrese el nombre del empleado: ')
    horas = eval(input('Ingrese las horas laboradas: '))
    pago = eval(input('Ingrese el pago hora: '))
    basico = horas * pago
    print('Empleado: ',empleado)
    print('Sueldo basico es s/',basico)

planilla()