"""
4. Escribir un programa que sume los números comprendidos entre
un rango de números ingresados
"""
"""
def problema1(num1,num2):
    suma=0
    if num1<num2:
        for x in range(num1,num2+1):
            print(x)
            suma=suma+x
    else:
        for x in range(num1,num2-1,-1):
            print(x)
            suma=suma+x
    print('\nLa suma es ',suma)

problema1(10,40)
problema1(40,10)
"""
def problema1(num1,num2):
    suma=0
    if num1<num2:
        x=num1
        while x<num2+1:
            print(x)
            suma=suma+x
            x+=1
    else:
        x=num1
        while x>num2-1:
            print(x)
            suma=suma+x
            x-=1
    print('\nLa suma es ',suma)

problema1(10,40)
problema1(40,10)