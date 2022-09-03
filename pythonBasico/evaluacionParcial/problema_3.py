"""
3. Los conductores de una empresa de transporte urbano. Tienen que ingresar al sistema el número de boletos vendidos por niños (s/1.0), universitario (s/1.5) y adultos (s/2.5), 
el costo de consumo de gasolina y otros gastos. Mostrar la lista de los conductores registrados y la ganancia obtenida. (Usar listas, tuplas y/o diccionario)
"""

registros={}

def problema3():
    precios={'Niños':1,'Universitarios':1.5,'Adultos':2.5}
    conductor=input('Ingrese nombre de conductor: ')
    cant_niño=eval(input('Ingrese el numero de boletos vendidos a niños: '))
    cant_uni=eval(input('Ingrese el numero de boletos vendidos a universitarios: '))
    cant_adulto=eval(input('Ingrese el numero de boletos vendidos a adultos: '))
    combustible=eval(input('Ingrese el costo total del combustible: '))
    for x,y in precios.items():
        if x=='Niños':
            total_niño=cant_niño*y
        elif x=='Universitarios':
            total_uni=cant_uni*y
        elif x=='Adultos':
            total_adulto=cant_adulto*y
    total_pasajes=total_niño+total_uni+total_adulto
    ganancia=total_pasajes-combustible
    registros[conductor]=ganancia
    print('Conductor\tGanancia')
    for x,y in registros.items():
        print(x,' ===> ',y)

problema3()