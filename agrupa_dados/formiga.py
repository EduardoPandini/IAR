import random
class Formiga:
    formigas = []
    def __init__(self, id, coordenadaX, coordenadaY, temitem, valor_cel, valor_formiga, raio_visao):
        self.id = id
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.temitem = temitem
        self.valor_cel = valor_cel
        self.valor_formiga = valor_formiga
        self.raio_visao = raio_visao
        Formiga.formigas.append(self)

    def __str__(self):
        return f"ID: {self.id}, {self.coordenadaX}, {self.coordenadaY}, {self.temitem}"

    def pega_larga(self, matriz, linha, coluna):
        cheias =  0
        if self.temitem == 0:
            if matriz[self.coordenadaX][self.coordenadaY] == self.valor_formiga:
                return 0
            else:
                for i in range(-self.raio_visao,self.raio_visao+1):
                    for j in range(-self.raio_visao,self.raio_visao+1):
                        if 0 < self.coordenadaX + i >= linha or 0 < self.coordenadaY + j >= coluna:
                            continue
                        if matriz[self.coordenadaX+i][self.coordenadaY+j] == matriz[self.coordenadaX][self.coordenadaY] - self.valor_formiga or matriz[self.coordenadaX][self.coordenadaY] == matriz[self.coordenadaX+i][self.coordenadaY+j]:
                            cheias += 1
                #funcao pra pegar
        else:
            if matriz[self.coordenadaX][self.coordenadaY] != self.valor_formiga:
                return 0
            else:
                for i in range(-self.raio_visao,self.raio_visao+1):
                    for j in range(-self.raio_visao,self.raio_visao+1):
                        if 0 < self.coordenadaX + i >= linha or 0 < self.coordenadaY + j >= coluna:
                            continue
                #super funcao larga item
                        if matriz[self.coordenadaX+i][self.coordenadaY+j] == self.temitem or matriz[self.coordenadaX+i][self.coordenadaY+j] == self.temitem + self.valor_formiga:      
                            cheias += 1
                #função pa largar

    def move(self, matriz, linha, coluna):
        while True:
            movimento_horizontal = random.randint(-1, 1)
            movimento_vertical = random.randint(-1, 1)
            if ((0 <= self.coordenadaX+movimento_horizontal < linha) and (0 <= self.coordenadaY+movimento_vertical < coluna)) and (movimento_vertical != 0 or movimento_horizontal != 0) and matriz[movimento_horizontal + self.coordenadaX][movimento_vertical+self.coordenadaY] < 5:                        
                # movendo do vazio pra vazio
                if matriz[self.coordenadaX][self.coordenadaY] == self.valor_formiga:
                    if matriz[self.coordenadaX+movimento_horizontal][self.coordenadaY+movimento_vertical] == 0:
                        matriz[self.coordenadaX][self.coordenadaY] = 0
                        matriz[self.coordenadaX+movimento_horizontal][self.coordenadaY+movimento_vertical] = self.valor_formiga
                        self.coordenadaX += movimento_horizontal
                        self.coordenadaY += movimento_vertical
                        #do vazio pra item
                    else:
                        matriz[self.coordenadaX][self.coordenadaY] = 0
                        matriz[self.coordenadaX+movimento_horizontal][self.coordenadaY+movimento_vertical] = self.valor_formiga + matriz[self.coordenadaX+movimento_horizontal][self.coordenadaY+movimento_vertical]
                        self.coordenadaX += movimento_horizontal
                        self.coordenadaY += movimento_vertical
                else:
                    #do item pro vazio
                    if matriz[self.coordenadaX+movimento_horizontal][self.coordenadaY+movimento_vertical] == 0:
                        matriz[self.coordenadaX][self.coordenadaY] -= self.valor_formiga
                        matriz[self.coordenadaX+movimento_horizontal][self.coordenadaY+movimento_vertical] = self.valor_formiga
                        self.coordenadaX += movimento_horizontal
                        self.coordenadaY += movimento_vertical
                    else: #item pra item
                        matriz[self.coordenadaX][self.coordenadaY] -= self.valor_formiga
                        matriz[self.coordenadaX+movimento_horizontal][self.coordenadaY+movimento_vertical] += self.valor_formiga
                        self.coordenadaX += movimento_horizontal
                        self.coordenadaY += movimento_vertical         
            break

                    

                
