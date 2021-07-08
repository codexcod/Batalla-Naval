from tablero import Tablero
from Inteligencia import Robot

casillas = int(input("casillas: "))
tableroAleatorio = Tablero(casillas)
tableroInteligencia = Tablero(casillas)

numBarcos = int(input("barcos: "))

tableroInteligencia.cargarBuques(numBarcos)
tableroAleatorio.cargarBuques(numBarcos)

robot = Robot(casillas,numBarcos)

puntosInteligencia = 0
puntosAleatorio = 0

while puntosInteligencia != numBarcos * 3 and puntosAleatorio != numBarcos * 3:
    esperar = input("esperar :")
    if robot.disparar(tableroAleatorio):
        puntosInteligencia += 1
        print(chr(27) + "[1;32m" + "La inteligencia mato a un barco")
        print(chr(27) + "[37m" + "")

    if tableroInteligencia.dispararAleatorio():
        puntosAleatorio += 1
        print(chr(27) + "[1;31m" + "¡Le pego el aleatorio!")
        print(chr(27) + "[37m" + "")


    print("Aleatorio :")
    print(tableroAleatorio.dibujarTablero())
    print("Inteligencia :")
    print(tableroInteligencia.dibujarTablero())

if puntosAleatorio > puntosInteligencia:
    print("Gano el aleatorio")

elif puntosAleatorio == puntosInteligencia:
    print("Empataron")

elif puntosInteligencia > puntosAleatorio:
    print("Gano la inteligencia")


