# k8sgaScheduler
**Algoritmo para alocação inteligente de recursos em cluster kubernetes**

> Artefato proposto no artigo intitulado: K8sGAScheduler: Algoritmo para alocação inteligente de recursos em cluster kubernetes apresentado no WGRS – Workshop de Gerência e Operação de Redes e Serviços - 2024.

## Introdução

O Kubernetes é uma plataforma de código aberto amplamente utilizada para gerenciar cargas de trabalho e serviços em contêineres. No entanto, a otimização da alocação de pods é uma questão complexa que requer soluções avançadas. Este projeto apresenta o K8sGAScheduler, um algoritmo inteligente desenvolvido para otimizar a alocação de recursos em clusters Kubernetes. Nossa abordagem leva em conta o consumo de recursos, a comunicação entre os pods e as restrições de capacidade dos nós.

O problema consiste em classificar diferentes alocações para determinar a solução mais eficiente. A solução ideal maximiza a utilização dos recursos em cada nó individualmente e agrupa os pods que mantêm comunicação frequente em um mesmo nó. Foi proposta uma modelagem matemática para representar o problema e, para sua resolução, utilizou-se uma abordagem baseada em um algoritmo genético implementado em Python.

É importante mencionar que este código é uma avaliação do modelo matemático proposto para o K8sGAScheduler e, nesta fase, não é executável diretamente no Kubernetes. A finalidade deste projeto é validar a formulação matemática e o algoritmo de avaliação de alocação.

## Dependências

Para rodar este repositório localmente, é necessário suprir as seguintes dependências:

- Python 3.8+: Linguagem de programação principal utilizada no projeto.
- Bibliotecas Python:
  - numpy: Para operações matemáticas e manipulação de arrays.
  - matplotlib: Para visualização de dados e geração de gráficos.
- Para nossos testes, usaremos o PyCharm como IDE, mas sua utilização é opcional, pode-se executar diretamente no terminal.

## Teste experimental

Nesta sessão será apresentado um script demo para testes básicos de funcionalidade. Para testes personalizados favor consultar a sessão de Documentação.

O teste experimental consiste em uma alocação de 25 pods sendo 15 pods com requisitos de CPU 50m e Mem 64Mi e 10 pods com requisitos de CPU 100m e Mem 128Mi. Para simular a comunicação entre pods a matriz de relacionamentos é preenchida onde 10% de seus espaços são preenchidos com valores aleatórios entre 0 e 1. Nesse exemplo quanto mais próximo de 1 o valor maior a comunicação entre os pods.

- Clone este repositório e execute o arquivo k8sgascheduler_demo.py (via pycharm ou terminal)
1. Via PyCharm: abra o arquivo demo deste repositório na IDE e execute (shift+f10).
2. Via terminal: acesse o diretório do repositório e execute:

```shel
python k8sgascheduler_demo.py
```

### Retorno do Algoritmo

```shell
Melhor Aptidão Global: 14.872363281249998
Melhor Alocação Global: [2, 0, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2]
Média Global das Aptidões: 12.739945624999997
Mediana Global das Aptidões: 12.961888020833333
Mínimo Global das Aptidões: 8.031731770833334
Desvio Padrão Global das Aptidões: 1.4051678021004357
```

![Resultado](img/demo.png)

### Fluxo de funcionamento:

1. **Inicia três matrizes:**
  - Matriz de nós:
    - Essa matriz representa os nós do cluster
    - Possui os campos: id, cpu_no, mem_no
  - Matriz de pods:
    - Essa matriz representa os pods a serem alocados
    - Possui os campos: id, cpu_pod, mem_pod
  - Matriz simétrica de relacionamentos
    - Essa matriz representa a taxa de relacionamento entre os pods
2. **Implementa o fluxo do algoritmo genético**
  - Inicialização da População
    - População com 100 individuos onde cada cromossomo carrega uma possível solução
  - Avaliação da Aptidão (Fitness)
    - Calcula o quão boa é a alocação com base no modelo matemático
  - Seleção dos Pais
    - Seleciona os cromossomos pais utilizando o método da roleta
  - Cruzamento
    - Realiza o cruzamento entre os pais selecionados para gerar novos cromossomos (filhos)
  - Mutação
    - Aplica a mutação (troca aleatória de gene) para permitir a busca de novas soluções
  - Avaliação da Aptidão dos filhos
    - Calcula a aptidão de solução de cada filho gerado
  - Seleção dos Sobreviventes
    - Exclui parte da população gerada e seleciona os cromossomos sobreviventes para gerar uma nova população
  - Repetição dos passos 4 a 8
    - Cada iteração do algoritmo corresponde a uma nova geração criada. O algoritmo está configurado para 100 gerações.
  - Retorna com a Melhor Solução Encontrada
    - O algoritmo retorna a melhor alocação de PODs em Nós encontrada durante as gerações
3. **Reexecução**
  - O algoritmo implementa o passo 2 por 5 vezes (por padrão)
  - Ao final das 5 execuções irá retornar: Melhor aptidão global, melhor alocação, média, mediana, mínimo e desvio padrão e um gráfico expressando a evolução das aptidões.

## Documentação

Para mais informações sobre o projeto e testes mais elaborados acesse: [Wiki - k8sGaScheduler](docs/documentacao.md)