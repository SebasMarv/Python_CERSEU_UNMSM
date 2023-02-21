#-----------Listas--------------

contactos=['Juan jose','Ana maria','Luis miguel','Luis pedro','Jose alberto']

print(contactos)

#Imprimir por posicion
print(contactos[0])
print(contactos[1])
print(contactos[2])
print(contactos[3])
print(contactos[-1])
print(contactos[-3])
print(contactos[2:4])

factura=['pan','huevo',100,340]

print(factura)

#contar elementos con "len"
print('Cantidad de elementos', len(factura))


print(factura)#antes de agregar
factura.append('pan')#agregar elementos
print(factura)

#contar las veces que repite
print(factura.count('pan'))

#añadir rango de datos 
factura.extend(range(5,9))
print(factura)

#Insertar elemento en una posicion
factura.insert(2,'Perú')
print(factura)

#borrar posicion
factura.pop(2)
print(factura)

#borrar por busqueda
factura.remove('pan')
print(factura)

#reversa de una lista
factura.reverse()
print(factura)


print(contactos)
#ordenar lista
contactos.sort()
print(contactos)
#ordenar en reversa
print(contactos)
contactos.sort(reverse=True)
print(contactos)

nuevo=contactos+factura
print(nuevo)

print('------------------------------------------\n')
lista=[
    ['Juan Jose','Analista',7600],
    ['Ana Maria','Programador',9600],
    ['Luciana Ana','Contador',6600],
    ['Luis Carlos','Administradora',11600]
]
print(lista)
print(lista[0])

print('------------------------------------------\n')
contactos=contactos * 3
print(contactos)

print('------------------------------------------\n')
for x in contactos:
    print(x)

print('------------------------------------------')

def lista(posicion):
    contactos=['Juan jose','Ana maria','Luis miguel','Luis pedro','Jose alberto']
    cargos=['Analista','Programador','Albañil','Contador','Administrador']
    sueldo=[6500,7600,8900,4500,6500,900]
    print('Contacto',contactos[posicion])
    print('Cargo',cargos[posicion])
    print('Sueldo',sueldo[posicion])

lista(2)
lista(4)

print('------------------------------------------\n')

contactos=['Juan jose','Ana maria','Luis miguel','Luis pedro','Jose alberto']
print(contactos.index('Ana maria')) #Buscar posicion
#print(contactos.index('Ana Jose'))#sino existe sale error

print('------------------------------------------\n')

def lista(contacto):
    contactos=['Juan jose','Ana maria','Luis miguel','Luis pedro','Jose alberto']
    cargos=['Analista','Programador','Albañil','Contador','Administrador']
    sueldo=[6500,7600,8900,4500,6500,900]
    try:
        posicion=contactos.index(contacto)
    except:
        posicion=-1
    if posicion==-1:
        print('Contacto no registrado')
    else:
        print('Contactos',contactos[posicion])
        print('Cargos',cargos[posicion])
        print('Sueldo',sueldo[posicion])

lista('Ana maria')
lista('Rocio Perez')

#-----------Tupla--------------

tupla=(12,14,-15,16,-34,23,18,14)
tupla

tupla[3]
tupla[2:5]

tupla.count(14)



#convertir tupla a una lista
lista_tupla=list(tupla)

#convertir lista a tupla
tupla_contactos=tuple(contactos)

for x in tupla:
    print(x)

nuevatupla=tupla+tupla_contactos
print(nuevatupla)

print(len(nuevatupla))



#-----------Diccionario--------------

diccionario={'JuanJose':4500,'Nancy':6500,'Carlos':8500,'Carmen':7500,'Alberto':3500}

diccionario.items()#mostrar todos los elementos
diccionario.keys()#mostrar las llaves
diccionario.values()#mostrar los valores

#Indicar la llave para que muestre un valor
diccionario['JuanJose']
diccionario.get('JuanJose')

#Añadir elementos a diccionario
diccionario['Sebastian']=6300
print(diccionario)

#CAmbiar el valor de una llave
diccionario['Nancy']=10000
diccionario.get('Nancy')
print(diccionario)

#cambiar un valor por una lista dentro de un diccinario
diccionario['Nancy']=[1000,2000,3000]
print(diccionario)

for x,y in diccionario.items():
    print(x,' ==> ',y)

#copiar
diccionario1=diccionario.copy()
print(diccionario1)

#copiar forma 2
diccionario2=diccionario
print(diccionario2)

#Eliminar un valor 
diccionario2.pop('Carmen')
diccionario2

#Cantidad de elementos de un diccionario
len(diccionario2)

#limpiar un diccionario
diccionario2.clear()
diccionario2