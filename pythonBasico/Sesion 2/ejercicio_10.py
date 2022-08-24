"""
12. En un juego de preguntas a las que se responde Si o No gana quien
responda correctamente las tres preguntas. Si se responde mal a
cualquiera de ellas ya no se pregunta la siguiente y termina el juego.
Las preguntas son:
•¿Colon descubrió América?
•¿La independencia de México fue en el año 1810?
•¿The Doors fue un grupo de rock Americano?
"""

def problema10():
    puntaje=0
    preg1=input('Colon descubrió América?: |')
    if preg1=='SI' or preg1=='si':
        preg2=input('La independencia de México fue en el año 1810?: |')
        puntaje+=1 #puntaje=puntaje + 1 
        if preg2=='SI' or preg2=='si':
            preg3=input('The Doors fue un grupo de rock Americano?: |')
            puntaje+=1 #puntaje=puntaje + 1 
            if preg3=='SI' or preg3=='si':
                puntaje+=1 #puntaje=puntaje + 1 
    print('Tu puntaje es: ',puntaje)

problema10()