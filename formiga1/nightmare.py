 # for id in range(pop_formiga):
    #     for i in range(linha):
    #         for j in range(coluna):
    #             if matriz[i][j][0] == id:
    #                 movimento_horizontal = 0
    #                 movimento_vertical = 0
    #                 while True:
    #                     movimento_horizontal = random.randint(-1, 1)
    #                     movimento_vertical = random.randint(-1, 1)
    #                     if ((0 <= i+movimento_horizontal < linha) and (0 <= j+movimento_vertical <coluna)) and (movimento_vertical != 0 or movimento_horizontal != 0) and (matriz[i+movimento_horizontal][j+movimento_vertical][1]== 0 or matriz[i+movimento_horizontal][j+movimento_vertical][1]== 2):
    #                         #caso seja uma formiga andando de um 
    #                         #vazio
    #                         if matriz[i][j][1] == 1:
    #                             #para um objeto
    #                             if matriz[i+movimento_horizontal][j+movimento_vertical][1] == 2:
    #                                 matriz[i][j][0] = -1
    #                                 matriz[i][j][1] = 0
    #                                 matriz[i+movimento_horizontal][j+movimento_vertical][1] = 3
    #                                 matriz[i+movimento_horizontal][j+movimento_vertical][0] = id
    #                                 #esse ta ok
    #                             #para um vazio
    #                             else:
    #                                 matriz[i][j][0] = -1
    #                                 matriz[i][j][1] = 0
    #                                 matriz[i+movimento_horizontal][j+movimento_vertical][1] = 1
    #                                 matriz[i+movimento_horizontal][j+movimento_vertical][0] = id
    #                                 #esse ta ok
    #                         #com objeto
    #                         else:
    #                             #para um com objeto
    #                             if matriz[i+movimento_horizontal][j+movimento_vertical][1] == 2:
    #                                 matriz[i][j][0] = -1
    #                                 matriz[i][j][1] = 2
    #                                 matriz[i+movimento_horizontal][j+movimento_vertical][1] = 3
    #                                 matriz[i+movimento_horizontal][j+movimento_vertical][0] = id
    #                             #para um sem objeto
    #                             else:
    #                                 matriz[i][j][0] = -1
    #                                 matriz[i][j][1] = 2
    #                                 matriz[i+movimento_horizontal][j+movimento_vertical][1] = 1
    #                                 matriz[i+movimento_horizontal][j+movimento_vertical][0] = id
    #                         break

# def pega_ou_larga(matriz, linha, coluna):
#     for id in range(pop_formiga):
#        if 
