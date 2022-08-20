
#Utilizando input y eval
def planilla():
    empleado = input('Ingrese el nombre del empleado: ')
    horas = eval(input('Ingrese las horas laboradas: '))
    pago = eval(input('Ingrese el pago hora: '))
    basico = horas * pago
    print('Empleado: ',empleado)
    print('Sueldo basico es s/',basico)

planilla()