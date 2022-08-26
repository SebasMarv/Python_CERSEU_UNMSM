"""
2) Calcular detalle de liquidación de empleado. Según los datos ingresados
empleado, sueldo básico, años de servicio y número de hijos. Calcular:
a. Liquidación: 65% de sueldo por años de servicio
b. CTS: 30% de liquidación
c. Asignación Familiar: Si tiene hijos el 5% de sueldo por años de servicio
d. Neto: Liquidación + CTS + Asignación Familiar
"""

def problema2(nombre,sueldo,años,hijos):
    liquidacion = 0.65*sueldo*años
    cts=0.3*liquidacion
    familiar=0.05*sueldo*años
    neto=liquidacion+cts+familiar
    print('- - - - - - - - - - - - - - - - -')
    print('El empleado : ',nombre)
    print('La liquidacion es: S/',liquidacion)
    print('La cts es: S/',cts)
    print('Asigancion familiar: S/',familiar)
    print('Sueldo neto: S/',neto)
    print('- - - - - - - - - - - - - - - - -')

problema2('Sebastian Marquez',930,5,2)
problema2('Alexa Mayuri',1200,4,1)