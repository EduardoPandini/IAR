import math

class Dado:
    dados = []
    def __init__(self, coordenadaX, coordenadaY, valores, tipo):
        self.coordenadaX = coordenadaX
        self.coordenadaY = coordenadaY
        self.valores = valores
        self.tipo = tipo
        Dado.dados.append(self)
    
    
    
    def __str__(self):
        return f"Coordenadas: {self.coordenadaX}, {self.coordenadaY}, Valores: {self.valores[0]}, {self.valores[1]}, Não sei: {self.tipo}"
    
    def distancia_euclidiana(dado1, dado2):
        # Acessando os valores de cada dado
        x1, y1 = dado1.valores[0], dado1.valores[1]
        x2, y2 = dado2.valores[0], dado2.valores[1]

        # Calcular as diferenças entre os pares de números
        diff_x = x2 - x1
        diff_y = y2 - y1

        # Calcular a soma das diferenças ao quadrado
        soma_quadrados = diff_x**2 + diff_y**2

        # Tirar a raiz quadrada da soma das diferenças ao quadrado
        distancia = math.sqrt(soma_quadrados)
        # print(distancia)

        return distancia
    
    def semelhanca(x, y, dado, matriz_dado, raio_visao, linha, coluna, alfa):
        similaridade = 0
        vizinhos = 0
        for i in range(-raio_visao, raio_visao+1):
                    for j in range(-raio_visao, raio_visao+1):
                        if 0 <= x + i  < linha and 0 <= y + j < coluna:
                             if matriz_dado[x+i][y+j] is not None:
                                vizinhos += 1
                                subtrai = Dado.distancia_euclidiana(dado, matriz_dado[x+i][y+j])/alfa
                                similaridade += 1.0 - subtrai
                                # print(similaridade)
        if vizinhos != 0:
            fx = similaridade/vizinhos**2
            if fx < 0.0: fx = 0.0
            
        else:
            fx = 0

        # print(fx)
        return fx
                                