# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 20:36:07 2022

@author: ING-J
"""

import sys
from PyQt5 import uic,QtWidgets
archivo="ejemplo2.ui"
Ui_MainWindow,QtBaseClass=uic.loadUiType(archivo)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)  
        self.btncalcular.clicked.connect(self.calcular)
        
    def calcular(self):
        if self.rbtpalermo.isChecked()==True:
            precio=200000
        elif self.rbtnunez.isChecked()==True:
            precio=250000
        elif self.rbtbelgrano.isChecked()==True:
            precio=280000 
        else:
            precio=320000
        
        if self.rbt1.isChecked()==True:
            precio=precio*1.2
        elif self.rbt25.isChecked()==True:
            precio=precio*1.05
        elif self.rbt69.isChecked()==True:
            precio=precio*0.9
        else:
            precio=precio*0.8 
        
        inicial=eval(self.txtinicial.text())
        saldo=round(precio-inicial,1)
        
        self.lblprecio.setText("s/"+str(round(precio,1)))  
        self.lblsaldo.setText("s/"+str(saldo))    
        
        
        
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec())
    