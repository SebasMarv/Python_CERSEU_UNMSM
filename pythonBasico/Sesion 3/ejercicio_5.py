"""
8. Usted adquiere su crédito de $ 10.000 pagaderos en 3 años con
cuotas semestrales iguales del 12% capitalizare
semestralmente. Hallar el pago semestral y construir el cuadro
de amortización.

El pago de la deuda es de $ 10.000 más los intereses de $
2.201,75 que suman un total de $ 12.201,75
"""

def problema5(deuda,tiempo,interes,modalidad):
    if modalidad=='A' or modalidad=='a':
        interes=interes/100
    elif modalidad=='B' or modalidad=='b':
        interes=interes/200
        tiempo=tiempo*2
    else:
        interes=interes/400
        tiempo=tiempo*4
    renta=(deuda*interes)/(1-(1+interes)**(-1*tiempo))
    print('Periodo \tRenta \tInteres \tAmortizacion \tSaldo')
    for x in range(1,tiempo+1):
        montointeres=deuda*interes
        amortizacion=renta-montointeres
        deuda=deuda-amortizacion
        print(x,'\t s/',round(renta,1),'\t s/',round(montointeres,1),'\t s/',round(amortizacion,1),'\t s/',round(deuda,1))

problema5(500000,5,8,'a')
problema5(500000,5,8,'b')
problema5(500000,5,8,'c')
    