import random
import numpy as np
from formiga import *
from dado import *
import matplotlib.pyplot as plt


# parametros
linha = 20
coluna = 20
raio_visao = 1
pop_formiga = 15
linha = 50
coluna = 50


matriz = np.zeros((linha, coluna), dtype=int)
posicoes_possiveis = [(i, j) for i in range(linha) for j in range(coluna)]

# Leitura do arquivo
with open('Square1-DataSet-400itens.txt', 'r') as file:
    linhas = file.readlines()[4:]  # Ignorando as primeiras 4 linhas
#  def __init__(self, id, coordenadaX, coordenadaY, valor1, valor2, tipo):
# Processamento dos dados
for linha in linhas:
    # Verificar se a linha não está vazia e não começa com '#'
    if linha.strip() and not linha.startswith("#"):
        valores = linha.split('\t')

        posicao = random.choice(posicoes_possiveis)
        matriz[posicao[0]][posicao[1]] = valores[2]
        novo_dado = Dado(posicao[0], posicao[1], valores[0], valores[1], int(valores[2]))
        print(novo_dado)


for i in range(pop_formiga):
    posicao = random.choice(posicoes_possiveis)
    posicoes_possiveis.remove(posicao)
    matriz[posicao[0]][posicao[1]] = 5
    nova_formiga = Formiga(i, posicao[0], posicao[1], 0)

# for dado in Dado.dados:
#     print(dado)

# print(matriz)
    
def update_plot(matriz, i):
    plt.clf()  # Limpa o gráfico atual
    plt.imshow(matriz, cmap='cividis', interpolation='nearest')
    plt.colorbar()  # Adiciona uma barra de cores para referência
    plt.title("iteração num %i" % i)
    plt.pause(0.001)  # Pausa por um curto período para atualizar o gráfico
    plt.show()

update_plot(matriz, 1)