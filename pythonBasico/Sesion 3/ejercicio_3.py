"""
6. Escribir un programa que ingrese el préstamo, monto de interés
y números de cuotas a pagar. Mostrar el monto total a pagar y
detalle el numero cuota, monto de cuota y saldo del monto total
a pagar.
"""
"""
def problema3(prestamo,interes,cuotas):
    total=prestamo*(1+interes/100)
    montocuotas=total/cuotas
    print('Monto total a pagar S/',round(total,1))
    print('Monto cuota S/',round(montocuotas,1))
    print('\nCuota \t Saldo')
    for x in range(1,cuotas+1):
        total=total-montocuotas
        print(x,'\t s/',round(total,1))

problema3(60000,10,25)
"""

def problema3(prestamo,interes,cuotas):
    total=prestamo*(1+interes/100)
    montocuotas=total/cuotas
    print('Monto total a pagar S/',round(total,1))
    print('Monto cuota S/',round(montocuotas,1))
    print('\nCuota \t Saldo')
    
    x=1
    while x<cuotas+1:
        total=total-montocuotas
        print(x,'\t s/',round(total,1))
        x+=1


problema3(60000,10,25)