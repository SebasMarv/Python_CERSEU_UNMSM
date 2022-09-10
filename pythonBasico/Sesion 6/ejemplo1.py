# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:02:46 2022

@author: ING-J
"""

import sys
from PyQt5 import uic,QtWidgets
archivo="ejemplo1.ui"
Ui_MainWindow,QtBaseClass=uic.loadUiType(archivo)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)  
        self.btncalcular.clicked.connect(self.calcular)
        
    def calcular(self):
        if self.rbteconomico.isChecked()==True:
            precio=10
        elif self.rbtejecutivo.isChecked()==True:
            precio=20
        else:
            precio=15
        cantidad=eval(self.txtcantidad.text())
        subtotal=precio*cantidad 
        if self.rbtfactura.isChecked()==True:
            igv=subtotal*0.18
        else:
            igv=0 
        self.lblsubtotal.setText("s/"+str(subtotal))
        self.lbligv.setText("s/"+str(igv))
        self.lblneto.setText("s/"+str(igv+subtotal))
        
        
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec())
    
    
    
    
    
    
    
    
    