"""
Ingresar las horas de trabajo normal, horas de trabajo extra y pago hora
normal de un empleado. Mostrar sueldo básico, sueldo extra sabiendo que es
el 15% más del pago de hora normal, descuento 13% (aplicado al sueldo
básico) y sueldo neto
"""

def problema9(horas,horas_extra,pago):
    basico = horas * pago
    extra = horas_extra * (pago*1.15)
    descuento = basico * 0.13
    neto = (basico + extra) - descuento
    print('Basico es: S/',basico)
    print('Sueldo Extra es: S/',extra)
    print('Descuento: S/',descuento)
    print('Sueldo neto es: S/',neto)

problema9(80,10,35)