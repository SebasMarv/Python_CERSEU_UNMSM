"""
11. Realizar un programa que simule las jugadas de un
tragamonedas e indicar las jugadas en que gano. El usuario tiene
que ingresar la cantidad de jugadas a jugar. Al final mostrar
también la cantidad de jugadas ganadas y perdidas.
Números al azar:
import random
print("Rango al azar 20 a 50 :",random.randint(20, 50))
"""

import random
def problema9(jugadas):
    ganadas=0
    for x in range(1,jugadas+1):
        num1=random.randint(1,3)
        num2=random.randint(1,3)
        num3=random.randint(1,3)
        if num1==num2 and num2==num3:
            ganadas+=1
            print(f'Jugada {x} = ({num1} - {num2} - {num3}) ====> GANO')
        else:
            print(f'Jugada {x} = ({num1} - {num2} - {num3}) ====> PERDIO')
    print(f'\n Jugadas {ganadas} ganadas')
    print(f'\n Jugadas {jugadas-ganadas} perdidas')

problema9(15)