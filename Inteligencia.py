from tablero import Tablero
from Celda import Celda
import random

class Robot:

    def __init__(self,casillas):
        self.casillas = casillas
        self.barcoEnMira = False
        self.mira = None
        self.posibilidades=[]
        self.microPosibilidades=[]
        self.aseguradas = []
        self.posibilidadesSecundarias = []
        self.posibildadSecundaria = None

    def disparar(self,tablero):
        if len(self.posibilidadesSecundarias) > 0 and not self.barcoEnMira:
            self.barcoEnMira = True
            self.mira = self.posibilidadesSecundarias[len(self.posibilidadesSecundarias) - 1]
            self.posibilidadesSecundarias.clear()
            self.pensarPosibilidades(self.mira,tablero)


        if self.barcoEnMira:
            print(f"""
aseguradas : {len(self.aseguradas)}
posibilidades : {len(self.posibilidades)}
micro: {len(self.microPosibilidades)}
secon : {len(self.posibilidadesSecundarias)}""")
            if len(self.aseguradas) == 0:
                if  len(self.microPosibilidades) == 0:
                    if len(self.posibilidades) == 4 or len(self.posibilidades) == 3:
                        aleatorio = random.randrange(0,len(self.posibilidades))
                        if tablero.dispararPunto(self.posibilidades[aleatorio].x,self.posibilidades[aleatorio].y):
                            self.posibildadSecundaria = self.posibilidades[aleatorio]
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


                                if self.chequearCelda(self.mira.x + diferencia * 2, self.mira.y,tablero):
                                    self.microPosibilidades.append(Celda(self.mira.x + diferencia * 2, self.mira.y))

                            return True

                        else:
                            self.posibilidades.remove(self.posibilidades[aleatorio])
                            self.pensarPosibilidades(self.mira,tablero)
                            return False

                    elif len(self.posibilidades) == 2:
                        aleatorio =random.randrange(0,2)
                        if tablero.dispararPunto(self.posibilidades[aleatorio].x,self.posibilidades[aleatorio].y):
                            if self.posibildadSecundaria == None:
                                self.posibildadSecundaria = self.posibilidades[aleatorio]

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
                                if self.chequearCelda(self.mira.x + diferencia * 2, self.mira.y,tablero):
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

                    elif len(self.posibilidades) == 1:
                        disparo = tablero.dispararPunto(self.posibilidades[0].x, self.posibilidades[0].y)
                        if self.mira.x == self.posibilidades[0].x:
                            diferencia = self.posibilidades[0].y - self.mira.y
                            self.posibilidades.clear()
                            self.aseguradas.append(Celda(self.mira.x, self.mira.y + diferencia * 2))

                        else:
                            diferencia = self.posibilidades[0].x - self.mira.x
                            self.posibilidades.clear()
                            self.aseguradas.append(Celda(self.mira.x + diferencia * 2, self.mira.y))

                        return disparo



                else:
                    aleatorio = random.randrange(0,len(self.microPosibilidades))
                    if tablero.dispararPunto(self.microPosibilidades[aleatorio].x,self.microPosibilidades[aleatorio].y):
                        if tablero.buques[tablero.getCelda(self.microPosibilidades[aleatorio].x,self.microPosibilidades[aleatorio].y).barco.numBuque].estaVivo():
                            self.microPosibilidades.clear()
                            self.posibilidadesSecundarias.append(self.posibildadSecundaria)
                            self.pensarPosibilidades(self.mira,tablero)

                        else:
                            self.limpiarMira()

                        return True

                    else:
                        if len(self.microPosibilidades) > 1:
                            self.microPosibilidades.remove(self.microPosibilidades[aleatorio])
                            self.aseguradas.append(self.microPosibilidades[0])
                            self.microPosibilidades.clear()
                        else:
                            self.microPosibilidades.clear()
                            self.posibilidadesSecundarias.append(self.posibildadSecundaria)
                            self.pensarPosibilidades(self.mira,tablero)


                        return False

            else:
                disparo = tablero.dispararPunto(self.aseguradas[len(self.aseguradas) - 1].x,self.aseguradas[len(self.aseguradas) - 1 ].y)
                if len(self.aseguradas) == 1:
                    if disparo:
                        if tablero.buques[tablero.getCelda(self.aseguradas[len(self.aseguradas) - 1].x,self.aseguradas[len(self.aseguradas) - 1].y).barco.numBuque].estaVivo():
                            self.pensarPosibilidades(self.mira,tablero)
                            self.aseguradas.clear()
                            self.posibilidadesSecundarias.append(self.posibildadSecundaria)
                            return True

                        else:
                            self.limpiarMira()
                            return True

                    else:
                        self.pensarPosibilidades(self.mira, tablero)
                        self.aseguradas.clear()
                        self.posibilidadesSecundarias.append(self.posibildadSecundaria)
                        return False

                else:
                    self.aseguradas.remove(self.aseguradas[len(self.aseguradas) - 1])
                    return disparo





        else:
                celda = self.buscarBarcos(tablero)

                if tablero.dispararPunto(celda.x,celda.y):
                    self.barcoEnMira = True
                    self.mira = celda

                    self.pensarPosibilidades(celda,tablero)

                    return True

                else:
                    return False



    def chequearCelda(self,x,y,tablero):
        if not tablero.getCelda(x,y) is None:
            if tablero.getCelda(x,y).oculto:
                return True

            return False

        return False

    def limpiarMira(self):
        self.mira = None
        self.barcoEnMira = False
        self.posibilidades.clear()
        self.microPosibilidades.clear()
        self.aseguradas.clear()


    def pensarPosibilidades(self,celda,tablero):
        self.aseguradas.clear()
        self.posibilidades.clear()
        if self.chequearCelda(celda.x, celda.y + 1, tablero):
            if self.chequearCelda(celda.x, celda.y - 1, tablero) or self.chequearCelda(celda.x, celda.y + 2, tablero):
                self.posibilidades.append(Celda(celda.x, celda.y + 1))

        if self.chequearCelda(celda.x + 1, celda.y, tablero):
            if self.chequearCelda(celda.x - 1, celda.y, tablero) or self.chequearCelda(celda.x + 2, celda.y, tablero):
                self.posibilidades.append(Celda(celda.x + 1, celda.y))

        if self.chequearCelda(celda.x, celda.y - 1, tablero):
            if self.chequearCelda(celda.x, celda.y + 1, tablero) or self.chequearCelda(celda.x, celda.y - 2, tablero):
                self.posibilidades.append(Celda(celda.x, celda.y - 1))

        if self.chequearCelda(celda.x - 1, celda.y, tablero):
            if self.chequearCelda(celda.x + 1, celda.y, tablero) or self.chequearCelda(celda.x - 2, celda.y, tablero):
                self.posibilidades.append(Celda(celda.x - 1, celda.y))

        if len(self.posibilidadesSecundarias) > 0:
            if tablero.buques[tablero.getCelda(self.posibilidadesSecundarias[0].x,
                                               self.posibilidadesSecundarias[0].y).barco.numBuque].estaVivo():
                if celda.x == self.posibilidadesSecundarias[0].x:
                    diferencia = self.posibilidadesSecundarias[0].y - celda.y
                    self.posibilidadesSecundarias.clear()
                    self.posibilidadesSecundarias.append(Celda(celda.x, celda.y + diferencia))

                else:
                    diferencia = self.posibilidadesSecundarias[0].x - celda.x
                    self.posibilidadesSecundarias.clear()
                    self.posibilidadesSecundarias.append(Celda(celda.x + diferencia, celda.y))


        if tablero.buques[tablero.getCelda(celda.x,celda.y).barco.numBuque].estaVivo():
            if not tablero.getCelda(celda.x + 1, celda.y) is None:
                if not tablero.getCelda(celda.x + 1,celda.y).barco is None:
                    if tablero.getCelda(celda.x + 1,celda.y).barco.estado == False:

                        if self.chequearCelda(celda.x + 2,celda.y,tablero):
                            self.microPosibilidades.append(Celda(celda.x + 2,celda.y))


                        if self.chequearCelda(celda.x - 1,celda.y,tablero):
                            self.microPosibilidades.append(Celda(celda.x - 1,celda.y))

            if not tablero.getCelda(celda.x - 1, celda.y) is None:
                if not tablero.getCelda(celda.x - 1,celda.y).barco is None:
                    if tablero.getCelda(celda.x - 1,celda.y).barco.estado == False:

                        if self.chequearCelda(celda.x - 2, celda.y, tablero):
                            self.microPosibilidades.append(Celda(celda.x - 2, celda.y))


                        if self.chequearCelda(celda.x + 1, celda.y, tablero):
                            self.microPosibilidades.append(Celda(celda.x + 1, celda.y))

            if not tablero.getCelda(celda.x, celda.y + 1) is None:
                if not tablero.getCelda(celda.x,celda.y + 1).barco is None:
                    if tablero.getCelda(celda.x,celda.y + 1).barco.numBuque == tablero.getCelda(celda.x,celda.y).barco.numBuque and tablero.getCelda(celda.x,celda.y + 1).barco.estado == False:
                        if self.chequearCelda(celda.x, celda.y + 2, tablero):
                            self.microPosibilidades.append(Celda(celda.x, celda.y + 2))

                        if self.chequearCelda(celda.x, celda.y - 1, tablero):
                            self.microPosibilidades.append(Celda(celda.x, celda.y - 1))

            if not tablero.getCelda(celda.x,celda.y - 1) is None:
                if not tablero.getCelda(celda.x,celda.y - 1).barco is None:
                    if tablero.getCelda(celda.x,celda.y - 1).barco.numBuque == tablero.getCelda(celda.x,celda.y).barco.numBuque and tablero.getCelda(celda.x,celda.y - 1).barco.estado == False:
                        if self.chequearCelda(celda.x, celda.y - 2, tablero):
                            self.microPosibilidades.append(Celda(celda.x, celda.y - 2))

                        if self.chequearCelda(celda.x, celda.y + 1, tablero):
                            self.microPosibilidades.append(Celda(celda.x, celda.y + 1))




    def calcularPosibilidades(self,celda,tablero):
        posibilidades = 0
        if self.chequearCelda(celda.x + 1,celda.y,tablero) and self.chequearCelda(celda.x + 2,celda.y,tablero):
            posibilidades += 1

        if self.chequearCelda(celda.x + 1,celda.y,tablero) and self.chequearCelda(celda.x - 1,celda.y,tablero):
            posibilidades += 1

        if self.chequearCelda(celda.x - 1,celda.y,tablero) and self.chequearCelda(celda.x - 2,celda.y,tablero):
            posibilidades += 1

        if self.chequearCelda(celda.x,celda.y + 1,tablero) and self.chequearCelda(celda.x,celda.y + 2,tablero):
            posibilidades += 1

        if self.chequearCelda(celda.x,celda.y + 1,tablero) and self.chequearCelda(celda.x,celda.y - 1,tablero):
            posibilidades += 1

        if self.chequearCelda(celda.x,celda.y - 1,tablero) and self.chequearCelda(celda.x,celda.y - 2,tablero):
            posibilidades += 1

        return posibilidades


    def buscarBarcos(self,tablero):
        posiblesCeldas = []
        max = 0
        mejorPosibilidad = 0
        for i in range(0,5):
            x = random.randrange(1, self.casillas + 1)
            y = random.randrange(1, self.casillas + 1)
            celda = tablero.getCelda(x, y)
            while not celda.oculto:
                x = random.randrange(1, self.casillas + 1)
                y = random.randrange(1, self.casillas + 1)
                celda = tablero.getCelda(x, y)


            posibilidades = self.calcularPosibilidades(celda,tablero)
            if posibilidades > max:
                max = posibilidades
                mejorPosibilidad = i

            posiblesCeldas.append(celda)

        return posiblesCeldas[mejorPosibilidad]



    
