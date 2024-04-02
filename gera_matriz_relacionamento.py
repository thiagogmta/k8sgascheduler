import random
numero_pods = 20            # Qt de PODs a serem alocados
taxa_rel = 10               # Porcentagem de preenchimento da matriz de relacionamentos
def gerar_matriz(numero_pods, taxa_rel):

    # Criar matriz_relacionamentos
    matriz_relacionamentos = [
        [round(random.uniform(0, 1), 2) if random.uniform(0, 100) < taxa_rel else 0 for _ in range(numero_pods)]
        for _ in range(numero_pods)
    ]

    # Tornar a matriz_relacionamentos simétrica
    for i in range(numero_pods):
        for j in range(i + 1, numero_pods):
            matriz_relacionamentos[i][j] = matriz_relacionamentos[j][i]
    return matriz_relacionamentos

matriz_relacionamentos = gerar_matriz(numero_pods, taxa_rel)

# Imprimir a matriz linha por linha
for linha in matriz_relacionamentos:
    print(linha)