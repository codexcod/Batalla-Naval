from tablero import Tablero
from Celda import Celda
import random

class Robot:

    def __init__(self,casillas,numBarcos):
        self.casillas = casillas
        self.numBarcos = numBarcos
        self.tablero = Tablero(casillas)
        self.barcoEnMira = False
        self.mira = None
        self.posibilidades=[]
        self.microPosibilidades=[]
        self.aseguradas = []

    def disparar(self,tablero):

        if self.barcoEnMira:
            if len(self.aseguradas) == 0:
                if  len(self.microPosibilidades) == 0:
                    if len(self.posibilidades) == 4 or len(self.posibilidades) == 3:
                        aleatorio =random.randrange(0,len(self.posibilidades))
                        print(f"disparar a {self.posibilidades[aleatorio].x} {self.posibilidades[aleatorio].y}")
                        if tablero.dispararPunto(self.posibilidades[aleatorio].x,self.posibilidades[aleatorio].y):
                            if self.mira.x ==  self.posibilidades[aleatorio].x:
                                diferencia = self.posibilidades[aleatorio].y - self.mira.y
                                print(f"La diferencia es {diferencia}")
                                self.posibilidades.clear()
                                self.microPosibilidades.append(Celda(self.mira.x,self.mira.y - diferencia))
                                self.microPosibilidades.append(Celda(self.mira.x,self.mira.y + diferencia * 2))

                            else:
                                diferencia = self.posibilidades[aleatorio].x - self.mira.x
                                print(f"La diferencia es {diferencia}")
                                self.posibilidades.clear()
                                self.microPosibilidades.append(Celda(self.mira.x - diferencia,self.mira.y ))
                                self.microPosibilidades.append(Celda(self.mira.x + diferencia * 2,self.mira.y ))

                        else:
                            self.posibilidades.remove(self.posibilidades[aleatorio])

                    elif len(self.posibilidades) == 2:
                        aleatorio =random.randrange(0,2)
                        print(f"disparar a {self.posibilidades[aleatorio].x} {self.posibilidades[aleatorio].y}")
                        if tablero.dispararPunto(self.posibilidades[aleatorio].x,self.posibilidades[aleatorio].y):
                            if self.mira.x ==  self.posibilidades[aleatorio].x:
                                diferencia = self.posibilidades[aleatorio].y - self.mira.y
                                self.posibilidades.clear()
                                self.aseguradas.append(Celda(self.mira.x ,self.mira.y + diferencia))

                            else:
                                diferencia = self.posibilidades[aleatorio].x - self.mira.x
                                self.posibilidades.clear()
                                self.aseguradas.append(Celda(self.mira.x  + diferencia,self.mira.y))

                        else:
                            self.aseguradas.append(self.posibilidades[0])
                            if self.mira.x ==  self.posibilidades[0].x:
                                diferencia = self.posibilidades[0].y - self.mira.y
                                self.posibilidades.clear()
                                self.aseguradas.append(Celda(self.mira.x ,self.mira.y - diferencia * 2))

                            else:
                                diferencia = self.posibilidades[0].x - self.mira.x
                                self.posibilidades.clear()
                                self.aseguradas.append(Celda(self.mira.x - diferencia * 2,self.mira.y ))

                else:
                    aleatorio = random.randrange(0,2)
                    print(f" aleatorio es {aleatorio}")
                    print(f"disparar a {self.microPosibilidades[aleatorio].x} {self.microPosibilidades[aleatorio].y}")
                    if tablero.dispararPunto(self.microPosibilidades[aleatorio].x,self.microPosibilidades[aleatorio].y):
                        self.barcoEnMira= False
                        self.mira = None
                    else:
                        self.microPosibilidades.clear()
                        self.aseguradas.append(self.microPosibilidades[0])

            else:
                print(f"disparar a {self.aseguradas[len(self.aseguradas) - 1].x} {self.aseguradas[len(self.aseguradas) - 1 ].y}")
                tablero.dispararPunto(self.aseguradas[len(self.aseguradas) - 1].x,self.aseguradas[len(self.aseguradas) - 1 ].y)
                if len(self.aseguradas) == 1:
                    self.barcoEnMira= False
                    self.mira = None

                self.aseguradas.remove(self.aseguradas[len(self.aseguradas) - 1])

        else:
            x = random.randrange(1, self.casillas + 1)
            y = random.randrange(1, self.casillas + 1)
            celda = tablero.getCelda(x, y)
            while not celda.oculto:
                x = random.randrange(1, self.casillas + 1)
                y = random.randrange(1, self.casillas + 1)
                celda = tablero.getCelda(x, y)

            if tablero.dispararPunto(x,y):
                self.barcoEnMira = True
                self.mira = celda
                self.posibilidades.append(Celda(x,y+1))
                self.posibilidades.append(Celda(x+1,y))
                self.posibilidades.append(Celda(x,y-1))
                self.posibilidades.append(Celda(x-1,y))

        print(f""" 
        {self.barcoEnMira}
        aseguradas:{len(self.aseguradas)} 
                            micro : {len(self.microPosibilidades)}
                            posibilidades = {len(self.posibilidades)}""")


    
