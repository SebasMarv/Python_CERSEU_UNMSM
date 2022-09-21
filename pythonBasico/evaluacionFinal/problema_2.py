#Problema 2

class empleado:

  def __init__(self, nombre,numHijos):
    self.nombre=nombre
    self.numHijos=numHijos
  
  def datos(self):
      print("Nombre: ",self.nombre,"\nNumero de hijos: ",self.numHijos)
  

  def asigFamiliar(self):
    if self.numHijos>=1:
      extra=90
    else:
      extra=0
    return extra

class administrativo(empleado):

  def __init__(self, nombre, numHijos, categoria, tipoAporte):
    super().__init__(nombre, numHijos)
    self.categoria=categoria
    self.tipoAporte=tipoAporte

  def Catego(self):
    empleado.datos(self)
    if self.categoria=="A" or self.categoria=="a":
      sueldo=8500
      if self.tipoAporte=="AFP" or self.tipoAporte=="afp":
        descuento=sueldo*0.13
        neto=sueldo-descuento
      else:
        descuento=sueldo*0.12
        neto=sueldo-descuento
    elif self.categoria=="B" or self.categoria=="b":
      sueldo=6500
      if self.tipoAporte=="AFP" or self.tipoAporte=="afp":
        descuento=sueldo*0.13
        neto=sueldo-descuento
      else:
        descuento=sueldo*0.12
        neto=sueldo-descuento
    elif self.categoria=="C" or self.categoria=="c":
      sueldo=3500
      if self.tipoAporte=="AFP" or self.tipoAporte=="afp":
        descuento=sueldo*0.13
        neto=sueldo-descuento
      else:
        descuento=sueldo*0.12
        neto=(sueldo-descuento)
    else:
      print("Valor ingreso no valido")

    print("La asignacion familiar es: ",empleado.asigFamiliar(self),"\nEl descuento es: ",descuento,"\nEl sueldo neto es: ",neto+empleado.asigFamiliar(self))


class ventas(empleado):

    sueldo=1025

    def __init__(self, nombre, numHijos, tipo, ventas):
      super().__init__(nombre, numHijos)
      self.tipo=tipo
      self.ventas=ventas

    def Tipo(self):
      empleado.datos(self)
      if self.tipo=="Externo" or self.tipo=="externo":
        totalventa=self.ventas*0.25
        totalfinal=totalventa+self.sueldo
      elif self.tipo=="Interno" or self.tipo=="interno":
        totalventa=self.ventas*0.12
        totalfinal=totalventa+self.sueldo
      else:
        print("Valor ingreso no valido")
      print("La asignacion familiar es: ",empleado.asigFamiliar(self),"\nSueldo basico: ",self.sueldo,"\nMonto final de ventas: ",totalventa,"Sueldo neto: ",totalfinal+empleado.asigFamiliar(self))

class docentes(empleado):

  def __init__(self, nombre, numHijos, nivel, horas):
    super().__init__(nombre, numHijos)
    self.nivel=nivel
    self.horas=horas

  def Nivel(self):
    empleado.datos(self)
    if self.nivel=="Colegio" or self.nivel=="colegio":
      totolDocent=self.horas*25
    elif self.nivel=="Tecnico" or self.nivel=="Tecnico":
      totolDocent=self.horas*45
    elif self.nivel=="Universitario" or self.nivel=="universitario":
      totolDocent=self.horas*65
    else:
      print("Valor ingreso no valido")
    print("La asignacion familiar es: ",empleado.asigFamiliar(self),"\nPago por dia: ",totolDocent,"\nHoras trabajadas: ",self.horas,"\nSueldo mensual: ",totolDocent*20,"\nSueldo final: ",(totolDocent*20)+empleado.asigFamiliar(self))

print("---------------Administrativo---------------")
#Administrativo
valorAdmin=administrativo("Sebastian Marquez", 1, "A","ONP")
valorAdmin.Catego()

print("--------------------------------------------")
print("---------------Ventas---------------")
#Ventas
valorVentas=ventas("Sebastian Marquez", 6, "Externo",600)

valorVentas.Tipo()

print("------------------------------------")
print("---------------Docentes---------------")
#Docentes

valorDocentes=docentes("Sebastian Marquez", 0, "Tecnico",8)

valorDocentes.Nivel()

print("--------------------------------------")