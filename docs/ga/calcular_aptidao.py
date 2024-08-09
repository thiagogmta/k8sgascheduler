# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 10:57:55 2023
@author: Thiago Guimarães
"""

import random
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------ Variáveis para o GA ------------------------------ #
tam_populacao = 100         # Tamaho da população do GA
num_geracoes = 100          # Numero de gerações do GA
prob_cruzamento = 0.8       # Probabilidade de cruzamento (80%)
prob_mutacao = 0.2          # Probabilidade de mutação (20%)
qt_teste = 5                # Qt de vezes que o teste será executado por padrão

# ------------------------------ Variáveis do cluster ------------------------------ #
numero_nos = 3              # Qt padrão de nós
numero_pods = 25            # Qt de PODs a serem alocados

# -------------------------------- Vetor de Alocação ------------------------------- #
alocacao = [0,1,1,1,0,2,0,2,2,1,1,2,0,0,1,0,0,2,2,2]

def gerar_matrizes():
    # Criar matriz_nos
    matriz_nos = [
        {'id': 0, 'cpu_no': 2000, 'mem_no': 2048},
        {'id': 1, 'cpu_no': 2000, 'mem_no': 2048},
        {'id': 2, 'cpu_no': 2000, 'mem_no': 2048}

    ]
    # Criar matriz_pod
    matriz_pods = [
        {'id': 0, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 1, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 2, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 3, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 4, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 5, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 6, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 7, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 8, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 9, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 10, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 11, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 12, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 13, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 14, 'cpu_pod': 50, 'mem_pod': 64},
        {'id': 15, 'cpu_pod': 100, 'mem_pod': 128},
        {'id': 16, 'cpu_pod': 100, 'mem_pod': 128},
        {'id': 17, 'cpu_pod': 100, 'mem_pod': 128},
        {'id': 18, 'cpu_pod': 100, 'mem_pod': 128},
        {'id': 19, 'cpu_pod': 100, 'mem_pod': 128},
        {'id': 20, 'cpu_pod': 100, 'mem_pod': 128},
        {'id': 21, 'cpu_pod': 100, 'mem_pod': 128},
        {'id': 22, 'cpu_pod': 100, 'mem_pod': 128},
        {'id': 23, 'cpu_pod': 100, 'mem_pod': 128},
        {'id': 24, 'cpu_pod': 100, 'mem_pod': 128}
    ]

    # Criar matriz_relacionamentos
    matriz_relacionamentos = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.22, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0.83, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.87, 0, 0, ],
        [0, 0, 0.83, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.55, 0, 0, 0.53, 0, 0, 0, 0, 0.21, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.82, 0, 0, 0, 0, 0, 0, 0.35, 0, 0, 0, 0.89, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.45, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0.44, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.06, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.76, 0, 0, 0, 0, 0, 0.59, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.97, 0.87, 0, 0, 0, 0, 0, 0.35, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0.82, 0, 0, 0, 0, 0, 0.87, 0, 0, 0.36, 0, 0, 0, 0.99, 0.99, 0, 0, 0, 0, 0, 0.09, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.57, 0, 0, 0.47, 0, 0, 0, 0, 0, 0, 0, 0, 0.22, 0, 0, 0, ],
        [0, 0, 0, 0.55, 0, 0, 0, 0, 0, 0, 0, 0.36, 0, 0, 0, 0.44, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0.22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.44, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0.53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.94, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.35, 0.99, 0, 0, 0, 0, 0.94, 0, 0, 0, 0, 0, 0, 0, 0.14, ],
        [0, 0, 0, 0, 0.35, 0.45, 0, 0, 0.76, 0, 0, 0.99, 0, 0, 0, 0, 0, 0, 0, 0.66, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.66, 0, 0, 0, 0, 0.04, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0.21, 0, 0, 0, 0, 0, 0, 0, 0, 0.22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, ],
        [0, 0, 0.87, 0, 0.89, 0, 0, 0.06, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.04, 0, 0, 0, 0, 0, ],
        [0, 0, 0, 0, 0, 0, 0, 0, 0.59, 0, 0, 0.09, 0, 0, 0, 0, 0, 0.14, 0, 0, 0, 0.3, 0, 0, 0]
    ]
    return matriz_nos, matriz_pods, matriz_relacionamentos

matriz_nos, matriz_pods, matriz_relacionamentos = gerar_matrizes()
# --------------- B(x) Função de Alocação
# Descrição:
# Retorna a quantidade de Nós utilizados em cada alocação
# A função set cria um conjunto de itens únicos e a função len conta esses itens
# B(x) = a quantidade de nós utilizados para alocar os pods.
def func_alocacao(alocacao):
    nos_utilizados = set(alocacao)
    num_nos_utilizados = len(nos_utilizados)
    return num_nos_utilizados

# --------------- S(x) - Função de Consumo
# Descrição:
# Calcula o percentual de consumo de CPU e Memória dos PODs nos Nós
# S(x) = capacidade total do Nó (em memória ou cpu) dividido pelo somatório da
# quantidade de recursos (em memória ou cpu) demandados pelos PODs a serem alocados
# naquele Nó.
# 1. Itera sobre cada Nó da matriz de nós
# 2. Itera sobre o vetor de alocação verificando se cada pod está alocado no Nó da iteração anterior.
# 3. Caso o POD esteja alocado realiza o somatório da quantidade de memória e cpu demandada
# 4. Retorna o somatório 
def func_consumo(alocacao, matriz_nos, matriz_pods, peso):
    soma_porc_mem = 0
    soma_porc_cpu = 0

    # Itera sobre cada nó utilizado na alocação
    for node in range(len(matriz_nos)):
        # Inicializar somatórios para cada nó
        somatorio_mem = 0
        somatorio_cpu = 0

        # Itera sobre cada POD alocado e verificar se pertence ao nó atual
        # enumerate() retorna uma tupla onde a variável 'POD' armazena o índice
        # que representa o POD e a variavel 'alocado_no' armazena o conteúdo
        # que representa o Nó.
        for pod, alocado_no in enumerate(alocacao):
            if alocado_no == node:
                # Soma a quantidade de memória e CPU consumida pelo POD no nó atual
                somatorio_mem += matriz_pods[pod]['mem_pod']
                somatorio_cpu += matriz_pods[pod]['cpu_pod']

        # Calcula a porcentagem de utilização de memória e CPU para o nó atual
        media_mem = somatorio_mem / matriz_nos[node]['mem_no']
        media_cpu = somatorio_cpu / matriz_nos[node]['cpu_no']

        # Soma as porcentagens calculadas aos somatórios gerais
        soma_porc_mem += media_mem ** peso
        soma_porc_cpu += media_cpu ** peso

    return soma_porc_mem, soma_porc_cpu

# --------------- I(x) - Função de Infactibilidade
# Descrição:
# Calcula a infactibilidade na alocação (se a alocação é viável ou não)
# É uma medida do quão próximo o Nó está de ficar sem recursos.
# I(x) = -1 ou 0 
# -1 -> se i(x) > 1 a alocação não é viável (pois excede a capacidade do nó 0.99%)
# 0 -> Caso Contrário
# 1. Itera sobre cada Nó da matriz de nós
# 2. Itera sobre o vetor de alocação verificando se cada pod está alocado no Nó da iteração anterior.
# 3. Caso o POD esteja alocado realiza o somatório da quantidade de memória e cpu demandada
# 4. Calcula a proporção de utilização do Nó (em memória e cpu)
#   a. Retorna 0 se a alocação for factivel
#   b. Retorna -1 se a alocação for infactível
# 5. Retorna o somatório da infactibilidade da alocação
def func_infactibilidade(alocacao, matriz_nos, matriz_pods):
    somatorio_inf_mem = 0
    somatorio_inf_cpu = 0
    
    # Itera sobre cada nó utilizado na alocação
    for node in range(len(matriz_nos)):
        infactibilidade_mem = 0
        infactibilidade_cpu = 0
        somatorio_mem = 0
        somatorio_cpu = 0

        # Itera sobre cada POD alocado e verificar se pertence ao nó atual
        for pod, alocado_no in enumerate(alocacao):
            
            if alocado_no == node:
                somatorio_mem += matriz_pods[pod]['mem_pod']
                somatorio_cpu += matriz_pods[pod]['cpu_pod']

        if (somatorio_mem / matriz_nos[node]['mem_no']) <= 1:
            infactibilidade_mem += 0
        else:
            infactibilidade_mem += (somatorio_mem / matriz_nos[node]['mem_no'])
            
        if (somatorio_cpu / matriz_nos[node]['cpu_no']) <= 1:
            infactibilidade_cpu += 0
        else:
            infactibilidade_cpu += (somatorio_cpu / matriz_nos[node]['cpu_no'])

        # Acumular infactibilidade total para o nó
        somatorio_inf_mem += infactibilidade_mem
        somatorio_inf_cpu += infactibilidade_cpu
        
    # Retornar a infactibilidade total
    return somatorio_inf_mem, somatorio_inf_cpu

# --------------- T(x) - Calcula a taxa de relacionamento dentre os PODs
def taxa_relacionamento(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos):
    pesos_comunicacao = [0] * len(matriz_nos)
    for i, node in enumerate(alocacao):
            for j in range(i + 1, len(alocacao)):
                if alocacao[j] == node:
                    pod1 = i
                    pod2 = j
                    peso = matriz_relacionamentos[pod1][pod2]
                    pesos_comunicacao[node] += peso
    soma_pesos = sum(pesos_comunicacao)
    return soma_pesos

# --------------- F(x) Função de Aptidão
# Descrição:
# Avalia cada alocação e retorna sua aptidão.
# f(x) = O somatório da porcentagem de ocupação da memória de todos os nós dividido 
# pela quantidade de nós utilizados na alocação somado ao somatório da porcentagem 
# de ocupação da cpu de todos os nós dividido pela quantidade de nós utilizados 
# na alocação somado a taxa de relacionamento entre os nós subtraido a infactibilidade 
# de alocação de memória subtraido a infactibilidade de alocação de cpu.
def calcular_aptidao(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos):
    
    somatorio_mem, somatorio_cpu = func_consumo(alocacao, matriz_nos, matriz_pods, 2)
    num_nos = func_alocacao(alocacao)
    somatorio_inf_mem, somatorio_inf_cpu = func_infactibilidade(alocacao, matriz_nos, matriz_pods)
    taxa_rel = taxa_relacionamento(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos)
    
    aptidao = (somatorio_mem / num_nos + somatorio_cpu / num_nos) - (somatorio_inf_mem + somatorio_inf_cpu) + taxa_rel

    return aptidao

print("Alocação informada:", alocacao)
aptidao = calcular_aptidao(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos)
print("Aptidão da alocação:", aptidao)