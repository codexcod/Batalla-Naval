from tablero import Tablero
from Celda import Celda
from Barco import Barco
from Buque import Buque
from Inteligencia import Robot
import random

tablero = Tablero(int(input("Ingrese el numero de casillas: ")))

tablero.agregarBuque(Buque(3,4,True,1))
tablero.agregarBuque(Buque(7,4,True,1))
tablero.agregarBuque(Buque(5,4,False,1))







robot = Robot(tablero.casillas)
print(tablero.mostrarTablero())



while 4 == 4:
    esperar = input("esperar: ")
    robot.disparar(tablero)
    print(tablero.buques[tablero.getCelda(3, 4).barco.numBuque].estaVivo())
    print(tablero.buques[tablero.getCelda(5, 4).barco.numBuque].estaVivo())
    print(tablero.buques[tablero.getCelda(7, 4).barco.numBuque].estaVivo())
    print(tablero.mostrarTablero())
    print(tablero.dibujarTablero())
















