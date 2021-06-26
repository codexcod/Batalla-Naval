from tablero import Tablero
from Celda import Celda
from Barco import Barco
import random

tablero = Tablero(int(input("Ingrese el numero de casillas: ")))
puntos = 0
cantidadBarcos = int(input("Ingrese la cantidad de barcos: "))

tablero.cargarBarcos(cantidadBarcos)

print(tablero.dibujarTablero())

while(puntos < cantidadBarcos):
  if(tablero.dispararPunto(int(input("Disparar x: ")),int(input("Disparar y: ")))):
    print("Barco encontrado")
    puntos += 1
  else:
    print("No se encontro nada")

  print(tablero.dibujarTablero())

print("Ganaste el juego!")



