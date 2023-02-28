from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Owner
from django.db.models import F,Q

def list_owner(request):

    # data_context = {
    #     'nombre': 'Jesús de La Cruz',
    #     'edad': 29,
    #     'pais_nacimiento': 'Perú',
    #     'dni': '951456123',
    #     'vigente': False
    # }

    data_context = [
        {
            'nombre': 'Jesús de La Cruz',
            'edad': 26,
            'pais_nacimiento': 'Perú',
            'dni': '451456653',
            'vigente': True
        },
        {
            'nombre': 'Eduardo Gutierrez',
            'edad': 28,
            'pais_nacimiento': 'Brasil',
            'dni': '46514561',
            'vigente': True,
            'pokemons': [
                {
                    'nombre_pokemon': 'charizard',
                    'ataques': ['ataque1 - charizard', 'ataque2 - charizard']
                }
            ]
        },
        {
            'nombre': 'María Luisa',
            'edad': 35,
            'pais_nacimiento': 'México',
            'dni': '23456123',
            'vigente': True
        }
    ]

    """Crear un objeto en una tabla de la BD"""
    #p = Owner(nombre="Juliana", pais="España", edad=26)
    #p.save()  # Guarda el registro en la B.D.

    #p.nombre = "Samanta"
    #p.save()

    """Obtener todos los elementos de una tabla de la BD"""
    #owners = Owner.objects.all()

    """Filtración de datos: .filter()"""
    #owners = Owner.objects.filter(nombre="Paolo")

    """Filtración de datos con AND de SQL: filter()"""
    #owners = Owner.objects.filter(nombre="Juliana", edad=26)

    """Filtración de datos más precisos con : __contains"""
    #owners = Owner.objects.filter(nombre__contains="Benito")

    """Filtración de datos más precisos con: __endswith"""
    #owners = Owner.objects.filter(nombre__endswith="ima")

    """Obtener un solo objeto de la tabla en la BD"""
    #owners = Owner.objects.get(dni="63451234")

    #print("El dato es: {}".format(owners))
    #print("Tipo de datos: {}".format(type(owners)))

    """Ordenar por cualquier atributo o campo de la tabla"""

    """Ordenar alfabéticamente por nombre"""
    # owners = Owner.objects.order_by('-edad')

    """Ordenar concatenando diferentes métodos de ORMs"""
    #owners = Owner.objects.filter(nombre="Juliana").order_by("-edad")

    """Acortar datos: Obtener un rango de registro de una talba en la BD"""
    #owners = Owner.objects.all()#[0:5]

    """Eliminando un conjunto de datos es específico"""
    # owners = Owner.objects.filter(id=3)
    # owners.delete()

    """Actualizacion de datos en al bd a un cierto grupo de datos o un solo registro"""
    # Owner.objects.filter(nombre__startswith="Ju").update(edad=34)

    """Utilizando F expressions"""
    #Owner.objects.filter(edad__lte=27).update(edad=(F('edad') + 10))

    """Consultas complejas"""
    # query = Q(pais__startswith = 'Pe') | Q(pais__startswith = 'Es')
    # owners=Owner.objects.filter(query)

    #Negacion not ~
    # query = Q(pais__startswith = 'Pe') | ~Q(edad=34)
    # owners=Owner.objects.filter(query)

    query = Q(pais__startswith='Pe') | Q(pais__startswith='Es')
    owners = Owner.objects.filter(query, edad=34)


    return render(request, 'owner/owner_list.html', context={'data': owners})