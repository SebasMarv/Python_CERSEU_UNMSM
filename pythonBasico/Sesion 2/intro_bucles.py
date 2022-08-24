#Bucles

"""
print('Sebas')
print('Sebas')
print('Sebas')
print('Sebas')
print('Sebas')
print('Sebas')
print('Sebas')
print('Sebas')
print('Sebas')
print('Sebas')
print('Sebas')
print('Sebas')
print('Sebas')
"""

#########
## FOR
#########

# la variable i esta iterando en el rango propuesto
for i in range(1,13): #Siempre uno mas al rango
    print('Sebastian Marquez')

# imprimir numeros de dos cifras
for y in range(10,100):
    print(y)

#imprimir numero del 10 al 100 que avance de 3 en 3
for x in range(10,101,3):
    print(x)

#imprimir un numero del 500 al 400
for a in range(500,399,-1):
    print(a)

#Imprimir numero de 3 cifras que sean multiplos de 9
for b in range(100,1000):
    if b % 9==0:
        print(b)

#Recorrer una cadena
nombre = 'Sebastian Marquez'
for x in nombre:
    print(x)

#########
## WHILE
#########

x=10
while x<100:
    print(x)
    x+=1

# la variable i esta iterando en el rango propuesto
for i in range(1,13): #Siempre uno mas al rango
    print('Sebastian Marquez')

# imprimir numeros de dos cifras
y=10
while y<100:
    print(y)
    y+=1

#imprimir numero del 10 al 100 que avance de 3 en 3
x=10
while x<101:
    print(x)
    x+=3

#imprimir un numero del 500 al 400
x=500
while x>399:
    print(x)
    x-=1

#Imprimir numero de 3 cifras que sean multiplos de 9
x=100
while x<1000:
    if x % 9 ==0:
        print(x)
    x+=1

#------------------------

resp='S'
while resp=='S':
    nombre=input('Ingrese el nombre: ')
    print(nombre)
    resp=input('Desea continuar?: S/N')