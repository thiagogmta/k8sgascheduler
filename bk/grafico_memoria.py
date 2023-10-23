import numpy as np
import matplotlib.pyplot as plt

# Dados dos pods
pod_memoria = [137, 177, 133, 106]
pod_cpu = [192, 174, 138, 139]

# Dados do nó
no_memoria = 1024
no_cpu = 1000

# Cálculo da CPU disponível no nó
cpu_disponivel_no = no_cpu - sum(pod_cpu)

# Cálculo da memória disponível no nó
memoria_disponivel_no = no_memoria - sum(pod_memoria)

# Cálculo da porcentagem de utilização dos recursos
porcentagem_cpu_utilizada = (sum(pod_cpu) / no_cpu) * 100
porcentagem_cpu_disponivel = (cpu_disponivel_no / no_cpu) * 100
porcentagem_memoria_utilizada = (sum(pod_memoria) / no_memoria) * 100
porcentagem_memoria_disponivel = (memoria_disponivel_no / no_memoria) * 100

# Criar gráfico de barras
fig, ax = plt.subplots(figsize=(8, 6))

# Somatório da CPU Utilizada pelos PODs
ax.bar(0, sum(pod_cpu), color='darkblue')
ax.text(0, sum(pod_cpu), f'{porcentagem_cpu_utilizada:.2f}%', ha='center', va='bottom')

# CPU Disponível no Nó
ax.bar(0, cpu_disponivel_no, bottom=sum(pod_cpu), color='lightblue')
ax.text(0, sum(pod_cpu) + cpu_disponivel_no, f'{porcentagem_cpu_disponivel:.2f}%', ha='center', va='bottom')

# Somatório da Memória Utilizada pelos PODs
ax.bar(1, sum(pod_memoria), color='darkgreen')
ax.text(1, sum(pod_memoria), f'{porcentagem_memoria_utilizada:.2f}%', ha='center', va='bottom')

# Memória Disponível no Nó
ax.bar(1, memoria_disponivel_no, bottom=sum(pod_memoria), color='lightgreen')
ax.text(1, sum(pod_memoria) + memoria_disponivel_no, f'{porcentagem_memoria_disponivel:.2f}%', ha='center', va='bottom')

ax.set_ylabel('Recursos')
ax.set_title('Alocação de Recursos')
ax.set_xticks([0, 1])
ax.set_xticklabels(['CPU', 'Memória'])

# Posicionando a legenda
ax.legend(bbox_to_anchor=(1, 1), loc='upper left')

plt.tight_layout()
plt.show()
