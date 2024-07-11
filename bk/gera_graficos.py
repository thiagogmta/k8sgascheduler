# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:44:28 2024

@author: thiagogmta
"""

import matplotlib.pyplot as plt

# Nomes dos nós
nodos = ['Nó 1', 'Nó 2', 'Nó 3']

# Recursos totais disponíveis em cada nó (100%)
recursos_totais = [100, 100, 100]

# Porcentagem de recursos consumidos em cada nó (50%)
consumo_recursos = [110, 40, 0]

# Plot

plt.bar(nodos, recursos_totais, color='lightblue', label='Recursos Totais')
plt.bar(nodos, [min(consumo_recursos[i], recursos_totais[i]) for i in range(len(nodos))], color='tomato', label='Recursos Consumidos')
plt.bar(nodos, [max(consumo_recursos[i] - recursos_totais[i], 0) for i in range(len(nodos))], color='darkred', label='Excedente de Recursos', bottom=[min(consumo_recursos[i], recursos_totais[i]) for i in range(len(nodos))])

# Adicionando linha pontilhada para os recursos totais
for i in range(len(nodos)):
    plt.axhline(y=recursos_totais[i], color='lightblue', linestyle='--')

# Adicionando rótulos
plt.ylabel('Porcentagem de Recursos')
plt.title('Consumo de Recursos nos Nós do Cluster')
plt.legend()

# Encontrando o índice do nó com maior consumo
indice_max = consumo_recursos.index(max(consumo_recursos))

# Adicionando linha pontilhada
plt.axhline(y=consumo_recursos[indice_max], color='red', linestyle='--', label='Maior Consumo')

# Adicionando números sobre as barras
for i in range(len(nodos)):
    plt.text(i, consumo_recursos[i] + 1, str(consumo_recursos[i]) + "%", ha='center', va='bottom')
    
# Exibindo o gráfico
plt.show()
