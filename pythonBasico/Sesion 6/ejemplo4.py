# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:15:35 2022

@author: ING-J
"""

import sys
from PyQt5 import uic,QtWidgets
archivo="ejemplo4.ui"
Ui_MainWindow,QtBaseClass=uic.loadUiType(archivo)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)  
        self.btncalcular.clicked.connect(self.calcular)
        
    def calcular(self):
        producto=self.cboproducto.currentText() 
        marca=self.lstmarca.currentItem().text() 
        
        if producto=="LAPTOP":
            precio=7400
        elif producto=="NOTEBOOK":
            precio=3500
        else:
            precio=2500 
        
        if marca=="HP":
            precio=precio*1.15
        elif marca=="LENOVO":
            precio=precio*1.2
        elif marca=="LG":
            precio=precio*1.4
        else:
            precio=precio*1.9 
        
        self.lblneto.setText("s/"+str(precio))
        
        
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec())
    