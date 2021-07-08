from tablero import Tablero
from Celda import Celda
from Barco import Barco
from Buque import Buque
from Inteligencia import Robot
import random

tablero = Tablero(int(input("Ingrese el numero de casillas: ")))

tablero.agregarBuque(Buque(5,5,False,1))
tablero.agregarBuque(Buque(2,4,True,1))
tablero.agregarBuque(Buque(6,2,True,1))

robot = Robot(tablero.casillas,1)
print(tablero.mostrarTablero())

while 4 == 4:
    esperar = input("esperar: ") 
    robot.disparar(tablero)
    print(tablero.mostrarTablero())













