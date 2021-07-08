from tablero import Tablero
from Celda import Celda
from Barco import Barco
from Buque import Buque
from Inteligencia import Robot
import random

tablero = Tablero(int(input("Ingrese el numero de casillas: ")))

tablero.agregarBuque(Buque(4,4,False,1))

robot = Robot(tablero.casillas,1)
print(tablero.mostrarTablero())

while 4 == 4:
    esperar = input("esperar: ") 
    robot.disparar(tablero)
    print(tablero.mostrarTablero())













