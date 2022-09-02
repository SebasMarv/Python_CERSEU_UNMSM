"""
1.- Desarrolle un programa que registre contactos: Nombre, teléfono y correo. Mostrar
los contactos registrados.
"""


contactos={}
def problema1():
    nombre=input('Ingrese nombre: ')
    telefono=input('Ingrese telefono: ')
    correo=input('Ingrese correo: ')
    lista=[telefono,correo]
    contactos[nombre]=lista
    for x,y in contactos.items():
        print(x,' ===> ',y)

problema1()