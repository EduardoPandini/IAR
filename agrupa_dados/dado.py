class Dado:
    dados = []
    def __init__(self, coordenadaX, coordenadaY, valor1, valor2, tipo, id):
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.valor1 = valor1
        self.valor2 = valor2
        self.tipo = tipo
        self.id = id
        Dado.dados.append(self)

    def __str__(self):
        return f"Coordenadas: {self.coordenadaX}, {self.coordenadaY}, Valores: {self.valor1}, {self.valor2}, Não sei: {self.tipo}"
