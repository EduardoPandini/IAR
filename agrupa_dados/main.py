import random
import numpy as np
from formiga import *
from dado import *
import matplotlib.pyplot as plt


# parametros
raio_visao = 1
pop_formiga = 100
linha = 60
coluna = 60
valor_formiga = 5
iteracao = 2000000



matriz = np.zeros((linha, coluna), dtype=int)
matriz_dado = [[None for i in range(linha)] for i in range(coluna)]
matriz_aux = np.zeros((linha, coluna), dtype=int)
posicoes_possiveis = [(i, j) for i in range(linha) for j in range(coluna)]

# Leitura do arquivo
with open('Square1-DataSet-400itens.txt', 'r') as file:
    linhas = file.readlines()[4:]  # Ignorando as primeiras 4 linhas
meozovo = 1
for entrada in linhas:
#     # Verificar se a linha não está vazia e não começa com '#'
    if entrada.strip() and not entrada.startswith("#"):
        valores = entrada.split('\t')
        valores_aux = [float(valores[0].replace(',', '.')), float(valores[1].replace(',', '.'))]

        posicao = random.choice(posicoes_possiveis)
        posicoes_possiveis.remove(posicao)
        novo_dado = Dado(posicao[0], posicao[1], valores_aux, int(valores[2]))
        matriz_dado[posicao[0]][posicao[1]] = novo_dado
        print(novo_dado)
 


for i in range(pop_formiga):
    posicao = random.choice(posicoes_possiveis)
    posicoes_possiveis.remove(posicao)
    matriz[posicao[0]][posicao[1]] = 5
    nova_formiga = Formiga(i, posicao[0], posicao[1], 0, 5, valor_formiga, raio_visao)

    
def update_plot(matriz, i):
    plt.clf()  # Limpa o gráfico atual
    plt.imshow(matriz, cmap='gist_ncar', interpolation='nearest')
    plt.colorbar()  # Adiciona uma barra de cores para referência
    plt.title("iteração num %i" % i)
    # plt.pause(0.001)  # Pausa por um curto período para atualizar o gráfico

def somarMatrizesFim(matriz1, matriz2):
    result = []
    for i in range(len(matriz1)):   
        result.append([])
        for j in range(len(matriz1[0])):
            if matriz2[i][j] is None:
                result[i].append(matriz1[i][j])
            else:
                result[i].append(matriz2[i][j].tipo)
    return result
  
def somarMatrizes(matriz1, matriz2):
    result = []
    for i in range(len(matriz1)):   
        result.append([])
        for j in range(len(matriz1[0])):
            if matriz2[i][j] is None:
                result[i].append(matriz1[i][j])
            else:
                result[i].append(matriz1[i][j] + matriz2[i][j].tipo)
    return result
matriz_aux = somarMatrizes(matriz, matriz_dado)
update_plot(matriz_aux, 1)
plt.show()
for i in range(iteracao):
    
    for formiga in Formiga.formigas:
        formiga.mover(matriz, linha, coluna)
        formiga.pega_larga(matriz, linha, coluna, matriz_dado, raio_visao)
        
    if i % 10000 == 0:
        print(i, "still alive")
        # matriz_aux = somarMatrizesFim(matriz, matriz_dado)
        # update_plot(matriz_aux, iteracao)
        # plt.show()
matriz_aux = somarMatrizesFim(matriz, matriz_dado)
update_plot(matriz_aux, iteracao)
plt.show()