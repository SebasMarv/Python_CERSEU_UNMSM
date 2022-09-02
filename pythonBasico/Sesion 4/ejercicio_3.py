"""
3.- Desarrolle un programa que realice una encuesta de 3 opciones preguntando: ¿Qué
lenguaje de programación prefiere?
Mostrar los resultados de la encuesta.
"""

programacion={'Python':0,'Java':0,'php':0}
def problema3():
    print('Seleccione un lenguaje de su preferencia: ')
    for x in programacion:
        print(x)
    lenguaje=input('Ingrese: ')
    programacion[lenguaje]=programacion[lenguaje]+1
    for x,y in programacion.items():
        print(x,' ==> ',y)

problema3()