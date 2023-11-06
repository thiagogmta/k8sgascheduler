import random

# Tamanho da matriz (120x120)
n = 36

# Proporção de zeros na matriz original
zero_ratio = 0.7  # Por exemplo, 70% de zeros

# Gere uma matriz com números aleatórios de 0 a 120
matriz_relacionamentos = [[random.randint(0, 120) for _ in range(n)] for _ in range(n)]

# Reduza valores maiores que 120 para 120 (mantendo a proporção de zeros)
for i in range(n):
    for j in range(i, n):
        if random.random() > zero_ratio:
            matriz_relacionamentos[i][j] = 0
            matriz_relacionamentos[j][i] = 0
        elif matriz_relacionamentos[i][j] > 120:
            matriz_relacionamentos[i][j] = 120
            matriz_relacionamentos[j][i] = 120

# Imprima a matriz resultante
for linha in matriz_relacionamentos:
    print(linha)