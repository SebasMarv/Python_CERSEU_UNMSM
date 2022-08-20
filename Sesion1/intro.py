print('Nombre es Juan Jose')

#No hace falta declarar el tipo de variables que tienen
nombre = 'Juan jose'
edad = 40 
correo = 'Ing-Juanjose@hotmail.com'

#Se puede tener 
print('Nombre es ',nombre)
print('Edad es ', edad)
print('correo es ', correo)

horas = 40
pago = 50
basico = horas * pago

print('Empleado: ',nombre)
print('Sueldo Basico: ',basico)

#Se crea el metodo para automatizar un proceso repetitivo
def planilla(empleado, horas, pago):
    basico = horas * pago
    print('Empleado: ',empleado)
    print('Sueldo basico es s/',basico)

#Utilizando el metodo
planilla('Juan Jose',35,45)
planilla('Ana Maria',46,50)
planilla('Lucia Carmen',80,33)
