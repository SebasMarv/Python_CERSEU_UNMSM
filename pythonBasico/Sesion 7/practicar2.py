"""
Ingreso de datos
*alumno, curso, tres notas (almacenar los datos), promedio, observacion
crear menu de opciones
La logica del programa se defina en la clase utilizando el metodo constructor
"""

#Clase

class alumno:
  def __init__(self,nombre,curso,n1,n2,n3):
    import statistics as operaciones
    self.nombre=nombre
    self.curso=curso
    self.n1=n1
    self.n2=n2
    self.n3=n3
    #Promedio mediante el metodo "mean"
    self.promedio=operaciones.mean([self.n1,self.n2,self.n3])
  #Crear mis metodos
  def Observacion(self):
    if(self.promedio>=0 and self.promedio<=5):
      self.observacion="Jalada"
    elif(self.promedio>5 and self.promedio<=11):
      self.observacion="A cargo"
    elif(self.promedio>11 and self.promedio<=15):
      self.observacion="Regular"
    elif(self.promedio>15 and self.promedio<=20):
      self.observacion="Bueno"


#diccionario u tupla para guardar datos
def ingresar_alumno():
  nom_lista=[]
  curso_lista=[]
  n1_lista=[]
  n2_lista=[]
  n3_lista=[]
  prom_lista=[]
  observa_lista=[]
  rpta="s"
  while(rpta.upper()=="S"):
    nom=input("Nombre: ").upper()
    cur=input("Curso: ").upper()
    nota1=input("Nota1: ")
    nota2=input("Nota2: ")
    nota3=input("Nota3: ")
    #Instancia la clase mediante un objeto
    nota_alumnos=alumno(nom,cur,nota1,nota2,nota3)
    nota_alumnos.observacion()
    #guardar los datos en el arreglo
    nom_lista.append(nota_alumnos.nombre)
    curso_lista.append(nota_alumnos.curso)
    n1_lista.append(nota_alumnos.n1)
    n2_lista.append(nota_alumnos.n2)
    n3_lista.append(nota_alumnos.n3)
    prom_lista.append(nota_alumnos.promedio)
    observa_lista.append(nota_alumnos.observacion)

    rpta=input("Desea agregar otro elemento?: [S/N]")
    if (rpta.upper()=="N"):
      break

#Menu principal de la app
