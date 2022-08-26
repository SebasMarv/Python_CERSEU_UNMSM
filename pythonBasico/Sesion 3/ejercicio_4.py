"""
7. Para el cálculo del valor de la amortización nos estamos
refiriendo exactamente a la renta o pago periódico que se
debe hacer para pagar los intereses y reducir la deuda y se
utiliza las fórmulas de las anualidades vencidas.
"""

def problema4(deuda,tiempo,interes):
    interes=interes/100
    renta=(deuda*interes)/(1-(1+interes)**(-1*tiempo))
    print('Periodo \tRenta \tInteres \tAmortizacion \tSaldo')
    for x in range(1,tiempo+1):
        montointeres=deuda*interes
        amortizacion=renta-montointeres
        deuda=deuda-amortizacion
        print(x,'\t s/',round(renta,1),'\t s/',round(montointeres,1),'\t s/',round(amortizacion,1),'\t s/',round(deuda,1))

problema4(500000,5,8)