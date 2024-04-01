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
