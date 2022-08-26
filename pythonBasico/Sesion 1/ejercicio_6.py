"""
Una institución social tiene un centro de salud, un comedor infantil, una escuela
infantil y un asilo de ancianos. La institución recibe anualmente una donación
que lo reparte de la siguiente forma: 25% de la donación para la implementación
del centro de salud, 35% de la donación para el comedor infantil, 25% de la
donación para la escuela infantil y el resto para el asilo de ancianos. Diseñe un
algoritmo para efectuar el reparto de la donación
"""

def problema6(donacion):
    print('- - - - - - - - - - - - - - - - -')
    print('Centro Salud S/',round(donacion*0.25,1))
    print('Comedor infantil S/',round(donacion*0.35,1))
    print('Escuela Infantil S/',round(donacion*0.25,1))
    print('Asilo de Ancianos S/',round(donacion*0.15,1))
    print('- - - - - - - - - - - - - - - - -')

problema6(4500)
