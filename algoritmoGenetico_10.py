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
numero_pods = 10

def gerar_matriz_nos():
    matriz_nos=[
        {"id": 0, "cpu_no": 1000, "memoria_no": 1024},
        {"id": 1, "cpu_no": 1000, "memoria_no": 1024},
        {"id": 2, "cpu_no": 1000, "memoria_no": 1024}
    ]
    return matriz_nos
        
def gerar_matriz_pods():
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
        
        # Penalização pelo consumo excedente de cpu + bonificação pela alocação apropriada
        # Falta inserir o qt de nos
        if somatorio_alocacao[node]['cpu'] > matriz_nos[node]['cpu_no']:
            aptidao -= somatorio_alocacao[node]['cpu'] - matriz_nos[node]['cpu_no']
        else:
            aptidao += somatorio_alocacao[node]['cpu']

        # Penalização pelo consumo excedente de cpu + bonificação pela alocação apropriada
         # Falta inserir o qt de nos
        if somatorio_alocacao[node]['memoria'] > matriz_nos[node]['memoria_no']:
            aptidao -= somatorio_alocacao[node]['memoria'] - matriz_nos[node]['memoria_no']
        else:
            aptidao += somatorio_alocacao[node]['memoria']

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
