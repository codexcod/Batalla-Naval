from Celda import Celda
from Barco import Barco
import string
import random

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
      if self.celdas[i].x == x and self.celdas[i].y == y:
        return self.celdas[i]

  def dispararPunto(self,x,y):
    if x <= self.casillas or y <= self.casillas:
      if self.getCelda(x,y).ocupado:
        self.getCelda(x,y).barco.matarBarco()
        self.getCelda(x,y).color = " M "
        self.getCelda(x,y).oculto = False
        return True
      else:
        self.getCelda(x,y).color = " N "
        self.getCelda(x,y).oculto = False
        return False  
    else:
      return False

  def dibujarTablero(self):
    dibujo = "   "
    letras = list(string.ascii_lowercase)
    for x in range (self.casillas):
      dibujo += f" {letras[x]} "
    
    dibujo += "\n"
    for y in range (1,self.casillas + 1):
      dibujo += f" {y} "
      for x in range (1,self.casillas + 1):

        if(self.getCelda(x,y).oculto):
            dibujo += " · "
        else:
          dibujo += self.getCelda(x,y).color

      dibujo += "\n"
    return dibujo

  def mostrarTablero(self):
    dibujo = "   "
    letras = list(string.ascii_lowercase)
    for x in range (self.casillas):
      dibujo += f" {letras[x]} "
    
    dibujo += "\n"
    for y in range (1,self.casillas + 1):
      dibujo += f" {y} "
      for x in range (1,self.casillas + 1):
        dibujo += self.getCelda(x,y).color

      dibujo += "\n"
      
    return dibujo

  def cargarBarcos(self,cantidadBarcos):
    for i in range(cantidadBarcos):
      celda = self.getCelda(random.randrange(1, self.casillas + 1 ),random.randrange(1, self.casillas + 1))
      
      while(celda.ocupado):
        celda = self.getCelda(random.randrange(1, self.casillas + 1),random.randrange(1, self.casillas + 1))

      if(not celda.ocupado):
        celda.agregarBarco(Barco())
        celda.ocupado = True

  def dispararAleatorio(self):
    x = random.randrange(1, self.casillas + 1)
    y = random.randrange(1, self.casillas + 1)
    celda = self.getCelda(x, y)
    while not celda.oculto:
      x = random.randrange(1, self.casillas + 1)
      y = random.randrange(1, self.casillas + 1)
      celda = self.getCelda(x, y)

    return self.dispararPunto(x,y)
