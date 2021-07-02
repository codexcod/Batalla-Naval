from tablero import Tablero
from Celda import Celda
from Barco import Barco
from Buque import Buque
import random


casillas = int(input("Con cuantas casillas quiere jugar?(9.max): "))
while casillas > 9 or casillas < 1:
    print("Ingrese una cantidad de casillas correcta")
    casillas = int(input("Con cuantas casillas quiere jugar?(9.max): "))

numBarcos = int(input(f"Con cuantos buques  quiere jugar?({casillas * casillas - (casillas)}.max) "))
while numBarcos > casillas * casillas - (casillas) or numBarcos < 1:
    print("Ingrese una cantidad de buques correcta")
    numBarcos = int(input(f"Con cuantos buques quiere jugar?({casillas * casillas - (casillas)}.max) "))


tableroJugador = Tablero(casillas)
tableroRobot = Tablero(casillas)

print(f"""

{tableroJugador.dibujarTablero()}

Selecciona la posicion de los buques

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


    tableroJugador.agregarBuque(Buque(x,y,True,1))
    print(tableroJugador.mostrarTablero())

tableroRobot.cargarBuques(numBarcos)

print(f"""
Comienza el juego!

{tableroJugador.mostrarTablero()}

{tableroRobot.dibujarTablero()}

""")

puntosJugador = 0
puntosRobot = 0

while puntosRobot != numBarcos * 3 and puntosJugador != numBarcos * 3:
    print("¿Donde vas a disparar?")
    x = int(input("x: "))
    while x > casillas or x < 1:
        print("Fuera de rango")
        x = int(input("x: "))

    y = int(input("y: "))
    while y > casillas or y < 1:
        print("Fuera de rango")
        y = int(input("x: "))


    if tableroJugador.dispararAleatorio():
        print(tableroJugador.mostrarTablero())
        print(chr(27)+"[1;31m"+"""
Encontraron uno de tus  barcos!
""")
        print(chr(27)+"[37m" + "")
        puntosRobot += 1
    else:
        print(tableroJugador.mostrarTablero())

    if tableroRobot.dispararPunto(x,y):
        print(tableroRobot.dibujarTablero())
        print(chr(27) + "[1;32m" + """
Le diste a un barco!
        """)
        print(chr(27) + "[37m" + "")
        puntosJugador += 1
    else:
        print(tableroRobot.dibujarTablero())

    print(f"{puntosRobot}  {puntosJugador}")




if puntosRobot > puntosJugador:
    print("Te gano un robot jajajaj")

elif puntosRobot == puntosJugador:
    print("Empataste con un robot jjajaj")

elif puntosJugador > puntosRobot:
    print("Ganaste contra la maquina")

