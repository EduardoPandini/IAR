import math

x1, y1 = -19.2730055, -18.23689836
x2, y2 =  -20.10683994,	-20.7140554

# Calcular as diferenças entre os pares de números
diff_x = x2 - x1
diff_y = y2 - y1

# Calcular a soma das diferenças ao quadrado
soma_quadrados = diff_x**2 + diff_y**2

# Tirar a raiz quadrada da soma das diferenças ao quadrado
distancia = math.sqrt(soma_quadrados)
# print(distancia)
print(distancia)