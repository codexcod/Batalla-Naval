from Barco import Barco

class Buque:

  def __init__(self,barcos,x,y):
    self.vidas = len(barcos)
    self.vivo = False
    self.x = x
    self.y = y
    
  