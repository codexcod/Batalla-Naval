from Celda import Celda

class Tablero:

  def __init__(self, casillas):
    self.celdas = []
    self.casillas = casillas
    for x in range(1,self.casillas + 1):
      for y in range(1,self.casillas + 1):
        self.celdas.append(Celda(x,y))
    

  def getCeldas(self):
    return self.celdas
  
  def getCelda(self,x,y):
    for i in range(len(self.celdas)):
      if(self.celdas[i].x == x and self.celdas[i].y == y):
        return self.celdas[i]

  def dispararPunto(self,x,y):
      self.getCelda(x,y).barco.matarBarco()
      self.getCelda(x,y).color = " M "

  def dibujarTablero(self):
    dibujo = ""
    for y in range (1,self.casillas + 1):
      for x in range (1,self.casillas + 1):
        dibujo += self.getCelda(x,y).color
      dibujo += "\n"
    return dibujo