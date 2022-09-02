"""
3. Los conductores de una empresa de transporte urbano. Tienen que ingresar al sistema el número de boletos vendidos por niños (s/1.0), universitario (s/1.5) y adultos (s/2.5), 
el costo de consumo de gasolina y otros gastos. Mostrar la lista de los conductores registrados y la ganancia obtenida. (Usar listas, tuplas y/o diccionario)
"""

precios={'Niños':1,'Universitarios':1.5,'Adultos':2.5}

def problema3():
    niño=eval(input('Ingrese el numero de boletos vendidos a niños: '))
    uni=eval(input('Ingrese el numero de boletos vendidos a universitarios: '))
    adulto=eval(input('Ingrese el numero de boletos vendidos a adultos: '))
    