# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 10:57:55 2023

@author: Thiago Guimarães

Fluxo do algoritmo genético:
    
    1 - Definição da representação dos cromossomos
        - Cada cromossomo representa uma solução candidata que é a alocação de PODs em Nós (Gene: 1 sim; 0 não)
    2 - Iníciar a população
        - Cada cromossomo é uma "pessoa" que carrega uma possível solução.
    3 - Avaliação da aptidão (fitness)
        - A aptidão calcula o quão boa é aquela alocação com base no peso do relacionamento entre os PODs
    4 - Seleção dos pais
        - Seleciona os cromossomos pais (roleta)
    5 - Cruzamento (crossover)
        - Realizar o cruzamento entre os pais selecionados para gerar novos cromossomos (filhos)
    6 - Mutação
        - Aplica a mutação (troca aleatória de gene). Permitindo que o algoritmo continue buscando novas soluções.
    7 - Avaliação da aptidão dos filhos
        - Calcula a aptidão de solução de cada filho gerado
    8 - Seleção dos sobreviventes
        - Exclui parte da população gerada e seleciona os cromossomos sobreviventes para gerar uma nova população
    9 - Repete os passos de 4 a 8
        - Cada vez que o algoritmo se repetir será uma nova geração criada
    10 - Retorna com a melhor solução encontrada
