import sys
import django

print('Version de python Intalado:')
print(sys.version)

print('Version Info')
print(sys.version_info)


print('Version de Django Instalado: {}'.format(django.get_version()))

