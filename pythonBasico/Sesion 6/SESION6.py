# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 19:07:28 2022

@author: ING-J
"""
import random 
print("numero al azar de 0-1",random.random())
print("Random de 20 a 50 :", int((50-20)*random.random()+20))
print("Random de 20 a 50 :",random.randint(20,50))
print("Random de 20 a 50 :",random.randint(-20,50))

print("Random decimal :",random.uniform(-10,20))
print("Random decimal :",random.uniform(-10.5,20.5))

print("Elegir de lista elemento al azar :",
      random.choice(["juan","jose","luis","carlos","maria"]))

lista=["juan","jose","luis","carlos","maria"]
random.shuffle(lista)
print("Imprimir lista en desorden :",lista)

print("Extrae numero de elementos al azar de lista :",
      random.sample(lista,1))

print("Extrae numero de elementos al azar de lista :",
      random.sample(lista,2))

print("Extrae numero de elementos al azar de lista :",
      random.sample(lista,3))


"""
ingresa n jugadas de un tragamoneda, las figuras son triangulo,
cuadrado y circulo. Indicar la jugadas que gano o perdio.
Tambien indicar cuantos gano y perdio
"""
def problema1(jugadas):
    gano=0
    for x in range(1,jugadas+1):
        lista=["triangulo","cuadrado","circulo"]
        fig1=random.choice(lista)
        fig2=random.choice(lista)
        fig3=random.choice(lista)
        if fig1==fig2 and fig2==fig3:
            gano=gano+1
            jugada="Gano"
        else:
            jugada="Perdio" 
        print("Jugada nº",x," (",fig1,"-",fig2,"-",fig3,")  ====>",jugada)
    print("Gano ",gano," jugadas")
    print("Perdio ",jugadas-gano," jugadas")

problema1(20)


"""
funciones fecha
"""
from datetime import date 
fecha=date(2022,1,12)
print("Fecha es ",fecha)
print("Fecha actual es: ",date.today())

fecha=date.today() 
print("Año :",fecha.year)
print("Mes :",fecha.month) 
print("Dia :",fecha.day)


from datetime import time 
tiempo=time(20,38,40)
print("Tiempo es :",tiempo)
print("Hora es :", tiempo.hour)
print("Minuto es :",tiempo.minute)
print("Segundo es :",tiempo.second)

tiempo=time() 
print("Hora actual :",tiempo)


from datetime import datetime 
fechahora=datetime.now() 
print("Fecha y Hora actual es: ",fechahora)
print("Año :",fechahora.year)
print("Mes :",fechahora.month) 
print("Dia :",fechahora.day)
print("Hora es :", fechahora.hour)
print("Minuto es :",fechahora.minute)
print("Segundo es :",fechahora.second)
















