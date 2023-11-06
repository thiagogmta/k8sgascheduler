# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 10:57:55 2023
@author: Thiago Guimarães

Este algoritmo calcula a aptidão de uma alocação de Pods em nós de um cluster Kubernetes.
"""

import random

def calcular_aptidao(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos):
    somatorio_alocacao = [{'memoria': 0, 'cpu': 0} for _ in matriz_nos]
    pesos_comunicacao = [0] * len(matriz_nos)
    aptidao = 0

    for i, node in enumerate(alocacao):
        for j in range(i + 1, len(alocacao)):
            if alocacao[j] == node:
                pod1 = i
                pod2 = j
                peso = matriz_relacionamentos[pod1][pod2]
                pesos_comunicacao[node] += peso
                aptidao += peso

    for pod, node in enumerate(alocacao):
        somatorio_alocacao[node]['memoria'] += matriz_pods[pod]['memoria']
        somatorio_alocacao[node]['cpu'] += matriz_pods[pod]['cpu']

        if somatorio_alocacao[node]['cpu'] > matriz_nos[node]['cpu_no']:
            aptidao -= somatorio_alocacao[node]['cpu'] - matriz_nos[node]['cpu_no']

        if somatorio_alocacao[node]['memoria'] > matriz_nos[node]['memoria_no']:
            aptidao -= somatorio_alocacao[node]['memoria'] - matriz_nos[node]['memoria_no']

    return aptidao


numero_nos = 3
numero_pods = 10

# Matrizes de nós, pods e relacionamentos
matriz_nos = [
    {"id": 0, "cpu_no": 1000, "memoria_no": 1024},
    {"id": 1, "cpu_no": 1000, "memoria_no": 1024},
    {"id": 2, "cpu_no": 1000, "memoria_no": 1024}
]

matriz_pods = [
    {'id': 0, 'cpu': 153, 'memoria': 109},
    {'id': 1, 'cpu': 153, 'memoria': 109},
    {'id': 2, 'cpu': 153, 'memoria': 109},
    {'id': 3, 'cpu': 153, 'memoria': 109},
    {'id': 4, 'cpu': 153, 'memoria': 109},
    {'id': 5, 'cpu': 153, 'memoria': 109},
    {'id': 6, 'cpu': 153, 'memoria': 109},
    {'id': 7, 'cpu': 153, 'memoria': 109},
    {'id': 8, 'cpu': 153, 'memoria': 109},
    {'id': 9, 'cpu': 153, 'memoria': 109}
]

matriz_relacionamentos = [
    [0, 36, 0, 0, 60, 0, 0, 120, 0, 0],
    [36, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 72, 0, 0, 0, 0, 0],
    [60, 0, 0, 72, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [120, 0, 0, 0, 0, 0, 0, 0, 0, 160],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 160, 0, 0]
]

#1 - Alocação Algoritmo:
#alocacao = [0, 0, 1, 0, 0, 2, 1, 0, 1, 0]

#2 - Alocação Simulador
#alocacao = [2, 0, 1, 0, 2, 1, 2, 1, 0, 2]

#3 - Alocação do Ambiente
#alocacao = [0, 1, 2, 1, 2, 2, 0, 1, 0, 2]

alocacao = [0, 1, 2, 1, 2, 2, 0, 1, 0, 2]

aptidao = calcular_aptidao(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos)

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
#print("Matriz de Pods:")
#for pod in matriz_pods:
#    print(f"Pod {pod['id']}: Memória={pod['memoria']} CPU={pod['cpu']}")
    
print(f"Quantidade total de CPU requerida pelos PODs: {cpu_total_pod}")
print(f"Quantidade total de Memória requerida pelos PODs: {mem_total_pod}")
print("")

print("Aptidão da alocação informada:", aptidao)