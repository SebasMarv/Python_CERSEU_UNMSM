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