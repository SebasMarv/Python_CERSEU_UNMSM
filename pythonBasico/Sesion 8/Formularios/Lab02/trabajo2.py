
#definir el codigo de llamada de los formularios

#definir o importar el modulo que contiene 
import sys
#definir el codigo de llamado de los formularios
from PyQt5.QtWidgets import QMainWindow,QApplication
#Se importa la clase UI para los archivos con las extensiones UI(formulario)
from PyQt5 import uic
#importar modulo1(archivo donde tengo la logica)
import modulo2 as operac

class Operac(QMainWindow):
  def __init__(self):
    #archivo
    QMainWindow.__init__(self)
    uic.loadUi("Formulario04.ui",self)
    self.initUi()
  def initUi(self):
      self.bcalcular.clicked.connect(self.calcular)
      self.bnuevo.clicked.connect(self.nuevo)
      self.bsalir.clicked.connect(self.salir)
  def calcular(self):
      valor=int(self.tmonto.text())
      #calculo
      self.lbldescuento.setText(str(operac.descuento(valor)))
      self.lblpago.setText(str(operac.montopago(valor,operac.descuento(valor))))
  def nuevo(self):
    self.tmonto.setText("")
    self.tdescuento.setText("")
    self.tpago.setText("")
  def salir(self):
    self.close()

if __name__ == '__main__':
  #Se crea una instancia para iniciar la aplicacion  
  app=QApplication(sys.argv)
  #Se crea un objeto ventana01 de tipo clase Operaciones
  ventana01=Operac()
  #Se muesta el objeto
  ventana01.show()
  #Cerrar la aplicacion
  sys.exit(app.exec())