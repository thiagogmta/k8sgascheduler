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

tam_populacao = 100
num_geracoes = 50
prob_cruzamento = 0.9
prob_mutacao = 0.2

numero_nos = 3
numero_pods = 10

def gerar_matriz_nos():
    matriz_nos=[
        {"id": 0, "cpu_no": 1000, "memoria_no": 1024},
        {"id": 1, "cpu_no": 1001, "memoria_no": 1024},
        {"id": 2, "cpu_no": 1002, "memoria_no": 1024}
    ]
    return matriz_nos
        
def gerar_matriz_pods():
    matriz_pods = [
        {"id": 0, "cpu": 192, "memoria": 137},
        {"id": 1, "cpu": 174, "memoria": 177},
        {"id": 2, "cpu": 138, "memoria": 133},
        {"id": 3, "cpu": 139, "memoria": 106},
        {"id": 4, "cpu": 105, "memoria": 166},
        {"id": 5, "cpu": 155, "memoria": 102},
        {"id": 6, "cpu": 198, "memoria": 111},
        {"id": 7, "cpu": 143, "memoria": 181},
        {"id": 8, "cpu": 191, "memoria": 168},
        {"id": 9, "cpu": 132, "memoria": 116}
    ]
    
    matriz_relacionamentos = [
        [0, 3, 0, 0, 5, 0, 6, 10, 0, 6],
        [3, 0, 9, 5, 0, 0, 0, 2, 0, 0],
        [0, 9, 0, 0, 7, 0, 10, 0, 0, 0],
        [0, 5, 0, 0, 6, 10, 0, 0, 4, 5],
        [5, 0, 7, 6, 0, 0, 5, 1, 0, 0],
        [0, 0, 0, 10, 0, 0, 1, 0, 0, 10],
        [6, 0, 10, 0, 5, 1, 0, 5, 0, 10],
        [10, 2, 0, 0, 1, 0, 5, 0, 2, 5],
        [0, 0, 0, 4, 0, 0, 0, 2, 0, 4],
        [6, 0, 0, 5, 0, 10, 10, 5, 4, 0]
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

    print('-' * 45)
    print(alocacao)
    for indice, valor in enumerate(alocacao):
        print(f"O POD {indice} está no Nó '{valor}'")

    for pod, node in enumerate(alocacao):
        somatorio_alocacao[node]['memoria'] += matriz_pods[pod]['memoria']
        somatorio_alocacao[node]['cpu'] += matriz_pods[pod]['cpu']

    for i, somatorio in enumerate(somatorio_alocacao):
        print(f"Recursos utilizados Nó {i}: Memória = {somatorio['memoria']} CPU = {somatorio['cpu']}")


    for i, node in enumerate(alocacao):
        for j in range(i + 1, len(alocacao)):
            if alocacao[j] == node:
                pod1 = i
                pod2 = j
                peso = matriz_relacionamentos[pod1][pod2]

    for i, node in enumerate(somatorio):
        pesos_comunicacao[i] = sum(node.values())

    for i, peso in enumerate(pesos_comunicacao):
        print(f"O somatório do peso do relacionamento dos pods do nó {i} é {peso}")
        
    return aptidao


"""
def calcular_aptidao(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos):
    somatorio_alocacao = [{'memoria': 0, 'cpu': 0} for _ in range(len(matriz_nos))]
    aptidao = 0
    
    print('-' * 45)
    print(alocacao)
    for indice, valor in enumerate(alocacao):
        print(f"O POD {indice} está no Nó '{valor}'")
        
    for no in matriz_nos:
        print(f"Nó {no['id']}: Memória = {no['memoria_no']} CPU = {no['cpu_no']}")
    
    for pod, node in enumerate(alocacao):
        somatorio_alocacao[node]['memoria'] += matriz_pods[pod]['memoria']
        somatorio_alocacao[node]['cpu'] += matriz_pods[pod]['cpu']
        
    
    for i, somatorio in enumerate(somatorio_alocacao):
        print(f"Recursos utilizados Nó {i}: Memória={somatorio['memoria']} CPU={somatorio['cpu']}")
        
        
    pesos_comunicacao = [0] * len(matriz_nos)
    
    for i in range(len(alocacao)):
        for j in range(i + 1, len(alocacao)):
            pod1 = alocacao[i]
            pod2 = alocacao[j]
            pesos_comunicacao[pod1] += matriz_relacionamentos[pod1][pod2]
            pesos_comunicacao[pod2] += matriz_relacionamentos[pod1][pod2]
    
    for i, somatorio in enumerate(somatorio_alocacao):
        print(f"Peso da comunicação entre os pods do nó {i}: {pesos_comunicacao[i]}")
        

    for i in range(len(alocacao)):
        for j in range(i + 1, len(alocacao)):
            pod1 = alocacao[i]
            pod2 = alocacao[j]
            aptidao += matriz_relacionamentos[pod1][pod2]
            
        for k, no in enumerate(matriz_nos):
            
            #print(f"Nó {no['id']}: Memória={no['memoria_no']} CPU={no['cpu_no']}")
            
            cpu_usada = sum(matriz_pods[pod]['cpu'] for pod, node in enumerate(alocacao) if node == k)
            memoria_usada = sum(matriz_pods[pod]['memoria'] for pod, node in enumerate(alocacao) if node == k)
            
            #print(f"Foi usado cpu: {cpu_usada}")
            
            if cpu_usada > no['cpu_no']:
                aptidao -= cpu_usada - no['cpu_no']
            #else:
                #aptidao += no['cpu_no'] - cpu_usada  # Adiciona quantidade não utilizada de CPU à aptidão
            
            if memoria_usada > no['cpu_no']:
                aptidao -= memoria_usada - no['memoria_no']
            #else:
                #aptidao += no['memoria_no'] - memoria_usada  # Adiciona quantidade não utilizada de memória à aptidão
       
    return aptidao
"""
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
def realizar_mutacao(filhos, prob_mutacao):
    for i in range(len(filhos)):
        if random.random() < prob_mutacao:
            indice1, indice2 = random.sample(range(len(filhos[i])), 2)
            filhos[i][indice1], filhos[i][indice2] = filhos[i][indice2], filhos[i][indice1]

def algoritmo_genetico(numero_pods, numero_nos, matriz_relacionamentos, tam_populacao, prob_mutacao, num_geracoes):
    populacao = iniciar_pop(numero_pods, numero_nos, tam_populacao)
    
    melhores_aptidoes = []
    
    for geracao in range(num_geracoes):
        pais_selecionados = selecionar_pais(populacao, matriz_relacionamentos)
        filhos = realizar_cruzamento(pais_selecionados, prob_cruzamento)
        realizar_mutacao(filhos, prob_mutacao)
        populacao = filhos

        melhor_alocacao = max(populacao, key=lambda alocacao: calcular_aptidao(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos))
        melhor_aptidao = calcular_aptidao(melhor_alocacao, matriz_nos, matriz_pods, matriz_relacionamentos)
        
        melhores_aptidoes.append(melhor_aptidao)
        
        print(f"Melhor indivíduo da geração {geracao + 1}: {melhor_alocacao}, Aptidão: {melhor_aptidao}")

            
    melhor_alocacao = max(populacao, key=lambda alocacao: calcular_aptidao(alocacao, matriz_nos, matriz_pods, matriz_relacionamentos))
    melhor_aptidao = calcular_aptidao(melhor_alocacao, matriz_nos, matriz_pods, matriz_relacionamentos)

    # Plotando o gráfico 1 - Gráfico da evolução do Algoritmo Genético
    plt.plot(range(1, num_geracoes + 1), melhores_aptidoes)
    plt.xlabel('Geração')
    plt.ylabel('Melhor Aptidão')
    plt.title('Evolução das Gerações')
    plt.show()
    
    # Plotando o gráfico 2 - Gráfico da alocação da melhor aptidão
    
    print("\nMelhor alocação encontrada:")
    print(f"Alocação: {melhor_alocacao}")
    print(f"Aptidão: {melhor_aptidao}")
    
    

    return melhor_alocacao, melhor_aptidao

# Exemplo de uso do algoritmo
print('-' * 45)
print(' Alocação de recursos em um Cluster K8s')
print('-' * 45)
print("# Gerando os Nós da Infraestrutura #")
# Gerando Matriz dos Nós
matriz_nos = gerar_matriz_nos()

print('-' * 45)
print("# Gerando os Pods da Infraestrutura #")

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
