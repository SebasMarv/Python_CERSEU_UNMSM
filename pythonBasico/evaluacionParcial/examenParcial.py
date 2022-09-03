#-------------------------Problema_1-------------------------

"""
1.- La inmobiliaria Nogales ofrece venta de viviendas en los siguientes condominios, sus precios y condiciones son las siguientes (Mostrar detalle: precio neto y pago de cuotas mensuales), 
sabiendo que la venta es por 15 años:
Ingreso de data:
•	Condiminio
•	Tiempo laboral
•	Sueldo básico
•	Inicial minimo
"""

condominios={'Alborada':650000,'Villa Sol':535000,'Villa Norte':480000,'Magnolia':430000}

def problema1():
    #Listado de precios para el usuario
    print('=========Lista de condominios,precios e inicial minimo=========')
    print('|Condominios|\t|Precios|\t|Inicial minima|')
    for x,y in condominios.items():
        if x=='Alborada':
            print(f'{x}\tS/{y}\tS/{y*0.20}')
        elif x=='Villa Sol':
            print(f'{x}\tS/{y}\tS/{y*0.17}')
        elif x=='Villa Norte':
            print(f'{x}\tS/{y}\tS/{y*0.16}')
        elif x=='Magnolia':
            print(f'{x}\tS/{y}\tS/{y*0.15}')
    print('===============================================================')
    #Ingreso de datos
    condiminio=input('Ingrese el condominio deseado: ')
    tiempo=eval(input('Ingrese el tiempo laboral: '))
    sueldoBase=eval(input('Ingrese su sueldo base: S/'))
    inicial=eval(input('Ingrese la inicial: S/'))
    print('===============================================================')
    if condiminio=='Alborada' and tiempo>=4 and sueldoBase>=4800 and inicial>=130000:
        precio=650000-inicial
        precioFinal=precio*1.18
        cuotaMensual=precioFinal/(12*15)
        print(f'Condominio adquirido: |{condiminio}|')
        print(f'El precio neto es: {round(precioFinal,2)} y el pago de cuotas mensuales es: {round(cuotaMensual,2)}')
    elif condiminio=='Villa Sol' and tiempo>=3 and sueldoBase>=4300 and inicial>=90950:
        precio=535000-inicial
        precioFinal=precio*1.15
        cuotaMensual=precioFinal/(12*15)
        print(f'Condominio adquirido: |{condiminio}|')
        print(f'El precio neto es: {round(precioFinal,2)} y el pago de cuotas mensuales es: {round(cuotaMensual,2)}')
    elif condiminio=='Villa Norte' and tiempo>=2 and sueldoBase>=3500 and inicial>=76800:
        precio=480000-inicial
        precioFinal=precio*1.16
        cuotaMensual=precioFinal/(12*15)
        print(f'Condominio adquirido: |{condiminio}|')
        print(f'El precio neto es: {round(precioFinal,2)} y el pago de cuotas mensuales es: {round(cuotaMensual,2)}')
    elif condiminio=='Magnolia' and tiempo>=2 and sueldoBase>=2800 and inicial>=64500:
        precio=430000-inicial
        precioFinal=precio*1.15
        cuotaMensual=precioFinal/(12*15)
        print(f'Condominio adquirido: |{condiminio}|')
        print(f'El precio neto es: {round(precioFinal,2)} y el pago de cuotas mensuales es: {round(cuotaMensual,2)}')
    else:
        print('===>Lo sentimos no cumple con las condiciones minimas.<===')
    #Resultado precioFinal = precio Neto || coutaMensual = cuota mensual
    print('===============================================================')

problema1()

#-------------------------Problema_2-------------------------

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
    print('Periodo \tPago Semestral  \tInteres \tAmortizacion \t Saldo')
    for x in range(1,semestres+1):
        if x<selecSemestre:
            mInteres=deuda*interes
            amortizacion=0
            deuda=deuda-amortizacion
            renta_2=mInteres
            print(x,'\t         s/',round(renta_2,1),'\t     s/',round(mInteres,1),'\t s/',round(amortizacion,1),'\t         s/',round(deuda,1))
        elif x>=selecSemestre:
            mInteres=deuda*interes
            amortizacion=renta-mInteres
            deuda=deuda-amortizacion
            print(x,'\t         s/',round(renta,1),'\t s/',round(mInteres,1),'\t s/',round(amortizacion,1),'\t s/',round(deuda,1))

problema2(100000,5,10,4)

#-------------------------Problema_3-------------------------

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
    combustible=eval(input('Ingrese el costo total del combustible: S/'))
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
        print(x,' ===> S/',y)

problema3()
