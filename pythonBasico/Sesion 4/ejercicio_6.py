"""
6.- Desarrolle un programa que matricule y acepte 2 estudiantes por diplomado de
Big Data, Hacking y Programación. Registrar nombre estudiantes y diplomado
seleccionado.
"""

cursos={'BigDAta':0,'Hacking':0,'Programacion':0}
matriculados={}
def problema6():
    print('Lista de diplomados')
    for x in cursos:
        print(x)
    diplomado=input('Seleccion su diplomado: ')
    cantidad=cursos[diplomado]
    if cantidad==2:
        print('No hay vacantes')
    else:
        nombre=input('Ingrese el nombre')
        matriculados[nombre]=diplomado
        cursos[diplomado]=cursos[diplomado]+1
    for x,y in cursos.items():
        print(x,' ===> ',y)
    print('==============')
    for x,y in matriculados.items():
        print(x,' ===> ',y)

problema6()