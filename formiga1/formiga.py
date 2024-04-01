import random
import numpy as np

import matplotlib.pyplot as plt
# parametros
linha = 20
coluna = 20
pop_formiga = 15
pop_objeto = 100
raio_visao = 1
dicionario_formiga = {}
f1 = 0.1 #pegar
f2 = 0.6 #largar


def move_formiga():
    for formiga in dicionario_formiga:
        posicao = dicionario_formiga[formiga]
        while True:
            movimento_horizontal = random.randint(-1, 1)
            movimento_vertical = random.randint(-1, 1)
            #do vazio
            if ((0 <= posicao[0]+movimento_horizontal < linha) and (0 <= posicao[1]+movimento_vertical <coluna)) and (movimento_vertical != 0 or movimento_horizontal != 0) and (matriz[posicao[0]+movimento_horizontal][posicao[1]+movimento_vertical] == 0 or matriz[posicao[0]+movimento_horizontal][posicao[1]+movimento_vertical] == 2):                        
                if matriz[posicao[0]][posicao[1]] == 1:
                #para um objeto
                    if matriz[posicao[0]+movimento_horizontal][posicao[1]+movimento_vertical] == 2:
                        matriz[posicao[0]][posicao[1]] = 0
                        matriz[posicao[0]+movimento_horizontal][posicao[1]+movimento_vertical] = 3
                        dicionario_formiga[formiga] = (posicao[0]+movimento_horizontal, posicao[1]+movimento_vertical,posicao[2])
                #sem objeto
                    else:
                        matriz[posicao[0]][posicao[1]] = 0
                        matriz[posicao[0]+movimento_horizontal][posicao[1]+movimento_vertical] = 1
                        dicionario_formiga[formiga] = (posicao[0]+movimento_horizontal, posicao[1]+movimento_vertical,posicao[2])
            #de um objeto
                else:
                #para um objeto
                    if matriz[posicao[0]+movimento_horizontal][posicao[1]+movimento_vertical] == 2:
                        matriz[posicao[0]][posicao[1]] = 2
                        matriz[posicao[0]+movimento_horizontal][posicao[1]+movimento_vertical] = 3
                        dicionario_formiga[formiga] = (posicao[0]+movimento_horizontal, posicao[1]+movimento_vertical,posicao[2])
                #pro vazio
                    else:
                        matriz[posicao[0]][posicao[1]] = 2
                        matriz[posicao[0]+movimento_horizontal][posicao[1]+movimento_vertical] = 1
                        dicionario_formiga[formiga] = (posicao[0]+movimento_horizontal, posicao[1]+movimento_vertical,posicao[2])
                break


#func de pega ou larga duh
def pega_ou_larga():
    
    for formiga in dicionario_formiga:
        cheias = 0
        posicao = list(dicionario_formiga[formiga])
        #condições sem item
        if posicao[2] == 0:
            if matriz[posicao[0], posicao[1]] == 1:
                continue
            else: 
                for i in range(-raio_visao,raio_visao+1):
                    for j in range(-raio_visao,raio_visao+1):
                        if 0 < posicao[0] + i >= linha or 0 < posicao[1] + j >= coluna:
                            continue
                        if matriz[posicao[0]+i][posicao[1]+j] == 2:
                            cheias += 1
                f = cheias/8
                pegar = (f1/(f1+f))**2
                randomm = random.random()
                if (pegar) >= randomm and pegar >= 0.06:
                    # print("pegar", pegar)
                    posicao[2] = 1
                    dicionario_formiga[formiga] = posicao
                    matriz[posicao[0]][posicao[1]] = 1
        #quando ela tem item
        else:
            if matriz[posicao[0], posicao[1]] == 1:
                for i in range(-raio_visao,raio_visao+1):
                    for j in range(-raio_visao,raio_visao+1):
                        if 0 < posicao[0] + i >= linha or 0 < posicao[1] + j >= coluna:
                            continue
                        if matriz[posicao[0]+i][posicao[1]+j] == 2:
                            cheias += 1
                f = cheias/8
                largar = (f/f2+f)**2
                randomm = random.random() 
                if (largar) >= randomm and largar >= 0.05:
                    # print("largar",largar)
                    posicao[2] = 0
                    dicionario_formiga[formiga] = posicao
                    matriz[posicao[0]][posicao[1]] = 3
            else:
                continue
                    

def sumindo():
    acucar = 0
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j] == 2 or matriz[i][j] == 3:
                acucar += 1
    if acucar + pop_formiga < pop_objeto:
        
            print("as VAGABUNDA TÃO COMENDO SAPORRA DE ZUCAR")

def update_plot(matriz, i):
    plt.clf()  # Limpa o gráfico atual
    plt.imshow(matriz, cmap='cividis', interpolation='nearest')
    plt.colorbar()  # Adiciona uma barra de cores para referência
    plt.title("iteração num %i" % i)
    plt.pause(0.001)  # Pausa por um curto período para atualizar o gráfico


# Criando a matriz e posições possíveis
matriz = np.zeros((linha, coluna), dtype=int)
posicoes_possiveis = [(i, j) for i in range(linha) for j in range(coluna)]

# Preenchendo a matriz com formigas
for i in range(pop_formiga):
    posicao = random.choice(posicoes_possiveis)
    posicoes_possiveis.remove(posicao)
    matriz[posicao[0]][posicao[1]] = 1
    dicionario_formiga[i] = (posicao[0],posicao[1], 0)

# Preenchendo a matriz com objetos
for i in range(pop_objeto):
    posicao = random.choice(posicoes_possiveis)
    posicoes_possiveis.remove(posicao)
    matriz[posicao[0]][posicao[1]] = 2

# plt.imshow(matriz, cmap='cividis', interpolation='nearest')
# plt.title("inicio")
# plt.show()
for i in range(20000):
    # update_plot(matriz, i)
    # if i== 5000:
    #     plt.imshow(matriz, cmap='cividis', interpolation='nearest')
    #     plt.title("%i" % i)
    #     plt.show()

        
        # time.sleep(0.1)
    sumindo()
    move_formiga()  # Movendo as formigas
    pega_ou_larga()

plt.imshow(matriz, cmap='cividis', interpolation='nearest')
plt.title("Fim")
plt.show()


