class Vehiculo():
  def __init__(self,marca,modelo):
    #atributos
    self.modelo=modelo
    self.marca=marca

  #comportamiento
  def estado(self):
    print("Marca: ",self.marca)


#herencia

class Moto(Vehiculo):
  pass #no construyo de momento nada dentro de la clase hija

class Camion(Vehiculo):
  pass #no construyo de momento nada dentro de la clase hija

miMoto=Moto()