
class Celda:
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.ocupado = False
    self.barco = None

  def agregarBarco(self, barco):
    self.barco = barco
    self.ocupado = True