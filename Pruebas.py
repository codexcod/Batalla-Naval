from tablero import Tablero
from Celda import Celda
from Barco import Barco
from Buque import Buque
import random

tablero = Tablero(int(input("Ingrese el numero de casillas: ")))



print(tablero.agregarBuque(Buque(1,1,True,1)))
print(tablero.agregarBuque(Buque(1,1,False,1)))