"""

import random
import matplotlib.pyplot as plt

tam_populacao = 50
num_geracoes = 100
prob_cruzamento = 0.9
prob_mutacao = 0.2

numero_nos = 3
numero_pods = 24

def gerar_matriz_nos():
    matriz_nos=[
        {"id": 0, "cpu_no": 1001, "memoria_no": 1024},
        {"id": 1, "cpu_no": 1002, "memoria_no": 1024},
        {"id": 2, "cpu_no": 1003, "memoria_no": 1024}
    ]
    return matriz_nos
        
def gerar_matriz_pods():
    matriz_pods = [
        {'id': 0, 'cpu': 153, 'memoria': 109},
        {'id': 1, 'cpu': 139, 'memoria': 141},
        {'id': 2, 'cpu': 110, 'memoria': 106},
        {'id': 3, 'cpu': 111, 'memoria': 84},
        {'id': 4, 'cpu': 84, 'memoria': 132},
        {'id': 5, 'cpu': 124, 'memoria': 81},
        {'id': 6, 'cpu': 158, 'memoria': 88},
        {'id': 7, 'cpu': 114, 'memoria': 144},
        {'id': 8, 'cpu': 152, 'memoria': 134},
        {'id': 9, 'cpu': 105, 'memoria': 92},
        {'id': 10, 'cpu': 110, 'memoria': 106},
        {'id': 11, 'cpu': 111, 'memoria': 84},
        {'id': 12, 'cpu': 84, 'memoria': 132},
        {'id': 13, 'cpu': 124, 'memoria': 81},
        {'id': 14, 'cpu': 158, 'memoria': 88},
        {'id': 15, 'cpu': 114, 'memoria': 144},
        {'id': 16, 'cpu': 152, 'memoria': 134},
        {'id': 18, 'cpu': 105, 'memoria': 92},
        {'id': 19, 'cpu': 153, 'memoria': 109},
        {'id': 20, 'cpu': 139, 'memoria': 141},
        {'id': 21, 'cpu': 110, 'memoria': 106},
        {'id': 22, 'cpu': 111, 'memoria': 84},
        {'id': 23, 'cpu': 84, 'memoria': 132},
        {'id': 24, 'cpu': 124, 'memoria': 81}
    ]
    
    matriz_relacionamentos = [
        [112, 62, 93, 0, 25, 49, 0, 100, 97, 0, 69, 75, 38, 0, 54, 108, 0, 0, 113, 59, 120, 67, 84, 33, 117, 0, 0, 0, 8, 21, 5, 0, 60, 33, 70, 6],
        [32, 0, 56, 50, 3, 0, 30, 73, 34, 3, 64, 30, 1, 12, 0, 0, 94, 0, 11, 69, 0, 93, 64, 3, 13, 94, 87, 119, 21, 22, 108, 37, 0, 119, 119, 0],
        [41, 119, 0, 0, 46, 75, 103, 0, 0, 56, 103, 59, 81, 0, 101, 66, 24, 0, 83, 61, 56, 0, 0, 0, 93, 0, 83, 59, 20, 3, 104, 0, 3, 85, 0, 104],
        [0, 2, 0, 54, 0, 73, 0, 85, 0, 0, 85, 78, 0, 108, 93, 0, 26, 1, 22, 34, 62, 18, 29, 89, 0, 23, 69, 0, 20, 73, 77, 0, 0, 0, 46, 38],
        [91, 77, 4, 0, 43, 80, 0, 0, 82, 53, 24, 59, 21, 0, 32, 83, 27, 0, 74, 96, 2, 63, 90, 27, 11, 67, 0, 19, 3, 27, 0, 0, 35, 0, 44, 80],
        [88, 0, 69, 70, 76, 40, 118, 78, 0, 56, 100, 86, 77, 38, 0, 82, 0, 0, 104, 60, 90, 20, 111, 62, 105, 0, 92, 97, 37, 56, 0, 74, 0, 5, 0, 39],
        [0, 52, 41, 0, 0, 18, 0, 28, 9, 80, 18, 52, 75, 0, 89, 0, 19, 19, 92, 31, 54, 42, 63, 28, 27, 37, 113, 0, 0, 56, 0, 85, 39, 57, 73, 106],
        [107, 72, 0, 18, 0, 104, 25, 77, 0, 0, 0, 119, 19, 35, 28, 58, 39, 32, 10, 20, 115, 0, 0, 46, 95, 46, 72, 109, 42, 36, 55, 26, 87, 0, 119, 72],
        [68, 76, 0, 0, 69, 0, 94, 0, 97, 2, 103, 0, 48, 0, 48, 0, 41, 51, 88, 110, 107, 40, 8, 0, 52, 0, 89, 79, 78, 106, 86, 72, 0, 83, 80, 90],
        [0, 14, 86, 0, 69, 106, 31, 0, 41, 30, 95, 26, 0, 54, 42, 0, 119, 0, 99, 0, 28, 108, 24, 116, 116, 51, 0, 95, 63, 113, 55, 73, 82, 0, 110, 74],
        [58, 118, 92, 115, 120, 108, 74, 0, 3, 57, 0, 109, 0, 63, 37, 0, 0, 117, 0, 0, 0, 41, 0, 52, 87, 51, 106, 6, 0, 0, 29, 47, 79, 93, 70, 27],
        [90, 82, 60, 5, 26, 9, 59, 21, 0, 111, 32, 0, 0, 43, 105, 0, 84, 0, 0, 7, 35, 23, 3, 51, 0, 0, 16, 6, 0, 19, 81, 0, 68, 78, 10, 0],
        [78, 10, 108, 0, 100, 82, 10, 49, 11, 0, 0, 0, 0, 0, 35, 0, 87, 62, 62, 81, 91, 11, 0, 87, 9, 25, 39, 0, 0, 91, 0, 0, 6, 7, 0, 35],
        [0, 15, 0, 70, 0, 39, 0, 25, 59, 53, 38, 74, 0, 42, 0, 0, 93, 61, 96, 0, 105, 109, 14, 0, 92, 88, 0, 35, 0, 0, 99, 75, 73, 83, 0, 0],
        [20, 0, 74, 98, 0, 0, 65, 12, 4, 96, 75, 35, 83, 0, 26, 0, 74, 82, 0, 4, 59, 63, 63, 77, 0, 107, 69, 12, 100, 5, 18, 0, 2, 0, 8, 39],
        [41, 0, 47, 0, 100, 5, 0, 65, 0, 0, 0, 0, 0, 0, 0, 72, 84, 84, 13, 67, 104, 33, 89, 33, 5, 91, 0, 59, 100, 15, 54, 23, 99, 117, 0, 31],
        [0, 37, 29, 14, 48, 0, 20, 41, 72, 33, 0, 114, 81, 120, 16, 88, 0, 22, 75, 4, 50, 36, 0, 19, 8, 120, 0, 0, 120, 70, 0, 57, 25, 24, 19, 93],
        [0, 0, 0, 61, 0, 0, 89, 107, 8, 0, 29, 0, 64, 67, 37, 93, 47, 38, 26, 8, 0, 31, 0, 106, 0, 37, 34, 91, 62, 4, 28, 34, 59, 26, 0, 20],
        [73, 25, 83, 60, 25, 67, 82, 6, 64, 32, 0, 0, 58, 68, 0, 114, 31, 29, 25, 39, 83, 93, 0, 0, 49, 0, 82, 13, 15, 95, 75, 0, 77, 0, 21, 17],
        [33, 38, 21, 49, 79, 98, 36, 52, 25, 0, 0, 80, 117, 0, 18, 101, 62, 48, 38, 18, 82, 0, 21, 53, 0, 117, 5, 24, 0, 70, 9, 96, 87, 112, 93, 109],
        [22, 0, 33, 64, 74, 14, 84, 23, 68, 2, 0, 68, 30, 19, 93, 103, 2, 8, 90, 87, 0, 115, 24, 0, 106, 107, 110, 107, 117, 10, 0, 87, 41, 84, 0, 83],
        [118, 113, 0, 81, 77, 39, 68, 0, 59, 99, 17, 100, 73, 47, 109, 79, 77, 35, 26, 0, 96, 0, 48, 91, 103, 0, 74, 101, 43, 0, 114, 0, 89, 41, 0, 36],
        [74, 63, 0, 50, 38, 28, 9, 0, 103, 39, 0, 97, 0, 75, 39, 48, 0, 0, 0, 70, 90, 71, 0, 88, 0, 0, 0, 0, 29, 0, 91, 109, 15, 76, 33, 0],
        [86, 106, 0, 119, 113, 80, 103, 100, 0, 3, 116, 86, 61, 0, 68, 69, 44, 43, 0, 64, 0, 120, 23, 0, 46, 64, 108, 17, 0, 97, 81, 28, 30, 0, 101, 0]
    ]

    return matriz_pods, matriz_relacionamentos

# Iniciando a População
def iniciar_pop(numero_pods, numero_nos, tam_populacao):
    populacao = []
    for _ in range(tam_populacao):
        alocacao = random.choices(range(numero_nos), k=numero_pods)
        populacao.append(alocacao)
    return populacao

# Versao 04 considerando memória e cpu
def calcular_aptidao(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos):
    somatorio_alocacao = [{'memoria': 0, 'cpu': 0} for _ in range(len(matriz_nos))]
    pesos_comunicacao = [0] * len(matriz_nos)
    aptidao = 0

    # --------------- Imprimindo a matriz de alocação dos pods nos nós
    #print('-' * 45)
    #print(alocacao)
    #for indice, valor in enumerate(alocacao):
    #    print(f"O POD {indice} está no Nó '{valor}'")

    # --------------- Calculando o peso do relacionamento entre os pods
    for i, node in enumerate(alocacao):
            for j in range(i + 1, len(alocacao)):
                if alocacao[j] == node:
                    pod1 = i
                    pod2 = j
                    peso = matriz_relacionamentos[pod1][pod2]
                    pesos_comunicacao[node] += peso
                    aptidao += peso
                    
    # --------------- Calculando o consumo de recursos dos pods nos Nós  
    for pod, node in enumerate(alocacao):
        somatorio_alocacao[node]['memoria'] += matriz_pods[pod]['memoria']
        somatorio_alocacao[node]['cpu'] += matriz_pods[pod]['cpu']
        
        if somatorio_alocacao[node]['cpu'] > no['cpu_no']:
            aptidao -= somatorio_alocacao[node]['cpu'] - no['cpu_no']
        
        if somatorio_alocacao[node]['memoria'] > no['memoria_no']:
            aptidao -= somatorio_alocacao[node]['memoria'] - no['memoria_no']


    # --------------- Imprimindo o resultado do consumo de recursos
    #for i, somatorio in enumerate(somatorio_alocacao):
    #    print(f"Recursos utilizados Nó {i}: Memória = {somatorio['memoria']} CPU = {somatorio['cpu']}")
    
    # --------------- Imprimindo o resultado do peso do relacionamento
    #for i, peso in enumerate(pesos_comunicacao):
    #    print(f"O somatório do peso do relacionamento dos pods do nó {i} é {peso}")
        
    return aptidao

# Seleciona os pais para realizar o cruzamento e gerar novos filhos (método roleta)
def selecionar_pais(populacao, matriz_relacionamentos):
    pais_selecionados=[]
    soma_aptidao = sum(calcular_aptidao(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos) for alocacao in populacao)
    for _ in range (len(populacao)):
        pai = None
        valor_aleatorio = random.uniform(0, soma_aptidao)
        acumulado = 0
        for alocacao in populacao:
            acumulado += calcular_aptidao(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos)
            if acumulado >= valor_aleatorio:
                pai = alocacao
                break
        pais_selecionados.append(pai)
    return pais_selecionados
        
# Realiza o cruzamento dos pais selecionados para que gere filhos com o gene de ambos
def realizar_cruzamento(pais_selecionados, prob_cruzamento):
    filhos = []
    for i in range(0, len(pais_selecionados), 2):
        pai1 = pais_selecionados[i]
        pai2 = pais_selecionados[i + 1]

        if pai1 is None:
            pai1 = random.choices(range(numero_nos), k=numero_pods)
        if pai2 is None:
            pai2 = random.choices(range(numero_nos), k=numero_pods)

        if random.random() < prob_cruzamento:
            ponto_corte = random.randint(1, len(pai1) - 1)
            filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
            filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
            filhos.append(filho1)
            filhos.append(filho2)
        else:
            filhos.append(pai1)
            filhos.append(pai2)
    return filhos

# Realiza a mutação para que novos filhos sejam gerados
def realizar_mutacao(filhos, prob_mutacao, numero_nos):
    for i in range(len(filhos)):
        if random.random() < prob_mutacao:
            for j in range(len(filhos[i])):
                if random.random() < prob_mutacao:
                    filhos[i][j] = random.randint(0, numero_nos - 1)

def algoritmo_genetico(numero_pods, numero_nos, matriz_relacionamentos, tam_populacao, prob_mutacao, num_geracoes):
    populacao = iniciar_pop(numero_pods, numero_nos, tam_populacao)
    
    melhor_alocacao = None
    melhor_aptidao = float('-inf')  # Inicializando com o menor valor possível
    
    melhores_aptidoes = []
    #historico_aptidoes = []
    
    for geracao in range(num_geracoes):
        pais_selecionados = selecionar_pais(populacao, matriz_relacionamentos)
        filhos = realizar_cruzamento(pais_selecionados, prob_cruzamento)
        realizar_mutacao(filhos, prob_mutacao, numero_nos)
        populacao = filhos
        
        for alocacao in populacao:
            aptidao = calcular_aptidao(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos)
            if aptidao > melhor_aptidao:
                melhor_alocacao = alocacao
                melhor_aptidao = aptidao
                
        melhores_aptidoes.append(melhor_aptidao)
        #historico_aptidoes.extend([aptidao for alocacao in populacao])
        print(f"Melhor indivíduo da geração {geracao + 1}: {melhor_alocacao}, Aptidão: {melhor_aptidao}")

    print('-' * 45)
    print("Melhor alocação encontrada:")
    print(f"Alocação: {melhor_alocacao}")
    print(f"Aptidão: {melhor_aptidao}")
    
    # Imprimindo a alocação dos pods nos nós
    for pod, node in enumerate(melhor_alocacao):
        print(f"O POD {pod} está alocado no Nó '{node}'")
        
    # Calculando o consumo de recursos utilizados nos nós
    somatorio_alocacao = [{'memoria': 0, 'cpu': 0} for _ in range(len(matriz_nos))]
    
    for pod, node in enumerate(melhor_alocacao):
        somatorio_alocacao[node]['memoria'] += matriz_pods[pod]['memoria']
        somatorio_alocacao[node]['cpu'] += matriz_pods[pod]['cpu']
    
    # Imprimindo o consumo de recursos utilizados nos nós
    for i, somatorio in enumerate(somatorio_alocacao):
        print(f"Recursos utilizados Nó {i}: Memória = {somatorio['memoria']} CPU = {somatorio['cpu']}")
    
    # Calculando o somatório do peso do relacionamento dos pods nos nós
    pesos_comunicacao = [0] * len(matriz_nos)
    for i, node in enumerate(melhor_alocacao):
        for j in range(i + 1, len(melhor_alocacao)):
            if melhor_alocacao[j] == node:
                pod1 = i
                pod2 = j
                peso = matriz_relacionamentos[pod1][pod2]
                pesos_comunicacao[node] += peso
    
    # Imprimindo o somatório do peso do relacionamento dos pods nos nós
    for i, peso in enumerate(pesos_comunicacao):
        print(f"O somatório do peso do relacionamento dos pods do nó {i} é {peso}")

    # Plotando o gráfico 1 - Gráfico da evolução do Algoritmo Genético
    plt.plot(range(1, num_geracoes + 1), melhores_aptidoes)
    plt.xlabel('Geração')
    plt.ylabel('Melhor Aptidão')
    plt.title('Evolução das Gerações')
    plt.show() 

    # Plotando o gráfico 2 - Gráfico do consumo de recursos
    
    return melhor_alocacao, melhor_aptidao

# Exemplo de uso do algoritmo
print('-' * 45)
print(' Alocação de recursos em um Cluster')
print('-' * 45)
#print("# Gerando os Nós da Infraestrutura #")
# Gerando Matriz dos Nós
matriz_nos = gerar_matriz_nos()

#print('-' * 45)
#print("# Gerando os Pods da Infraestrutura #")

# Gerando Matriz dos Pods
matriz_pods, matriz_relacionamentos = gerar_matriz_pods()
print("")

# Realiza o somatório da quantidade total de Memória e CPU dos Nós
# Realiza o somatório da quantidade total de Memória e CPU requisitados pelos PODs
mem_total_no = 0
cpu_total_no = 0
mem_total_pod = 0
cpu_total_pod = 0
for pod in matriz_pods:
    mem_total_pod += pod['memoria']
    cpu_total_pod += pod['cpu']

for no in matriz_nos:
    mem_total_no += no['memoria_no']
    cpu_total_no += no['cpu_no']
    
# Exibindo a matriz dos Nos
print("Matriz dos Nos:")
for no in matriz_nos:
    print(f"Nó {no['id']}: Memória={no['memoria_no']} CPU={no['cpu_no']}")

print(f"Quantidade total de CPU dos Nós: {cpu_total_no}")
print(f"Quantidade total de Memória dos Nós: {mem_total_no}")
print("")

# Exibindo a matriz de pods
print("Matriz de Pods:")
for pod in matriz_pods:
    print(f"Pod {pod['id']}: Memória={pod['memoria']} CPU={pod['cpu']}")
    
print(f"Quantidade total de CPU requerida pelos PODs: {cpu_total_pod}")
print(f"Quantidade total de Memória requerida pelos PODs: {mem_total_pod}")
print("")

# Exibindo a matriz de relacionamentos (apenas os valores de peso)
print("\nMatriz de Relacionamentos:")
for linha in matriz_relacionamentos:
    print(linha)
print("")

# Verificar se a infraestrutura comporta a quantidade de PODs

if (cpu_total_no>=cpu_total_pod) and (mem_total_no>=mem_total_pod):
    print('-' * 45)
    print("O algoritmo pode otimizar a alocação...")
    melhor_alocacao, melhor_aptidao = algoritmo_genetico(numero_pods, numero_nos, matriz_relacionamentos, tam_populacao, prob_mutacao, num_geracoes)

else:
    print('-' * 45)
    print("A alocação apropriada é infactível")
