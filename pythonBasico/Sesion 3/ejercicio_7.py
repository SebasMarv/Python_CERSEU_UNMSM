"""
10. Solicitar cedula, nombre y salario de empleados hasta cuando el
usuario lo desee, Si el empleado gana por encima de s/3500 se le
descuenta 13% de su salario. Imprimir para empleado su nuevo
salario o un mensaje en caso de no tener descuento. Imprimir el
total de dinero recogido por los descuentos y el porcentaje de
empleados a los cuales se les realizo.
"""

def problema7():
    resp='S'
    total_desc=0
    cant_empleados=0
    cant_desc=0
    while resp=='S' or resp=='s':
        nombre=input('Ingrese el nombre del empleado: ')
        sueldo=eval(input('Ingrese el sueldo: '))
        cant_empleados+=1 #contar la cantidad de empleados
        if sueldo>3500:
            total_desc=total_desc+sueldo*0.13
            cant_desc+=1 #contar la cantidad de empleados que tienen descuento
            print('Empleado ',nombre,' su nuevo salario es s/',round(sueldo*0.87,1))
        else:
            print('Empleado ',nombre,' Ud. no tiene descuento')
        resp=input('Desea continuar {S/N}')
    print('\nTotal descuento es s/',round(total_desc,1))
    print('Porcentaje de empleados con descuento es ',round(100*(cant_desc/cant_empleados),1))

problema7()
