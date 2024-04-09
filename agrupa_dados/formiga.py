import random
from dado import *
import math

class Formiga:
    formigas = []
    def __init__(self, id, coordenadaX, coordenadaY, temitem, valor_formiga, raio_visao, dado: Dado=None):
        self.id = id
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.temitem = temitem
        self.valor_formiga = valor_formiga
        self.raio_visao = raio_visao
        self.dado = dado
        Formiga.formigas.append(self)

    def __str__(self):
        return f"ID: {self.id}, {self.coordenadaX}, {self.coordenadaY}, {self.temitem}"

    def pega_larga(self, matriz, linha, coluna, matriz_dado, raio_visao):
        k1 = 0.4
        k2 = 0.8
        alfa = 28
        #eh o pega
        if self.temitem == 0:
            if matriz_dado[self.coordenadaX][self.coordenadaY] is None: #vazio passa
                return 0
            else: #analizar se pega
                semelhanca = Dado.semelhanca(self.coordenadaX, self.coordenadaY, matriz_dado[self.coordenadaX][self.coordenadaY],  matriz_dado, raio_visao, linha, coluna, alfa)
                pegar = (k1 /( k1 + semelhanca)) ** 2
                if pegar >= random.random() and pegar > 0.05:
                    self.dado = matriz_dado[self.coordenadaX][self.coordenadaY]
                    matriz_dado[self.coordenadaX][self.coordenadaY] = None
                    self.temitem = 1
                    # print("peguei", pegar)
        else:
            if matriz_dado[self.coordenadaX][self.coordenadaY] is None:
                semelhanca = Dado.semelhanca(self.coordenadaX, self.coordenadaY, self.dado, matriz_dado, raio_visao, linha, coluna, 28)
                largar = (semelhanca/(k2+semelhanca)) ** 2
                if largar >= random.random() and largar > 0.05:
                    matriz_dado[self.coordenadaX][self.coordenadaY] = self.dado
                    self.dado = None
                    self.temitem = 0
                    # print(largar, "larguei")



    def mover(self, matriz, linha, coluna):
        while True:
            movimento_horizontal = random.randint(-1, 1)
            movimento_vertical = random.randint(-1, 1)
            if ((0 <= self.coordenadaX+movimento_horizontal < linha) and (0 <= self.coordenadaY+movimento_vertical < coluna)) and (movimento_vertical != 0 or movimento_horizontal != 0) and matriz[movimento_horizontal + self.coordenadaX][movimento_vertical+self.coordenadaY] < 5:                        
                        matriz[self.coordenadaX][self.coordenadaY] = 0
                        matriz[self.coordenadaX+movimento_horizontal][self.coordenadaY+movimento_vertical] = self.valor_formiga
                        self.coordenadaX += movimento_horizontal
                        self.coordenadaY += movimento_vertical
            break