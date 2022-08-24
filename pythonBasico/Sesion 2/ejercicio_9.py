"""
9. El IMSS requiere clasificar a las personas que se jubilaran en el año
de 1997. Existen tres tipos de jubilaciones: por edad, por
antigüedad joven y por antigüedad adulta. Las personas adscritas a
la jubilación por edad deben tener 60 años o más y una antigüedad
en su empleo de menos de 25 años. Las personas adscritas a la
jubilación por antigüedad joven deben tener menos de 60 años y
una antigüedad en su empleo de 25 años o más. Las personas
adscritas a la jubilación por antigüedad adulta deben tener 60 años
o más y una antigüedad en su empleo de 25 años o más.
Determinar en qué tipo de jubilación, quedara adscrita una persona.
"""

def problema9(servicio,edad):
    if edad>=60 and servicio<25:
        print('Jubilacion por edad')
    elif edad<60 and servicio>25:
        print('Jubilacion por antiguedad joven')
    elif edad>=60 and servicio>=25:
        print('Jubilacion por antiguedad adulta')
    else:
        print('Usted no se jubila')

problema9(20,70)
problema9(30,50)
problema9(30,70)
problema9(20,50)