# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 10:57:55 2023
@author: Thiago Guimarães
"""

import random
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------ Variáveis para o GA ------------------------------ #
tam_populacao = 100          # Tamaho da população do GA
num_geracoes = 100            # Numero de gerações do GA
prob_cruzamento = 0.8       # Probabilidade de cruzamento (80%)
prob_mutacao = 0.2          # Probabilidade de mutação (20%)
qt_teste = 10                # Qt de vezes que o teste será executado por padrão

# ------------------------------ Variáveis do cluster ------------------------------ #
numero_nos = 3              # Qt padrão de nós
numero_pods = 25            # Qt de PODs a serem alocados

print("# --------------- Entre com os Dados Para o GA --------------- #")
qt = input(f"Entre com a quantidade de vezes que o teste será executado (tecle enter para padrão {qt_teste}): ")
if qt !='':
    qt_teste = int(qt)

# Função para gerar matrizes de PODs e de Relacionamentos
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
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.22, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0.83, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.87, 0, 0,],
        [0, 0, 0.83, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.55, 0, 0, 0.53, 0, 0, 0, 0, 0.21, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.82, 0, 0, 0, 0, 0, 0, 0.35, 0, 0, 0, 0.89, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.45, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0.44, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.06, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.76, 0, 0, 0, 0, 0, 0.59,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.57, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.97, 0.87, 0, 0, 0, 0, 0, 0.35, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0.82, 0, 0, 0, 0, 0, 0.87, 0, 0, 0.36, 0, 0, 0, 0.99, 0.99, 0, 0, 0, 0, 0, 0.09,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.57, 0, 0, 0.47, 0, 0, 0, 0, 0, 0, 0, 0, 0.22, 0, 0, 0,],
        [0, 0, 0, 0.55, 0, 0, 0, 0, 0, 0, 0, 0.36, 0, 0, 0, 0.44, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0.22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.44, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0.53, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.94, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.35, 0.99, 0, 0, 0, 0, 0.94, 0, 0, 0, 0, 0, 0, 0, 0.14,],
        [0, 0, 0, 0, 0.35, 0.45, 0, 0, 0.76, 0, 0, 0.99, 0, 0, 0, 0, 0, 0, 0, 0.66, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.66, 0, 0, 0, 0, 0.04, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0.21, 0, 0, 0, 0, 0, 0, 0, 0, 0.22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3,],
        [0, 0, 0.87, 0, 0.89, 0, 0, 0.06, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.04, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0, 0, 0, 0.59, 0, 0, 0.09, 0, 0, 0, 0, 0, 0.14, 0, 0, 0, 0.3, 0, 0, 0]
    ]
    return matriz_nos, matriz_pods, matriz_relacionamentos

matriz_nos, matriz_pods, matriz_relacionamentos = gerar_matrizes()

# Iniciando a População
def iniciar_pop(numero_pods, numero_nos, tam_populacao):
    populacao = []
    for _ in range(tam_populacao):
        alocacao = random.choices(range(numero_nos), k=numero_pods)
        populacao.append(alocacao)
    return populacao

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

def algoritmo_genetico(numero_pods, numero_nos, matriz_relacionamentos, tam_populacao, prob_mutacao, num_geracoes, teste):
    populacao = iniciar_pop(numero_pods, numero_nos, tam_populacao)
    
    melhor_alocacao = None
    melhor_aptidao = float('-inf')  # Inicializando com o menor valor possível
    
    melhores_aptidoes = []
    melhores_alocacoes = []
    todas_aptidoes = []
    
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
        melhores_alocacoes.append(melhor_alocacao)
        todas_aptidoes.append([calcular_aptidao(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos) for alocacao in populacao])

    print('-' * 45)
    print(f"Alocação: {melhor_alocacao}")
    print(f"Aptidão: {melhor_aptidao}")
    
    # Imprimindo a alocação dos pods nos nós
    for pod, node in enumerate(melhor_alocacao):
        print(f"O POD {pod} está alocado no Nó '{node}'")
        
    # Calculando o consumo de recursos utilizados nos nós
    somatorio_alocacao = [{'memoria': 0, 'cpu': 0} for _ in range(len(matriz_nos))]
    
    for pod, node in enumerate(melhor_alocacao):
        somatorio_alocacao[node]['memoria'] += matriz_pods[pod]['mem_pod']
        somatorio_alocacao[node]['cpu'] += matriz_pods[pod]['cpu_pod']
    
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
        
    return melhor_alocacao, melhor_aptidao, melhores_aptidoes

matriz_nos, matriz_pods, matriz_relacionamentos = gerar_matrizes()
print("")

resultados_aptidoes =[]
melhor_aptidao_global = float('-inf')
melhor_alocacao_global = None

for teste in range(qt_teste):
    mem_total_no = 0
    cpu_total_no = 0
    mem_total_pod = 0
    cpu_total_pod = 0
    for pod in matriz_pods:
        mem_total_pod += pod['mem_pod']
        cpu_total_pod += pod['cpu_pod']
    
    for no in matriz_nos:
        mem_total_no += no['mem_no']
        cpu_total_no += no['cpu_no']
    
    if (cpu_total_no>=cpu_total_pod) and (mem_total_no>=mem_total_pod):
        print('-' * 45)
        print(f"Melhor alocação encontrada no teste: {teste}")
        
        melhor_alocacao, melhor_aptidao, melhores_aptidoes = algoritmo_genetico(numero_pods, numero_nos, matriz_relacionamentos, tam_populacao, prob_mutacao, num_geracoes, teste)
        
        resultados_aptidoes.append(melhores_aptidoes)
        
        if melhor_aptidao > melhor_aptidao_global:
            melhor_aptidao_global = melhor_aptidao
            alocacao_global = melhor_alocacao
    else:
        print('-' * 45)
        print("A alocação apropriada é infactível")


# --------------- Melhor Aptidão Global --------------- #
# Identificando o teste que resultou na melhor aptidão global
print('-' * 45)
print("Melhor Alocação Global")
print(f"Melhor Aptidão Global: {melhor_aptidao_global}")
print(f"Melhor Alocação Global: {alocacao_global}")


# --------------- Imprimindo Gráficos --------------- #
# função para calcular a média e o desvio padrão ao longo do eixo 0, que representa as várias execuções do algoritmo.
media_aptidoes = np.mean(resultados_aptidoes, axis=0)
minimo_aptidoes = np.min(resultados_aptidoes, axis=0)
desvio_padrao_aptidoes = np.std(resultados_aptidoes, axis=0)

geracoes = range(1, num_geracoes + 1)

media_global_aptidoes = np.mean(media_aptidoes)
mediana_global_aptidoes = np.median(resultados_aptidoes)
minimo_global_aptidoes = np.min(resultados_aptidoes)
desvio_global_aptidoes = np.std(resultados_aptidoes)

print("Média Global das Aptidões:", media_global_aptidoes)
print("Mediana Global das Aptidões:", mediana_global_aptidoes)
print("Mínimo Global das Aptidões:", minimo_global_aptidoes)
print("Desvio Padrão Global das Aptidões:", desvio_global_aptidoes)
print("Melhor Aptidão Global:", melhor_aptidao_global)


# Plota todos os testes
for i, evolucao in enumerate(resultados_aptidoes):
    plt.plot(geracoes, evolucao, color='blue', alpha=0.3)

# plt.errorbar(geracoes, media_aptidoes, yerr=desvio_padrao_aptidoes, uplims=True, lolims=True, linewidth = 1, color='red', label='Média das aptidões')

plt.plot(geracoes, media_aptidoes, linewidth = 1, color='red', label='Média das aptidões')
plt.axhline(y=melhor_aptidao_global, color='green', linestyle='--', alpha=0.5, label='Melhor Aptidão Global')

plt.xlabel('Geração')
plt.ylabel('Aptidão')
plt.title('Evolução da Aptidão ao longo das Gerações')
plt.legend()
plt.show()