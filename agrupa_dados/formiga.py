import random
class Formiga:
    formigas = []
    def __init__(self, id, coordenadaX, coordenadaY, temitem):
        self.id = id
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.temitem = temitem
        Formiga.formigas.append(self)

    def __str__(self):
        return f"ID: {self.id}, {self.coordenadaX}, {self.coordenadaY}, {self.temitem}"

    # def move(self, matriz):
    #     while True:
    #         movimento_horizontal = random.randint(-1, 1)
    #         movimento_vertical = random.randint(-1, 1)
    #         if ((0 <= self.coordenadaX[0]+movimento_horizontal < matriz[0]) and (0 <= self.coordenadaY[1]+movimento_vertical <matriz[1])) and (movimento_vertical != 0 or movimento_horizontal != 0) and (matriz[self.coordenadaX+movimento_horizontal][self.coordenadaY+movimento_vertical] == 0 or matriz[self.coordenadaX+movimento_horizontal][self.coordenadaY+movimento_vertical] == 2):                        
    #             #movendo do vazio pra objeto
                
