

from audioop import mul


class calculadora:
  #Inicializar con el metodo constructor
  def __init__(self):
    self.valor1=int(input("Ingrese el valor 1: "))
    self.valor2=int(input("Ingrese el valor 2: "))
  
  #Crear los metodos
  def suma(self):
    suma=self.valor1+self.valor2
    print(f"La suma es: {suma}")
  def multiplicar(self):
    multi=self.valor1*self.valor2
    print(f"La multiplicacion es: {multi}")
  def division(self):
    div=self.valor1*self.valor2
    print(f"La division es: {div}")


#bloque principal
calculo=calculadora()

calculo.suma()
calculo.multiplicar()
calculo.division()