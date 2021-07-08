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
                        if tablero.dispararPunto(self.posibilidades[aleatorio].x,self.posibilidades[aleatorio].y):
                            if self.mira.x ==  self.posibilidades[aleatorio].x:
                                diferencia = self.posibilidades[aleatorio].y - self.mira.y
                                self.posibilidades.clear()
                                if self.chequearCelda(self.mira.x, self.mira.y - diferencia,tablero):
                                    self.microPosibilidades.append(Celda(self.mira.x, self.mira.y - diferencia))
                                if self.chequearCelda(self.mira.x, self.mira.y + diferencia * 2,tablero):
                                    self.microPosibilidades.append(Celda(self.mira.x, self.mira.y + diferencia * 2))


                            else:
                                diferencia = self.posibilidades[aleatorio].x - self.mira.x
                                self.posibilidades.clear()

                                if self.chequearCelda(self.mira.x - diferencia, self.mira.y,tablero):
                                    self.microPosibilidades.append(Celda(self.mira.x - diferencia, self.mira.y))


                                if self.chequearCelda(self.mira.x - diferencia * 2, self.mira.y,tablero):
                                    self.microPosibilidades.append(Celda(self.mira.x + diferencia * 2, self.mira.y))

                            return True

                        else:
                            self.posibilidades.remove(self.posibilidades[aleatorio])
                            return False

                    elif len(self.posibilidades) == 2:
                        aleatorio =random.randrange(0,2)
                        if tablero.dispararPunto(self.posibilidades[aleatorio].x,self.posibilidades[aleatorio].y):
                            if self.mira.x ==  self.posibilidades[aleatorio].x:
                                diferencia = self.posibilidades[aleatorio].y - self.mira.y
                                self.posibilidades.clear()
                                if self.chequearCelda(self.mira.x, self.mira.y - diferencia,tablero):
                                    self.microPosibilidades.append(Celda(self.mira.x, self.mira.y - diferencia))
                                if self.chequearCelda(self.mira.x, self.mira.y + diferencia * 2,tablero):
                                    self.microPosibilidades.append(Celda(self.mira.x, self.mira.y + diferencia * 2))

                            else:
                                diferencia = self.posibilidades[aleatorio].x - self.mira.x
                                self.posibilidades.clear()
                                if self.chequearCelda(self.mira.x - diferencia, self.mira.y,tablero):
                                    self.microPosibilidades.append(Celda(self.mira.x - diferencia, self.mira.y))
                                if self.chequearCelda(self.mira.x - diferencia * 2, self.mira.y,tablero):
                                    self.microPosibilidades.append(Celda(self.mira.x + diferencia * 2, self.mira.y))

                            return True
                        else:
                            self.posibilidades.remove(self.posibilidades[aleatorio])
                            self.aseguradas.append(self.posibilidades[0])
                            if self.mira.x ==  self.posibilidades[0].x:
                                diferencia = self.posibilidades[0].y - self.mira.y
                                self.posibilidades.clear()
                                self.aseguradas.append(Celda(self.mira.x ,self.mira.y + diferencia * 2))

                            else:
                                diferencia = self.posibilidades[0].x - self.mira.x
                                self.posibilidades.clear()
                                self.aseguradas.append(Celda(self.mira.x + diferencia * 2,self.mira.y))

                            return False

                else:
                    aleatorio = random.randrange(0,len(self.microPosibilidades))
                    if tablero.dispararPunto(self.microPosibilidades[aleatorio].x,self.microPosibilidades[aleatorio].y):
                        self.barcoEnMira= False
                        self.mira = None
                        self.microPosibilidades.clear()
                        return True
                    else:
                        self.microPosibilidades.remove(self.microPosibilidades[aleatorio])
                        self.aseguradas.append(self.microPosibilidades[0])
                        self.microPosibilidades.clear()
                        return False

            else:
                tablero.dispararPunto(self.aseguradas[len(self.aseguradas) - 1].x,self.aseguradas[len(self.aseguradas) - 1 ].y)
                if len(self.aseguradas) == 1:
                    self.barcoEnMira = False
                    self.mira = None

                self.aseguradas.remove(self.aseguradas[len(self.aseguradas) - 1])
                return True

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

                if self.chequearCelda(x,y + 1,tablero):
                    self.posibilidades.append(Celda(x,y+1))

                if self.chequearCelda(x+ 1,y,tablero):
                    self.posibilidades.append(Celda(x+1,y))

                if self.chequearCelda(x, y - 1,tablero):
                    self.posibilidades.append(Celda(x,y-1))

                if self.chequearCelda(x- 1, y,tablero):
                    self.posibilidades.append(Celda(x-1,y))

                return True

            else:
                return False

    def chequearCelda(self,x,y,tablero):
        if not tablero.getCelda(x,y) is None:
            if tablero.getCelda(x,y).oculto:
                return True

            return False

        return False



    
