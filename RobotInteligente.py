from tablero import Tablero
from Celda import Celda
from Barco import Barco
from Buque import Buque
from Inteligencia import Robot
import random


casillas = int(input("Con cuantas casillas quiere jugar?(9.max): "))
while casillas > 9 or casillas < 1:
    print("Ingrese una cantidad de casillas correcta")
    casillas = int(input("Con cuantas casillas quiere jugar?(9.max): "))

numBarcos = int(input(f"Con cuantos buques  quiere jugar?({casillas * casillas - (casillas)}.max) "))
while numBarcos > casillas * casillas - (casillas) or numBarcos < 1:
    print("Ingrese una cantidad de buques correcta")
    numBarcos = int(input(f"Con cuantos buques quiere jugar?({casillas * casillas - (casillas)}.max) "))

inputDificultad = ""
while not inputDificultad.isnumeric():

    inputDificultad = input("Dificultad del robot:  ")
    if inputDificultad.isnumeric():
        if int(inputDificultad) < 0:
            print("Escriba un numero mayor a 0")
            inputDificultad = ""

        else:
            dificultad = int(inputDificultad)




tableroJugador = Tablero(casillas)
tableroRobot = Tablero(casillas)
robot = Robot(casillas,dificultad)

print(f"""

{tableroJugador.dibujarTablero()}

Selecciona la posicion de los buques

""")

for i in range(1,numBarcos + 1):
    x = 0
    y = 0
    print(f"Barco numero {i}")
    inputX = ""
    while not inputX.isnumeric():
        inputX = input("x: ")
        if inputX.isnumeric():
            if int(inputX) > casillas or int(inputX) < 1:
                inputX = ""
                print("Fuera de rango")

            else:
                x = int(inputX)

    inputY = ""
    while not inputY.isnumeric():
        inputY = input("y: ")
        if inputY.isnumeric():
            if int(inputY) > casillas or int(inputY) < 1:
                print("Fuera de rango")
                inputY = ""

            else:
                y = int(inputY)

    print(inputX)
    print(y)

    orientacion = input("indique la orientacion(V/H)")
    while not tableroJugador.agregarBuque(Buque(x,y,orientacion == "v" or orientacion =="V",1)):
        print(chr(27) + "[1;31m" + "¡Ya hay un barco ocupando esos espacios!")
        print(chr(27) + "[37m" + "")
        print(f"Barco numero {i}")
        inputX = ""
        while not inputX.isnumeric():
            inputX = input("x: ")
            if inputX.isnumeric():
                if int(inputX) > casillas or int(inputX) < 1:
                    inputX = ""
                    print("Fuera de rango")
                    continue

                else:
                    x = int(inputX)

        inputY = ""
        while not inputY.isnumeric():
            inputY = input("y: ")
            if inputY.isnumeric():
                if int(inputY) > casillas or int(inputY) < 1:
                    print("Fuera de rango")
                    inputY = ""
                    continue

                else:
                    y = int(inputY)

        orientacion = input("indique la orientacion(V/H)")

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
    x = 0
    y = 0
    print("¿Donde vas a disparar?")
    inputX = ""
    while not inputX.isnumeric():
        inputX = input("x: ")
        if inputX.isnumeric():
            if int(inputX) > casillas or int(inputX) < 1:
                inputX = ""
                print("Fuera de rango")
                continue

            else:
                x = int(inputX)

    inputY = ""
    while not inputY.isnumeric():
        inputY = input("y: ")
        if inputY.isnumeric():
            if int(inputY) > casillas or int(inputY) < 1:
                print("Fuera de rango")
                inputY = ""
                continue

            else:
                y = int(inputY)


    while not tableroRobot.getCelda(x,y).oculto:
        print(chr(27) + "[1;31m" + "¡Ya disparaste a ese punto!")
        print(chr(27) + "[37m" + "")
        print("¿Donde vas a disparar?")

        inputX = ""
        while not inputX.isnumeric():
            inputX = input("x: ")
            if inputX.isnumeric():
                if int(inputX) > casillas or int(inputX) < 1:
                    inputX = ""
                    print("Fuera de rango")
                    continue
                else:
                    x = int(inputX)

        inputY = ""
        while not inputY.isnumeric():
            inputY = input("y: ")
            if inputY.isnumeric():
                if int(inputY) > casillas or int(inputY) < 1:
                    print("Fuera de rango")
                    inputY = ""
                    continue

                else:
                    y = int(inputY)

    if robot.disparar(tableroJugador):
        print(tableroJugador.mostrarTablero())
        print(chr(27)+"[1;31m"+"""Encontraron uno de tus  barcos!""")
        print(chr(27)+"[37m" + "")
        puntosRobot += 1
    else:
        print(tableroJugador.mostrarTablero())

    if tableroRobot.dispararPunto(x,y):
        print(tableroRobot.dibujarTablero())
        print(chr(27) + "[1;32m" + """Le diste a un barco!""")
        print(chr(27) + "[37m" + "")
        puntosJugador += 1
    else:
        print(tableroRobot.dibujarTablero())

    puntacion = "Jugador           Maquina"
    for i in range(0,len(tableroJugador.buques)):
        puntacion += "\n"
        puntacion += f"Barco {i + 1}: "
        if tableroJugador.buques[i].estaVivo():
            puntacion += chr(27) + "[1;32m" + "Vivo   "
            puntacion += chr(27) + "[37m" + ""
        else:
            puntacion += chr(27) + "[1;31m" + "Muerto "
            puntacion += chr(27) + "[37m" + ""

        puntacion += f"Barco {i + 1}: "
        if tableroRobot.buques[i].estaVivo():
            puntacion += chr(27) + "[1;32m" + "Vivo   "
            puntacion += chr(27) + "[37m" + ""
        else:
            puntacion += chr(27) + "[1;31m" + "Muerto "
            puntacion += chr(27) + "[37m" + ""

    print(f"{puntacion}")





if puntosRobot > puntosJugador:
    print("Te gano un robot jajajaj")

elif puntosRobot == puntosJugador:
    print("Empataste con un robot jjajaj")

elif puntosJugador > puntosRobot:
    print("Ganaste contra la maquina")

