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
        - Quanto menor o valor melhor a aptidão para solução
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
num_geracoes = 100
prob_cruzamento = 0.9
prob_mutacao = 0.1

def gerar_matriz_nos (numero_nos):
    matriz_nos=[]
    cpuNo = int(input("Informe a quantidade de cpu dos nós: "))
    memNo = int(input("Informe a quantidade de memória dos nós: "))
    for i in range(numero_nos):
        no = {}
        no['id'] = i
        no['cpu_no'] = cpuNo
        no['memoria_no'] = memNo
        matriz_nos.append(no)
    return matriz_nos
        
def gerar_matriz_pods(numero_pods, porcentagem_relacionamentos):
    matriz_pods = []
    matriz_relacionamentos = []

    for _ in range(numero_pods):
        pod = {'memoria': random.randint(100, 200), 'cpu': random.randint(100, 200)}
        matriz_pods.append(pod)

    for i in range(numero_pods):
        linha_relacionamentos = []
        for j in range(numero_pods):
            if i == j:
                linha_relacionamentos.append(0)  # Pod não se comunica com ele mesmo
            else:
                if random.random() < porcentagem_relacionamentos:
                    peso_ligacao = random.randint(0, 10)
                else:
                    peso_ligacao = 0
                linha_relacionamentos.append(peso_ligacao)

        matriz_relacionamentos.append(linha_relacionamentos)

    return matriz_pods, matriz_relacionamentos

# Iniciando a População
def iniciar_pop(numero_pods, numero_nos, tam_populacao):
    populacao = []
    for _ in range(tam_populacao):
        alocacao = random.choices(range(numero_nos), k=numero_pods)
        populacao.append(alocacao)
    return populacao

# Calculando a Aptidão (fitness)
def calcular_aptidao(alocacao, matriz_relacionamentos):
    aptidao = 0
    for i in range(len(alocacao)):
        for j in range(i+1, len(alocacao)):
            pod1 = alocacao[i]
            pod2 = alocacao[j]
            aptidao += matriz_relacionamentos[pod1][pod2]
    return aptidao

# Seleciona os pais para realizar o cruzamento e gerar novos filhos (método roleta)
def selecionar_pais(populacao, matriz_relacionamentos):
    pais_selecionados=[]
    soma_aptidao = sum(calcular_aptidao(alocacao, matriz_relacionamentos) for alocacao in populacao)
    for _ in range (len(populacao)):
        pai = None
        valor_aleatorio = random.uniform(0, soma_aptidao)
        acumulado = 0
        for alocacao in populacao:
            acumulado += calcular_aptidao(alocacao, matriz_relacionamentos)
            if acumulado >= valor_aleatorio:
                pai = alocacao
                break
        pais_selecionados.append(pai)
    return pais_selecionados
        
# Realiza o cruzamento dos pais selecionados para que gere filhos com o gene de ambos
def realizar_cruzamento(pais_selecionados):
    filhos = []
    for i in range(0, len(pais_selecionados),2):
        pai1 = pais_selecionados[i]
        pai2 = pais_selecionados[i+1]
        ponto_corte = random.randint(1, len(pai1)-1)
        filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
        filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
        filhos.extend([filho1, filho2])
    return filhos

# Realiza a mutação para que novos filhos sejam gerados
def realizar_mutacao(filhos, prob_mutacao):
    for i in range(len(filhos)):
        if random.random() < prob_mutacao:
            indice1, indice2 = random.sample(range(len(filhos[i])), 2)
            filhos[i][indice1], filhos[i][indice2] = filhos[i][indice2], filhos[i][indice1]
"""
# Função geral que inicia o Algoritmo Genético
def algoritmo_genetico(numero_pods, numero_nos, matriz_relacionamentos, tam_populacao, prob_mutacao, num_geracoes):
    populacao = iniciar_pop(numero_pods, numero_nos, tam_populacao)
    
    for _ in range(num_geracoes):
        pais_selecionados = selecionar_pais(populacao, matriz_relacionamentos)
        filhos = realizar_cruzamento(pais_selecionados)
        realizar_mutacao(filhos, prob_mutacao)
        populacao = filhos
    
    melhor_alocacao = max(populacao, key=lambda alocacao: calcular_aptidao(alocacao, matriz_relacionamentos))
    melhor_aptidao = calcular_aptidao(melhor_alocacao, matriz_relacionamentos)
    
    return melhor_alocacao, melhor_aptidao, populacao
"""

