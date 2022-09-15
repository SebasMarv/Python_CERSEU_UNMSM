#Metodo Constructor
class usuario:
  #Es importante definir el metodo contructor despues
  #de la definicion de la clase
  def __init__(self,nombre,apellido):
    self.nombre=nombre
    self.apellido=apellido
    def imprimir(self):
      print(self.nombre," ",self.apellido)

#Instanciar
user=usuario("Sebastian","Marquez")
