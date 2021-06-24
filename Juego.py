from tablero import Tablero
from Celda import Celda
from Barco import Barco

tablero = Tablero(6)


tablero.getCelda(1,2).agregarBarco(Barco())
tablero.getCelda(5,3).agregarBarco(Barco())
tablero.getCelda(3,2).agregarBarco(Barco())

tablero.dispararPunto(5,3)
print(tablero.dibujarTablero())



