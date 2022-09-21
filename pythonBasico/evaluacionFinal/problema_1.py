class Estudiante:
  def __init__(self, nombre,dni,sexo,fechaNacimiento):
    self.nombre=nombre
    self.dni=dni
    self.sexo=sexo
    self.fechaNacimiento=fechaNacimiento
  def codigo(self):
    nom=self.nombre[0:2]
    pat=self.nombre[self.nombre.find(" ")+1:self.nombre.find(" ")+2]
    posicion=self.nombre.find(" ",self.nombre.find(" ")+1)
    mat=self.nombre[posicion+1:posicion+3]
    dni_num=str(self.dni[4:8])
    posicion2=self.fechaNacimiento.find(" ",self.fechaNacimiento.find(" ")+1)
    fech=self.fechaNacimiento[posicion2+1:posicion2+2]
    return "{}{}{}{}{}".format(nom.upper(),mat.upper(),dni_num,self.sexo,fech)

class Carrera(Estudiante):
  def __init__(self, nombre,dni,sexo,fechaNacimiento,carrera,turno):
    super().__init__(nombre,dni,sexo,fechaNacimiento)
    self.carrera=carrera
    self.turno=turno

  def clasificacion(self):
    if self.carrera=="Ciencias":
      if self.turno =="Mañana":
        mensualidad=1200
      else:
        mensualidad=1500
    elif self.carrera=="Letras":
      if self.turno =="Mañana":
        mensualidad=900
      else:
        mensualidad=1000
    elif self.carrera=="Ingenieria":
      if self.turno =="Mañana":
        mensualidad=1400
      else:
        mensualidad=1600
    print(f"nombre: {self.nombre}")
    print(f"dni: {self.dni}")
    print(f"fecha de nacimiento: {self.fechaNacimiento}")
    print(f"carrera: {self.carrera}")
    print(f"turno: {self.turno}")
    print(f"Codigo: {Estudiante.codigo(self)}")


alumno1=Carrera("Sebastian Marquez Vaquez","73674117","M","26 de Junio de 1999","Ciencias","Mañana")

alumno1.clasificacion()