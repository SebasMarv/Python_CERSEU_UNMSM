"""
El monto de pasaje de una empresa de transporte es niño s/1.5, adulto s/3.0
y universitario es 2.0. Ingresar la cantidad de boletos vendido por cada tipo de
pasajero y monto de combustible consumido. Indicar total cobrado y ganancia
"""

def problema10(pNiño,pAdulto,pUniversitario,montoCombustible):
    totalNiño = pNiño * 1.5
    totalAdulto = pAdulto * 3.0
    totalUniversitario = pUniversitario * 2.0
    totalPasajes = totalAdulto + totalUniversitario + totalNiño
    ganancia = totalPasajes - montoCombustible
    print('Total Cobrado: S/', totalPasajes)
    print('Ganancia es: S/',ganancia)

problema10(30,40,50,150)