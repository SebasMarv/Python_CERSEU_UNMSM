# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:52:56 2022

@author: ING-J
"""

import sys
from PyQt5 import uic,QtWidgets
archivo="ejemplo3.ui"
Ui_MainWindow,QtBaseClass=uic.loadUiType(archivo)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)  
        self.btncalcular.clicked.connect(self.calcular)
        
    def calcular(self):
        if self.rbtnotebook.isChecked()==True:
            precio=3500
        elif self.rbtpc.isChecked()==True:
            precio=5500
        elif self.rbtlaptop.isChecked()==True:
            precio=7500 
        else:
            precio=11000 
        
        cantidad=eval(self.txtcantidad.text())
        subtotal=precio*cantidad 
        
        if self.rbt1.isChecked()==True:
            garantia=subtotal*0.1
        elif self.rbt2.isChecked()==True:
            garantia=subtotal*0.17
        else:
            garantia=subtotal*0.25
        
        accesorios=0
        if self.chkimpresora.isChecked()==True:
            accesorios=accesorios+eval(self.txtimpresora.text())*750 
        
        if self.chkparlantes.isChecked()==True:
            accesorios=accesorios+eval(self.txtparlantes.text())*150 
        
        if self.chksilla.isChecked()==True:
            accesorios=accesorios+eval(self.txtsilla.text())*1100 
        
        if self.chkaudifonos.isChecked()==True: 
            accesorios=accesorios+eval(self.txtaudifonos.text())*200 
        
        neto=subtotal+garantia+accesorios 
        self.lblprecio.setText("s/"+str(subtotal))
        self.lblgarantia.setText("s/"+str(garantia))
        self.lblaccesorios.setText("s"+str(accesorios))
        self.lblneto.setText("s/"+str(neto))
        
        
        
        
        
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec())
    