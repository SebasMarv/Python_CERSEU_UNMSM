"""
Metodos => procedimiento accion

Funcion => retorna 
"""


def problema1(x0,y0,x1,y1,x):
    return y0+(y1-y0)*(x-x0)/(x1-x0)

problema1(400,1.013,450,1.20,420)

print("Interpolar",problema1(400,1.013,450,1.20,420))


print('--------------------------------------------------')

def problema2(inversion,valorfinal,tiempo):
    tiempo=tiempo*12
    return ((valorfinal/inversion)**(1/tiempo)-1)*100

problema2(500000,625000,1.5)

print('--------------------------------------------------')

def problema3(valorfinal,tiempo,interes):
    interes=(interes/100)/12
    tiempo=tiempo*12
    return valorfinal/(1+interes)**tiempo

print('Resultado',problema3(250000,2,9))

print('--------------------------------------------------')

def problema4(deposito,interes,tiempo,capitalizacion):
    interes=interes/100
    if capitalizacion=='M':
        n=12*tiempo
        interes=interes/12
    elif capitalizacion=='T':
        n=4*tiempo
        interes=interes/4
    elif capitalizacion=='S':
        n=2*tiempo
        interes=interes/12
    return deposito*(1+interes)**n

problema4(15000,4.3,6,'T')

print('--------------------------------------------------')

def problema5(valor,grado):
    if grado=='K':
        res1=valor-273.15
        res2=valor*9/5-459.67
    elif grado=='C':
        res1=valor-273.15
        res2=valor*9/5+32
    else:
        res1=(valor-32)*5/9+273
        res2=(valor-32)*5/9
    return res1,res2

problema5(40,'C')
problema5(40,'K')
problema5(40,'F')

print('--------------------------------------------------')

