from Celda import Celda

class Tablero:

  def __init__(self, casillas):
    self.celdas = []
    self.casillas = casillas

  def crearTablero(self):
    for x in range(1,self.casillas + 1):
      for y in range(1,self.casillas + 1):
        self.celdas.append(Celda(x,y,False))

  def getCeldas(self):
    return self.celdas
  
  
