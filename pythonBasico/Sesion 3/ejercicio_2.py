"""
5. Escribir un programa que pregunte al usuario una cantidad a
invertir, el interés anual y el número de años, y muestre por
pantalla el capital obtenido en la inversión cada año que dura la
inversión.
"""
"""
def problema2(capital,interes,tiempo):
    print('Tiempo \t captital')
    for x in range(1,tiempo+1):
        capital=capital*(1+interes/100)
        print(x,'\t s/',round(capital,1))

problema2(10000,15,10)
"""
def problema2(capital,interes,tiempo):
    print('Tiempo \t captital')
    x=1
    while x<tiempo+1:
        capital=capital*(1+interes/100)
        print(x,'\t s/',round(capital,1))
        x+=1

problema2(10000,15,10)