def algoritmo_genetico(numero_pods, numero_nos, matriz_relacionamentos, tam_populacao, prob_mutacao, num_geracoes):
    populacao = iniciar_pop(numero_pods, numero_nos, tam_populacao)
    
    melhores_aptidoes = []
    
    for geracao in range(num_geracoes):
        pais_selecionados = selecionar_pais(populacao, matriz_relacionamentos)
        filhos = realizar_cruzamento(pais_selecionados)
        realizar_mutacao(filhos, prob_mutacao)
        populacao = filhos

        melhor_alocacao = max(populacao, key=lambda alocacao: calcular_aptidao(alocacao, matriz_relacionamentos))
        melhor_aptidao = calcular_aptidao(melhor_alocacao, matriz_relacionamentos)
        
        melhores_aptidoes.append(melhor_aptidao)
        
        print(f"Melhor indivíduo da geração {geracao + 1}: {melhor_alocacao}, Aptidão: {melhor_aptidao}")

    melhor_alocacao = max(populacao, key=lambda alocacao: calcular_aptidao(alocacao, matriz_relacionamentos))
    melhor_aptidao = calcular_aptidao(melhor_alocacao, matriz_relacionamentos)

    # Plotando o gráfico
    plt.plot(range(1, num_geracoes + 1), melhores_aptidoes)
    plt.xlabel('Geração')
    plt.ylabel('Melhor Aptidão')
    plt.title('Evolução das Gerações')
    plt.show()

    print("\nMelhor alocação encontrada:")
    print(f"Alocação: {melhor_alocacao}")
    print(f"Aptidão: {melhor_aptidao}")

    return melhor_alocacao, melhor_aptidao



# populacao = iniciar_pop(numero_pods, numero_nos, tam_populacao)
# melhor_aptidao = calcular_aptidao(melhor_alocacao, matriz_relacionamentos)




# Exemplo de uso do algoritmo
print('-' * 45)
print(' Alocação de recursos em um Cluster K8s')
print('-' * 45)
print("# Gerando os Nós da Infraestrutura #")
numero_nos = int(input("Digite a quantidade de nós da Infraestrutura: "))
matriz_nos = gerar_matriz_nos(numero_nos)

print('-' * 45)
print("# Gerando os Pods da Infraestrutura #")
# Gerando os Pods
numero_pods = int(input("Digite a quantidade de Pods a serem alocados: "))
porcentagem_relacionamentos = float(input("Digite a porcentagem de relacionamentos (0-100): ")) / 100


matriz_pods, matriz_relacionamentos = gerar_matriz_pods(numero_pods, porcentagem_relacionamentos)
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
    print(pod)
print(f"Quantidade total de CPU requerida pelos PODs: {cpu_total_pod}")
print(f"Quantidade total de Memória requerida pelos PODs: {mem_total_pod}")
print("")

# Exibindo a matriz de relacionamentos (apenas os valores de peso)
print("\nMatriz de Relacionamentos:")
for linha in matriz_relacionamentos:
    print(linha)
print("")

# Verificar se a infraestrutura comporta a quantidade de PODs

if (cpu_total_no>cpu_total_pod) and (mem_total_no>mem_total_pod):
    print('-' * 45)
    print("O algoritmo pode otimizar a alocação...")
    melhor_alocacao, melhor_aptidao = algoritmo_genetico(numero_pods, numero_nos, matriz_relacionamentos, tam_populacao, prob_mutacao, num_geracoes)
else:
    print('-' * 45)
    print("A alocação apropriada é infactível")




"""

plt.plot(alocacao, melhor_alocacao)
plt.title('Evolução do fitness')
plt.xlabel('Gerações')
plt.ylabel('Fitness')
plt.show()

"""







