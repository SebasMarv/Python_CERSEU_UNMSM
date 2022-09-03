"""
2.- Una deuda de $ 100.000 a 5 años plazo debe pagarse con el siguiente plan de 
amortización cuotas semestrales iguales a la tasa del 10% convertible semestralmente.
Durante el primer año y medio se pagarán solo intereses a partir del cuarto semestre 
se cancelarán las cuotas hasta extinguir su deuda al final de su plazo.
"""

def problema2(deuda,tiempo,interes,selecSemestre):
    interes=(interes/100)/2
    semestres=tiempo*2
    renta=(deuda*interes)/(1-(1+interes)**(-1*(semestres-(selecSemestre-1))))
    print('Periodo\tPago Semestral\tInteres\t         Amortizacion\t Saldo')
    for x in range(1,semestres+1):
        if x<selecSemestre:
            mInteres=deuda*interes
            amortizacion=0
            deuda=deuda-amortizacion
            renta_2=mInteres
            print(x,'\t s/',round(renta_2,1),'\t s/',round(mInteres,1),'\t s/',round(amortizacion,1),'\t         s/',round(deuda,1))
        elif x>=selecSemestre:
            mInteres=deuda*interes
            amortizacion=renta-mInteres
            deuda=deuda-amortizacion
            print(x,'\t s/',round(renta,1),'\t s/',round(mInteres,1),'\t s/',round(amortizacion,1),'\t s/',round(deuda,1))

problema2(100000,5,10,4)