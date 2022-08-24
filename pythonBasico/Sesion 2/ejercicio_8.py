"""
6. Ingresar nombre y puntaje de postulante mostrar a que área
ingreso.
Puntaje
Área
0 -100    No Ingreso
101- 130  Soporte
131 - 180 Desarrollo
181 - 200 Análisis
"""
def problema7(nombre,puntaje):
    print('Postulante',nombre)
    if puntaje<=100:
        print('No ingreso')
    elif puntaje <=130:
        print('Ingreso al area de soporte')
    elif puntaje <=180:
        print('Ingreso al area de desarrollo')
    else:
        print('Ingreso al area de analisis')
    print('------------------------')

problema7('Juan jose',80)
problema7('Juan jose',120)
problema7('Juan jose',170)
problema7('Juan jose',220)