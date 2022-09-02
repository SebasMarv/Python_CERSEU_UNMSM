"""
2.- Desarrolle un programa que registre contactos: Nombre, país.
Imprima solo a los contactos de un país. Mostrar los contactos registrados
"""

contactos={'Juan':'Peru','Maria':'Chile','Luis':'Colombia'}
def problema2(country):
    nombre=input('Ingrese nombre: ')
    pais=input('Ingrese pais: ')
    contactos[nombre]=pais
    for x,y in contactos.items():
        if y == country:
            print(x)
    print(contactos)

problema2('Peru')
problema2('Colombia')