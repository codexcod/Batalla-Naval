from tablero import Tablero
from Celda import Celda
from Barco import Barco
import random

tablero = Tablero(int(input("Ingrese el numero de casillas: ")))

print(tablero.agregarBuque(5,5,False,5))


print(tablero.mostrarTablero())





