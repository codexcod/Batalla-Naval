from tablero import Tablero
from Celda import Celda
from Barco import Barco
from Buque import Buque
import random

tablero = Tablero(int(input("Ingrese el numero de casillas: ")))

tablero.cargarBuques(10)

print(tablero.mostrarTablero())













