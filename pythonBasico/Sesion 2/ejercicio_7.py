"""
5. Ingresar el nombre empleado, área y horas de trabajo. Si el
empleado trabajo más de 160 horas el resto de las horas se paga
como horas extras es decir un 15% más.
Área  Pago por Hora
A       S/ 100
B       S/ 65
C       S/ 45
"""

def problema7(empleado,area,horas):
    if area=='A' or area=='a':
        pago=100
    elif area=='B' or area=='b':
        pago=65
    else:
        pago=45
        
    if horas<=160:
        basico=horas*pago
        extra=0
    else:
        basico=160*pago
        extra=(horas-160)*pago*1.15
    neto=basico+extra
    print('Empleado: ',empleado)
    print('Basico: ',basico)
    print('Extra: ',extra)
    print('Sueldo: ',neto)
    print('-------------------------------')

problema7('Sebastian Marquez','a',150)
problema7('Mario Vargas','b',180)