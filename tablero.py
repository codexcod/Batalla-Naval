from Celda import Celda
from Barco import Barco
from Buque import Buque
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
    for i in self.celdas:
      if i.x == x and i.y == y:
        return i
      
      

  def agregarBuque(self,buque):
    if buque.orientacion:
      if self.getCelda(buque.x,buque.y + buque.largo) is None or self.getCelda(buque.x,buque.y - buque.largo) is None or self.getCelda(buque.x,buque.y).ocupado:
        return False

      else:
        for i in range(1, buque.largo + 1):
          if self.getCelda(buque.x, buque.y + i).ocupado or self.getCelda(buque.x, buque.y - i).ocupado:
            return False

          else:
            self.getCelda(buque.x, buque.y + i).agregarBarco(Barco())
            self.getCelda(buque.x, buque.y + i).ocupado = True
            self.getCelda(buque.x, buque.y - i).agregarBarco(Barco())
            self.getCelda(buque.x, buque.y - i).ocupado = True

          self.getCelda(buque.x, buque.y).agregarBarco(Barco())
          return True

    else:
      if self.getCelda(buque.x + buque.largo,buque.y) is None or self.getCelda(buque.x - buque.largo,buque.y) is None:
        return False

      else:

        for i in range(1, buque.largo + 1):
          if self.getCelda(buque.x - i, buque.y).ocupado or self.getCelda(buque.x + i, buque.y).ocupado:
            return False
          else:
            self.getCelda(buque.x - i, buque.y).agregarBarco(Barco())
            self.getCelda(buque.x - i, buque.y).ocupado = True
            self.getCelda(buque.x + i, buque.y).agregarBarco(Barco())
            self.getCelda(buque.x + i, buque.y).ocupado = True

        self.getCelda(buque.x, buque.y).agregarBarco(Barco())
        return True





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

  def cargarBuques(self,cantidadBarcos):
    for i in range(cantidadBarcos):
      buque = self.agregarBuque(Buque(random.randrange(1, self.casillas + 1), random.randrange(1, self.casillas + 1), bool(random.randrange(0,2)),1))
      while (not buque):
        buque = self.agregarBuque(Buque(random.randrange(1, self.casillas + 1), random.randrange(1, self.casillas + 1), bool(random.randrange(0,2)),1))


  def dispararAleatorio(self):
    x = random.randrange(1, self.casillas + 1)
    y = random.randrange(1, self.casillas + 1)
    celda = self.getCelda(x, y)
    while not celda.oculto:
      x = random.randrange(1, self.casillas + 1)
      y = random.randrange(1, self.casillas + 1)
      celda = self.getCelda(x, y)

    return self.dispararPunto(x,y)