def sumadivisores(num):
    suma=0
    for x in range(1,num//2+1):
        if num%x==0:
            suma=suma+x
    return suma

sumadivisores(6)
sumadivisores(28)
sumadivisores(496)
sumadivisores(8128)

def numeroperfecto(num):
    if sumadivisores(num)==num:
        print('Es un numero perfecto')
    else:
        print('No es un numero perfecto')

numeroperfecto(6)
numeroperfecto(28)
numeroperfecto(496)
numeroperfecto(8128)
numeroperfecto(8126)#no es

print('--------------------------------------------------')

def amigos(num1,num2):
    if num1==sumadivisores(num2) and num2==sumadivisores(num1):
        print('Numeros amigos')
    else:
        print('No son numeros amigos')

amigos(220,284)
amigos(1184,1210)
amigos(1000,1001)#no

print('--------------------------------------------------')

def problista(lista):
    suma=0
    for x in lista:
        suma=suma+x
    return suma

problista([23,12,24,15])
problista([65,41,52,95])
problista([14,26,25,32,12,52,41,75])

"""
***********Funciones Canonicas***********
"""
print('--------------------------------------------------')

cadena='JuaN JoSe RomERo AliAGA'
print('Mayuscula ==>',cadena.upper())
print('Minuscula ==>',cadena.lower())
print('Primeras letras en mayuscula ==>',cadena.title())
print('Primera letra en mayuscula y el resto en minuscula ==>',cadena.capitalize())
print('Contrario (de minuscula a mayuscula y viceversa) ==>',cadena.swapcase())
print('Centrar ==>',cadena.center(40))
print('Centrar ==>',cadena.center(40,'.'))
print('Izquierda ==>',cadena.ljust(40))
print('Izquierda ==>',cadena.ljust(40,'.'))
print('Derecha ==>',cadena.rjust(40))
print('Derecha ==>',cadena.rjust(40,'.'))


cadena='               JuaN JoSe RomERo AliAGA          '
print('Limpiar espacios en blanco ambos lados:',cadena.strip())


cadena='_______________JuaN JoSe RomERo AliAGA_____________'
print('Limpiar caracter en blanco ambos lados:',cadena.strip('_'))
print('Limpiar caracter en el lado izquierdo:',cadena.lstrip('_'))
print('Limpiar caracter en el lado derecho:',cadena.rstrip('_'))
print('Indicar cuantos veces repite: ',cadena.count('o'))
print('Buscar caracter: ',cadena.find('o'))
print('Buscar caracter a partir de un posicion: ',cadena.find('o',22))
print('Buscar caracter a partir de un posicion: ',cadena.find('o',27,35))
print('Buscar caracter del final al inicio: ',cadena.rfind('o'))
print('Buscar caracter del final al inicio: ',cadena.index('o'))
print('Buscar caracter a partir de un posicion: ',cadena.index('o',27,35))
print('cantidad de caracteres: ', len(cadena))
print('Remplazar caracter: ',cadena.replace('J','x'))
print('extraer a partir de posiciones: ',cadena[12:])
print('extraer hasta una posicion: ',cadena[:12])
print('extraer en el rango de posiciones: ',cadena[12:20])
print('Repetir n veces: ',cadena*3)
print('Separar en lista: ',cadena.split(' '))

#Ingrese nombre,apellido parterno y materno
#Juan, romero aliaga
#Retornar por separado

def problema1_2(empleado):
    nombre=empleado[0:empleado.find(',')]
    paterno=empleado[empleado.find(',')+1:empleado.find(' ')]
    materno=empleado[empleado.find(' ')+1:]
    print('Nombre: ',nombre)
    print('Apellido paterno: ',paterno)
    print('Apellido materno: ',materno)

problema1_2('Juan,Romero Aliaga')
problema1_2('Sebastian,Marquez Vasquez')

"""
Ingrese nombre paterno materno, zona(norte,sur,centro)
turno(mañana,tarde,noche) y sexo(masculino,femenino)
Autogenerar codigo
Primera letra nombre + primera letra paterno + 
Primera letra materna + 3primeras letras de zona+ 1(Mañana) 2(Tarde) 3(Noche)
primera letra de sexo
todo el codigo en mayuscula
Sebastian Marquez Vasquez
"""
def autogenerador(empleado,zona,turno,sexo):
    nom=empleado[0:1]
    pat=empleado[empleado.find(' ')+1:empleado.find(' ')+2]
    posicion=empleado.find(' ',empleado.find(' ')+1)
    mat=empleado[posicion+1:posicion+2]
    zona=zona[0:3]
    if turno.upper()=='MAÑANA':
        turno='1'
    elif turno.upper()=='TARDE':
        turno='2'
    else:
        turno='3'
    sexo=sexo[0:1]
    codigo=(nom+pat+mat+zona+turno+sexo).upper()
    print('Su codigo es: ',codigo)

autogenerador('Juan Romero Aliaga','norte','noche','masculino')

"""
JUAN JOSE ROMERO ALIAGA
obtener por separado cada uno
"""


"""
********************Funciones numericas********************
"""

print('Valor absoluto: ',abs(-3))
print('Potencia',pow(4,3))
print('Raiz N: ',pow(36,1/2))
print('Redondear: ',round(pow(36,1/3),2))
print('Division - resto:',divmod(9,2))
print('Retornar la parte entera: ',int(34.91))
lista=[-23,34,0,130,-3]
print('Valor maximo: ',max(lista))
print('Valor minimo: ',min(lista))
print('Suma total:',sum(lista))

import math
print('Redondear hacia arriba: ',math.ceil(35.45))
print('Redondear hacia abajo: ',math.floor(35.45))
print('Factorial: ',math.factorial(5))
print('Exponencial: ',math.exp(1))
print('Logaritmo: ',math.log(9,3))
print('Logaritmo: ',math.log(1))
print('Raiz cuadrada: ',math.sqrt(64))
print("Seno :",math.sin(0))
print("CoSeno :",math.cos(0))
print("Tanngente :",math.tan(0))
print("Valor PI :",math.pi)

import random
print('Numero al azar de 0 - 1: ',random.random())
print('Random de 20 a 50:  ',int((50-20)*random.random()+20))
print('Random de 20 a 50:  ',random.randint(20,50))
print('Random de 20 a 50:  ',random.randint(-20,50))

print('Random decimal :',random.uniform(-10,20))
print('Random decimal :',random.uniform(-10.5,20.6))

print('Elegir de lista de elemento al azar: ',
        random.choice(['juan','jose','luis','carlos','maria']))

lista=['juan','jose','luis','carlos','maria']
random.shuffle(lista)
print('Imprimir lista en desorden: ',lista)

print('------------------------------------------')

print('Extrae numeros de elementos al azar de la lista: ',random.sample(lista,1))
print('Extrae numeros de elementos al azar de la lista: ',random.sample(lista,2))
print('Extrae numeros de elementos al azar de la lista: ',random.sample(lista,3))

"""
Caso: ingresa n jugadas de un tragamonedas, las figuras son triangulo, cuadrado y circulo
indicar las jugadas ganadoras o perdidas
indicar cuantos gano y perdio
"""

import random

lista=['📐','⏹️','👁️']
def problema9(jugadas):
    ganadas=0
    for x in range(1,jugadas+1):
        num1=random.sample(lista)
        num2=random.sample(lista)
        num3=random.sample(lista)
        if num1==num2 and num2==num3:
            ganadas+=1
            print(f'Jugada {x} = ({num1} - {num2} - {num3}) ====> GANO')
        else:
            print(f'Jugada {x} = ({num1} - {num2} - {num3}) ====> PERDIO')
    print(f'\n Jugadas {ganadas} ganadas')
    print(f'\n Jugadas {jugadas-ganadas} perdidas')

problema9(15)


"""
funciones fecha
"""

from datetime import date

fecha=date(2022,1,12)
print('Fecha es: ',fecha)
print('Fecha actual es: ',date.today())

fecha=date.today()
print('Año: ',fecha.year)
print('Mes: ',fecha.month)
print('Dia: ',fecha.day)

from datetime import time
tiempo=time(20,38,40)
print('Tiempo: ',tiempo)
print('Hora: ',tiempo.hour)
print('Minuto: ',tiempo.minute)
print('Segundo: ',tiempo.second)

tiempo=time()
print('Hora actual: ',tiempo)

from datetime import datetime
fechahora=datetime.now()
print('Fecha y hora actuales: ',fechahora)

from datetime import datetime
tiempo=datetime.now()
print('Tiempo: ',tiempo)
print('Hora: ',tiempo.hour)
print('Minuto: ',tiempo.minute)
print('Segundo: ',tiempo.second)