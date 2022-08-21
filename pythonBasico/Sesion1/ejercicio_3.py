"""
El cálculo del pago mensual de un empleado de una empresa se efectúa de la
siguiente manera: el sueldo básico se calcula en base al número total de horas
trabajadas basado en una tarifa horaria; al sueldo básico, se le aplica una
bonificación del 20% obteniéndose el sueldo bruto; al sueldo bruto, se le aplica
un descuento del 10% obteniéndose el sueldo neto. Escriba un programa que
calcule e imprima el sueldo básico, el sueldo bruto y el sueldo neto de un
trabajador.
"""

def problema3(nombre,horas,tarifa):
    basico = horas * tarifa
    sueldobruto = basico*1.2
    sueldoneto = sueldobruto*0.9
    print('- - - - - - - - - - - - - - - - -')
    print('Empleado ',nombre)
    print('Sueldo basico: S/',basico)
    print('Sueldo Bruto: S/',sueldobruto)
    print('Sueldo Neto: S/',sueldoneto)
    print('- - - - - - - - - - - - - - - - -')

problema3('Juan Jose',80,40)
problema3('Dinosaudio Gonzales',50,10)