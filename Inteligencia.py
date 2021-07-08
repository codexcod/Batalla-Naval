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
        print(f""" aseguradas:{len(self.aseguradas)} 
                    micro : {len(self.microPosibilidades)}
                    posibilidades = {len(self.posibilidades)}""")
        if self.barcoEnMira:
            if not len(self.aseguradas) > 0:
                if not len(self.microPosibilidades) > 0:
                    if len(self.posibilidades) == 4 or len(self.posibilidades) == 3:
                        aleatorio =random.randrange(0,len(self.posibilidades))
                        if tablero.dispararPunto(self.posibilidades[aleatorio].x,self.posibilidades[aleatorio].y):
                            if self.mira.x ==  self.posibilidades[aleatorio].x:
                                diferencia = self.posibilidades[aleatorio].x - self.mira.x
                                self.posibilidades.clear()
                                self.microPosibilidades.append(Celda(self.mira.x - diferencia,self.mira.y))
                                self.microPosibilidades.append(Celda(self.mira.x + diferencia * 2,self.mira.y))

                            else:
                                diferencia = self.posibilidades[aleatorio].y - self.mira.y
                                self.posibilidades.clear()
                                self.microPosibilidades.append(Celda(self.mira.x,self.mira.y - diferencia))
                                self.microPosibilidades.append(Celda(self.mira.x,self.mira.y + diferencia * 2))

                        else:
                            self.posibilidades.remove(self.posibilidades[aleatorio])

                    elif len(self.posibilidades) == 2:
                        aleatorio =random.randrange(0,2)
                        if tablero.dispararPunto(self.posibilidades[aleatorio].x,self.posibilidades[aleatorio].y):
                            if self.mira.x ==  self.posibilidades[aleatorio].x:
                                diferencia = self.posibilidades[aleatorio].x - self.mira.x
                                self.posibilidades.clear()
                                self.aseguradas.append(Celda(self.mira.x - diferencia,self.mira.y))

                            else:
                                diferencia = self.posibilidades[aleatorio].y - self.mira.y
                                self.posibilidades.clear()
                                self.aseguradas.append(Celda(self.mira.x,self.mira.y - diferencia))

                        else:
                            self.aseguradas.append(self.posibilidades[0])
                            self.posibilidades.clear()
                else:
                    aleatorio = random.randrange(0,2)
                    if tablero.dispararPunto(self.microPosibilidades[aleatorio].x,self.microPosibilidades[aleatorio].y):
                        self.barcoEnMira= False
                        self.mira = None
                    else:
                        self.microPosibilidades.remove(self.microPosibilidades[aleatorio])
                        self.aseguradas.append(self.microPosibilidades[0])

            else:
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


    
