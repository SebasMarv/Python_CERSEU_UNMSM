"""
5.- Desarrolla un programa que evaluación con 4 preguntas a los estudiantes. Ellos se
registran y se almacena su puntaje
"""

evaluados={}
def problema5():
    preguntas={'1+1=':2,'2*3=':6,'1+0=':1,'4/2=':2}
    puntaje=0
    nombre=input('Ingrese su nombre: ')
    for x,y in preguntas.items():
        respuesta=eval(input(x))
        if respuesta==y:
            puntaje=puntaje+5
    evaluados[nombre]=puntaje
    for x,y in evaluados.items():
        print(x,' ===> ',y)

problema5()