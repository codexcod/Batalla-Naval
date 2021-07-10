class Barco:
  def __init__(self):
    self.estado = True
    self.numBuque = None
    
  
  def matarBarco(self): 
    self.estado = False


  def setNumBuque(self,numero):
    self.numBuque = numero
    