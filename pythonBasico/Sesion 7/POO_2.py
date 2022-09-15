"""
Crear una aplicacion de permita el ingreso de dos valores
y defina los metodos basicos de operaciones
"""

#Clase es como una plantilla para ser utilizado por un objeto
class Operaciones():
  n1=0
  n2=0
  #Metodos - acciones de la clase
  def suma(self):
    return self.n1+self.n2

  def multiplicar(self):
    return self.n1*self.n2




#-----------------modulo principal de la app-----------------
#Instanciar la clase (define que podamos utilizar la clase mediante un objeto)
valor=Operaciones()
#Ingresar los valores y enviarlos a la clase para que retorne el metodo(s)
#Utilizar el objeto que utiliza la plantilla (class Operaciones)
valor.n1=eval(input("Ingresar el valor n1: "))
valor.n2=eval(input("Ingresar el valor n2: "))

print("El valor de la suma es: ",valor.suma())
print("El valor de la suma es: ",valor.multiplicar())