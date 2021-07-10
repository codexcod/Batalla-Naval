from Barco import Barco

class Buque:

  def __init__(self,x,y,orientacion,largo):
    self.x = x
    self.y = y
    self.orientacion = orientacion
    self.largo = largo
    self.barcos = []


  def agregarBarco(self,barco):
    self.barcos.append(barco)

  def eliminarBarco(self,barco):
    self.barcos.remove(barco)

  def estaVivo(self):
    return len(self.barcos) > 0

    
  