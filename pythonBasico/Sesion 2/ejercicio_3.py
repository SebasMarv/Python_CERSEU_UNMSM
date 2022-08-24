"""
3. Desarrollar un formulario para una entidad bancaria que realiza préstamo de 5 años con las
siguientes modalidades:
INTERES
Mensual 21.5%
Trimestral 25.5%
Semestral 31%
Mostrar el monto total a pagar y el monto de las cuotas
"""

def problema3(prestamo,modalidad):
    if modalidad =='m' or modalidad=='M':
        montototal=prestamo*1.215
        montocuota=montototal/(5*12)
    elif modalidad =='t' or modalidad =='T':
        montototal=prestamo * 1.255
        montocuota = montototal/(5*4)
    else:
        montototal=prestamo * 1.31
        montocuota = montototal/(5*2)
    print('Monto total a pagar S/',round(montototal,1))
    print('Pago cuota S/',round(montocuota,1))

problema3(150000,'m')
problema3(150000,'t')
problema3(150000,'s')

