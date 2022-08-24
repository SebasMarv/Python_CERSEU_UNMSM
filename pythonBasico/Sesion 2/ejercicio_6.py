"""
4. Un obrero necesita calcular su salario semanal, el cual se obtiene de
la siguiente manera: Si trabaja 40 horas o menos se le paga un
salario de $16 por hora, si trabaja más de 40 horas se le paga un
salario de $16 por cada una de las primeras 40 horas y un salario de
$20 por cada hora extra
"""

def problema6(horas):
    if horas<=40:
        basico=horas*16
        extra=0
    else:
        basico=40*16
        extra=(horas-40)*20
    neto=basico+extra
    print('Sueldo Basico S/',basico)
    print('Sueldo extra S/',extra)
    print('Sueldo neto S/',neto)
    print('--------------------------------')

problema6(30)
problema6(50)