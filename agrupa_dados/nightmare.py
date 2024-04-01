import random
import numpy as np
from formiga import *

import matplotlib.pyplot as plt

# Parâmetros
linha = 20
coluna = 20
raio_visao = 1
pop_formiga = 15
linha = 20
coluna = 20

matriz = np.zeros((linha, coluna), dtype=int)
posicoes_possiveis = [(i, j) for i in range(linha) for j in range(coluna)]

# Leitura do arquivo
with open('Square1-DataSet-400itens.txt', 'r') as file:
    linhas = file.readlines()[4:]  # Ignorando as primeiras 4 linhas

# Processamento dos dados
for linha in linhas:
    # Verificar se a linha não está vazia e não começa com '#'
    if linha.strip() and not linha.startswith("#"):
        valores = linha.split('\t')
        coordenadas = [float(valor.replace(',', '.')) for valor in valores[:2]]
        numero = int(valores[2])

        # Colocar o valor na matriz em uma posição aleatória
        posicao = random.randint(0, linha * coluna - 1)
        posicao_x = posicao // coluna
        posicao_y = posicao % coluna
        matriz[posicao_x][posicao_y] = numero

# Adicionar formigas
for i in range(pop_formiga):
    # Escolher uma posição aleatória que não tenha sido ocupada ainda
    posicao = random.choice(posicoes_possiveis)
    posicoes_possiveis.remove(posicao)
    matriz[posicao[0]][posicao[1]] = 1
    nova_formiga = Formiga(i, posicao[0], posicao[1], 0)

# Exibir as formigas
for formiga in Formiga.formigas:
    print(formiga)

print(matriz)
