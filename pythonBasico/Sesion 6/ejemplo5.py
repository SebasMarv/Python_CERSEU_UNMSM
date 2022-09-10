# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 21:28:12 2022

@author: ING-J
"""

import sys
from PyQt5 import uic,QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
archivo="ejemplo6.ui"
Ui_MainWindow,QtBaseClass=uic.loadUiType(archivo)
class MyApp(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)  
        self.btncalcular.clicked.connect(self.calcular)
        
    def calcular(self):
        prestamo=eval(self.txtprestamo.text())
        interes=eval(self.txtinteres.text())
        cuotas=eval(self.txtcuotas.text())
        monto=prestamo*(1+interes/100)
        montocuota=monto/cuotas
        self.lblmonto.setText("s/"+str(monto))
        dic={"fila":0}
        for x in range(1,cuotas+1):
            monto=monto-montocuota
            self.tbl1.setRowCount(dic["fila"]+1)#definir la cantidad de filas que tiene la tabla
            self.tbl1.setItem(dic["fila"],0,QTableWidgetItem(str(x)))#llenar dato en una fila y columna especifica
            self.tbl1.setItem(dic["fila"],1,QTableWidgetItem("s/"+str(montocuota)))
            self.tbl1.setItem(dic["fila"],2,QTableWidgetItem("s/"+str(monto)))
            dic["fila"]=dic["fila"]+1  
        
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=MyApp()
    window.show()
    sys.exit(app.exec())
    