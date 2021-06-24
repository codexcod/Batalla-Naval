from tablero import Tablero
from Celda import Celda
from Barco import Barco

tablero = Tablero(8)

tablero.crearTablero()

for x in range(len(tablero.celdas)):
     print(f"x : {tablero.celdas[x].x} y : {tablero.celdas[x].y}")

tablero.getCelda(1,2).agregarBarco(Barco())
tablero.getCelda(5,3).agregarBarco(Barco())
tablero.getCelda(3,2).agregarBarco(Barco())

tablero.dispararPunto(5,3)

print(f"{tablero.getCelda(5,3).barco.estado}")


