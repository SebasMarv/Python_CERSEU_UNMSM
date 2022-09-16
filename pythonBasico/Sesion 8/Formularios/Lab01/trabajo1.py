
#definir el codigo de llamada de los formularios

#definir o importar el modulo que contiene 
import sys
#definir el codigo de llamado de los formularios
from PyQt5.QtWidgets import QMainWindow,QApplication
#Se importa la clase UI para los archivos con las extensiones UI(formulario)
from PyQt5 import uic
#importar modulo1(archivo donde tengo la logica)
import modulo1 as operaciones


#crear una clase de operaciones que herede la clase QMainwindow
class Operaciones(QMainWindow):
  #Se crea el metodo contructor de la clase operaciones
  def __init__(self):
    #cargar el archivo o la venta de extension
    QMainWindow.__init__(self)
    uic.loadUi("Formulario01.ui",self)
    #Inicia el entorno grafico
    self.initUi()
#crear una clase que herede la clase de operaciones
#inicializar los objetos del formulario
  def initUi(self):
      self.bnuevo.clicked.connect(self.nuevo)
      self.bcalcular.clicked.connect(self.calcular)
      self.bsalir.clicked.connect(self.salir)
#inicializar las cajas de texto y los label
  def nuevo(self):
      self.tnumero1.settext("")
      self.tnumero2.settext("")
      self.lblsuma.settext("")
      self.lblresta.settext("")
      self.lblproducto.settext("")
      self.lbldivision.settext("")
  def calcular(self):
      valorn1=int(self.tnumero1.text())
      valorn2=int(self.tnumero2.text())
  #calculos
      self.lblsuma.setText(str(operaciones.suma(valorn1,valorn2)))
      self.lblresta.setText(str(operaciones.resta(valorn1,valorn2)))
      self.lblproducto.setText(str(operaciones.multi(valorn1,valorn2)))
      self.lbldivision.setText(str(operaciones.div(valorn1,valorn2)))
  def salir(self):
  #Salir de la app
      self.close()

if __name__ == '__main__':
  #Se crea una instancia para iniciar la aplicacion  
  app=QApplication(sys.argv)
  #Se crea un objeto ventana01 de tipo clase Operaciones
  ventana01=Operaciones()
  #Se muesta el objeto
  ventana01.show()
  #Cerrar la aplicacion
  sys.exit(app.exec())
  
