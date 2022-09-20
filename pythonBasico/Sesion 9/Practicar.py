from contextlib import nullcontext
from math import factorial


def hi():
  return print("Hola amiga")

hi()
hi()
hi()
hi()

#---------------------------------------------

def nombre():
  nom = input("Ingrese su nombre: ")
  return nom

nombre()

#---------------------------------------------

import math as calc

def facto(n):
  f=calc.factorial(n)
  print(f"El factorial de {n} es {f}")

facto(10)

#---------------------------------------------

def factura():
  total=eval(input("Ingrese el total de la factura: "))
  iva=input("Ingrese el porcentaje de IVA: ")
  if iva==" ":
    importFinal=total+(total*0.21)
    print(f"El importe final es: {importFinal}\nEl porcentaje de iva es: {21}%")
  else:
    importFinal=total+(total*(int(iva)/100)) 
    print(f"El importe final es: {importFinal}\nEl porcentaje de iva es: {iva}%")

factura()

#---------------------------------------------

