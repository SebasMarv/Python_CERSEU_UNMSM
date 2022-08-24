"""
Validar el ingreso a un sistema información a los siguientes usuarios.
USUARIO CLAVE
ADMIN   123
USER    456
"""

def problema4(usuario,clave):
    if (usuario == 'ADMIN' and clave =='123') or (usuario == 'USER' and clave =='456'):
        print('Bienvenido usuario ',usuario)
    else:
        print('Usuario ',usuario,'no registrado')

problema4('ADMIN','123')
problema4('ROOT','582')
