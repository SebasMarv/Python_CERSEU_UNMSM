"""

"""

#clase
class Calculo():
  precio=0
  cantidad=0
  
  def total(self):
    return self.precio*self.cantidad
  def igv(self):
    return self.total()*0.18
  def montoTotal(self):
    return self.total()+self.igv()
  def descuento(self):
    if self.montoTotal() > 100:
      return self.montoTotal()*0.20
    else:
      return self.montoTotal()*0.05
  
  def totalPago(self):
    return self.montoTotal()-self.descuento()

#instanciar
prueba=Calculo()

#Utilizar objeto que contiene la estructura de la clase (valores y funciones)
prueba.precio=eval(input("Ingrese el precio: "))
prueba.cantidad=eval(input("Ingrese el cantidad: "))

#Imprimir resultados
print(f"El valor final es: {prueba.totalPago()}")