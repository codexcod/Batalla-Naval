from tablero import Tablero
from Celda import Celda
from Barco import Barco
import random


casillas = int(input("Con cuantas casillas quiere jugar?(9.max): "))
while casillas > 9 or casillas < 1:
    print("Ingrese una cantidad de casillas correcta")
    casillas = int(input("Con cuantas casillas quiere jugar?(9.max): "))

numBarcos = int(input(f"Con cuantos barcos jugara quiere jugar?({casillas * casillas - (casillas)}.max) "))
while numBarcos > casillas * casillas - (casillas) or numBarcos < 1:
    print("Ingrese una cantidad de barcos correcta")
    numBarcos = int(input(f"Con cuantos barcos jugara quiere jugar?({casillas * casillas - (casillas)}.max) "))


tableroJugador = Tablero(casillas)
tableroRobot = Tablero(casillas)

print(f"""

{tableroJugador.dibujarTablero()}

Selecciona la posicion de los barcos

""")

for i in range(1,numBarcos + 1):
    print(f"Barco numero {i}")
    x = int(input("x: "))
    while x > casillas or x < 1:
        print("Fuera de rango")
        x = int(input("x: "))

    y = int(input("y: "))

    while y > casillas or y < 1:
        print("Fuera de rango")
        y = int(input("x: "))

    tableroJugador.getCelda(x,y).agregarBarco(Barco())
    print(tableroJugador.mostrarTablero())

tableroRobot.cargarBarcos(numBarcos)

print(f"""
Comienza el juego!

{tableroJugador.mostrarTablero()}

{tableroRobot.dibujarTablero()}

""")

puntosJugador = 0
puntosRobot = 0

while puntosRobot < numBarcos or puntosJugador < numBarcos:
    print("¿Donde vas a disparar?")
    x = int(input("x: "))
    while x > casillas or x < 1:
        print("Fuera de rango")
        x = int(input("x: "))

    y = int(input("y: "))
    while y > casillas or y < 1:
        print("Fuera de rango")
        y = int(input("x: "))

    disparoJugador = tableroRobot.dispararPunto(x,y)

    disparoRobot = tableroJugador.dispararAleatorio()

    print(tableroJugador.mostrarTablero())
    print(tableroRobot.dibujarTablero())











