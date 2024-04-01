# k8sgaScheduler

## Genetic Algorithm for 5g K8s Scheduler

Este repositório armazena o protótipo de um algoritmo genético para fomentar o aprimoramento do scheduler padrão do Kubernetes. O objetivo é encontrar a melhor alocação possível de pods, visando maximizar a eficiência do cluster.

Os Algoritmos Genéticos são uma técnica de otimização inspirada na teoria da evolução biológica. São amplamente utilizados para resolver problemas complexos de otimização, incluindo a alocação eficiente de recursos, e podem ser aplicados à solução deste problema.

Para representar o problema por meio do Algoritmo Genético, a lógica de implementação foi formulada da seguinte maneira: Um cromossomo [0,1,0,2] representa a alocação de 4 pods em 3 nós, e eles estão alocados da seguinte forma: o pod 0 está alocado no nó 0, o pod 1 está alocado no nó 1, o pod 2 está alocado no nó 0 e o pod 3 está alocado no nó 2.

Para o ambiente, foram criadas três matrizes. A primeira é a Matriz de nós, que representa os nós que receberão as alocações de pods. Esta matriz possui os campos: id, cpu e memória para cada nó. A segunda é a Matriz de pods, que representa os pods a serem alocados. Esta matriz também possui os campos: id, CPU e memória para cada pod. A terceira é uma matriz simétrica de relacionamentos que representa a taxa de envio e recebimento de informações entre os pods. Essa representação abstrai que dado um valor na matriz simboliza o peso da quantidade de troca de informações entre os pods.

> **Nota**: O projeto em fase de andamento porém funcional para testes iniciais

## Cenários de teste:

Foram formulados 3 cenários de testes para avaliação do modelo:

- Baixa capacidade - 20 pods
  - 20 pods com cpu de 50 milicores e memória de 64B.
- Capacidade aleatória
  - 15 pods com cpu de 50 milicores e memória de 64MB.
  - 10 pods com CPU de 100 milicores e memória de 128MB.
- Alta capacidade
    - 20 pods com CPU de 50 milicores e memória de 64MB.
    - 10 pods com CPU de 100 milicores e memória de 128MB.

## Arquivos do repositório:

Na raiz do repositório estão os três algoritmos que retornam as melhores alocações em três cenários diferentes:

- k8sgascheduler_a.py
  - Arquivo referente ao texte de baixa capacidade
- k8sgascheduler_b.py
  - Arquivo referente ao texte de capacidade aleatória
- k8sgascheduler_c.py
  - Arquivo referente ao texte de alta capacidade

No diretório \calcular encontram-se três arquivos que calculam a apitidão de uma alocação específica inserida pelo usuário.

- Diretório \calcular
  - aptidao_a.py
    - Calcula aptidão para uma alocação do cenário de Baixa capacidade
  - aptidao_b.py
    - Calcula aptidão para uma alocação do cenário de Capacidade aleatória
  - aptidao_c.py
    - Calcula aptidão para uma alocação do cenário de Alta capacidade
  
> **Nota**: Para informar uma alocação específica e receber sua aptidão altere o valor da variável 'alocação'. Exemplo: alocacao = [0,1,1,1,0,2,0,2,2,1,1,2,0,0,1,0,0,2,2,2]

## Como utilizar:

Clone este repositório e execute:

```bash
cd k8sgascheduler
python k8sgascheduler_a.py
```
Ao executar o algoritmo serão solicitadas as informações:
- Quantidade de vezes que o teste será executado (tecle enter para padrão 10):
- Quantidade de Nós do cluster (tecle enter para padrão 3):
- Quantidade de PODs do cluster (tecle enter para padrão 20):

O Fluxo do algoritmo ocorre da seguinte maneira:

Serão criadas três matrizes:
- Matriz dos Nós 
    - Contem informações dos Nós do Cluster
    ```python
    matriz_nos = [
        {"id": 0, "cpu_no": 2000, "memoria_no": 2048},
        {"id": 1, "cpu_no": 2000, "memoria_no": 2048},
        {"id": 2, "cpu_no": 2000, "memoria_no": 2048}
    ]
    ```
- Matriz dos PODs
    - Contem informações sobre os PODs a serem alocados
    ```python
    matriz_pods = [
        {"id": 0, "cpu": 50, "memoria": 64},
        {"id": 1, "cpu": 50, "memoria": 64},
        {"id": 2, "cpu": 50, "memoria": 64},
        {"id": 3, "cpu": 50, "memoria": 64},
        {"id": 4, "cpu": 50, "memoria": 64},
        {"id": 5, "cpu": 50, "memoria": 64},
        {"id": 6, "cpu": 50, "memoria": 64},
        {"id": 7, "cpu": 50, "memoria": 64},
        {"id": 8, "cpu": 50, "memoria": 64},
        {"id": 9, "cpu": 50, "memoria": 64}
    ]
    ```
- Matriz de Relacionamentos
    - A matriz de relacionamentos é uma matriz simétrica
    - Contem o peso do relacionamento entre os pods
    ```python
    matriz_relacionamentos = [
        [0.13, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.97, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0.71, 0, 0, 0, 0, 0, 0.53, 0.23, 0, 0, 0, 0, 0, 0.54],
        [0, 0, 0.16, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.83, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.24, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0.66, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0.71, 0, 0, 0, 0.66, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.69, 0, 0, 0.59, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0.69, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.89, 0, 0],
        [0, 0.53, 0.83, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.07],
        [0.97, 0.23, 0, 0, 0, 0, 0, 0.59, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0.24, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.69, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.69, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.89, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.55, 0],
        [0, 0.54, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.07, 0, 0, 0, 0, 0, 0, 0]
    ]
    ```
- O algoritmo busca a melhor alocação possível levando em consideração:
    1. A taxa de comunicação entre os pods
        - Sendo interessante alocar no mesmo nós os pods que tenham maior taxa de comunicação
    2. O consumo de CPU
        - O algoritmo deve otimizar o consumo de CPU dos Nós.
        - Respeitar os limites de recursos disponíveis no nó.
        - O algoritmo não deve aceitar alocações infactíveis.
    3. O consumo de memória
        - Análogo aos requisitos para CPU

> **Note**: O peso do relacionamentos diz respeito ao peso da troca de informações entre um POD i e um POD j que estejam alocados no mesmo Nó.

### Calculando a Aptidão de uma alocação:
Para inserir uma alocação e receber a aptidão da alocação desejada, basta alterar o arquivo aptidao_a.py e informar a alocação desejada na variavel "alocacao".

```bash
python calcular\aptidao_a.py
```

```python
Alocação informada: [0, 1, 1, 1, 0, 2, 0, 2, 2, 1, 1, 2, 0, 0, 1, 0, 0, 2, 2, 2]
Aptidão da alocação: 0.07153645833333333
```

## Alteração de Parâmetros

**Controle do Algoritmo**

As variáveis a seguir podem ser alteradas para se obter resultados variados:

```python
tam_populacao = 100         # Tamaho da população do GA
num_geracoes = 100          # Numero de gerações do GA
prob_cruzamento = 0.8       # Probabilidade de cruzamento (80%)
prob_mutacao = 0.2          # Probabilidade de mutação (20%)
qt_teste = 10               # Qt de vezes que o teste será executado por padrão
numero_nos = 3              # Qt padrão de nós
cpu_no = 2000               # Qt de CPU de cada Nó
mem_no = 2048               # Qt de Memória de cada Nó
numero_pods = 20            # Qt de PODs a serem alocados
cpu_pod = 50                # Qt de CPU de cada POD
mem_pod = 64                # Qt de Memória de cada POD
taxa_rel = 10               # Porcentagem de preenchimento da matriz de relacionamentos
```

**Controle da Infraestrutura**

As características de memória e cpu tanto dos Nós quanto dos PODs podem ser alteradas diretamente em suas respectivas matrizes.

> **Note**: Para alteração da quantidade de Nós e de Pods é necessário alterar as variáveis: *numero_nos* e *numero_pod*. Também é necessário adequar a matriz de relacionamentos conforme a nova quantidade de PODs inseridas.

## Resultado do algoritmo

Exemplo de utilização:
```bash
---------------------------------------------
Melhor alocação encontrada no teste: 9
---------------------------------------------
Alocação: [1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 1, 1, 0, 1, 1, 2, 1, 1, 1]
Aptidão: 7.997057291666666
O POD 0 está alocado no Nó '1'
O POD 1 está alocado no Nó '1'
O POD 2 está alocado no Nó '1'
O POD 3 está alocado no Nó '1'
O POD 4 está alocado no Nó '1'
O POD 5 está alocado no Nó '1'
O POD 6 está alocado no Nó '1'
O POD 7 está alocado no Nó '1'
O POD 8 está alocado no Nó '2'
O POD 9 está alocado no Nó '0'
O POD 10 está alocado no Nó '0'
O POD 11 está alocado no Nó '1'
O POD 12 está alocado no Nó '1'
O POD 13 está alocado no Nó '0'
O POD 14 está alocado no Nó '1'
O POD 15 está alocado no Nó '1'
O POD 16 está alocado no Nó '2'
O POD 17 está alocado no Nó '1'
O POD 18 está alocado no Nó '1'
O POD 19 está alocado no Nó '1'
Recursos utilizados Nó 0: Memória = 192 CPU = 150
Recursos utilizados Nó 1: Memória = 960 CPU = 750
Recursos utilizados Nó 2: Memória = 128 CPU = 100
O somatório do peso do relacionamento dos pods do nó 0 é 0
O somatório do peso do relacionamento dos pods do nó 1 é 7.869999999999999
O somatório do peso do relacionamento dos pods do nó 2 é 0
---------------------------------------------
Melhor Alocação Global
Melhor Aptidão Global: 8.3098828125
Melhor Alocação Global: [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```
O algoritmo irá retornar o melhor indivíduo (melhor alocação) de cada uma das gerações. Ao final o Algoritmo retorna a melhor alocação e a melhor aptidão encontrada.

O Algoritmo também irá retornar um grafico representando a evolução das alocações até a alocação ótmia encontrada. O grafico a seguir apresenta o concatenado de 4 testes que foram executados.

- Cada traço azul representa uma evolução do algoritmo em cada rodada q foi executado
- A linha pontilhada em verde demarca a melhor aptidão encontrada
- A linha em vermelho demarca a média das aptidões.

![Melhor alocação encontrada](img/resultado_teste01.png)

Observando o gráfico podemos observar a evolução das aptidões convergência o ótimo global. É possível, dado o contexto, que alocações diferentes resultem em um mesmo valor de aptidão contanto que atenda os critérios propostos.

## Observações 

Para os Testes k8sgascheduler_b e k8sgascheduler_c, o algoritmo requer apenas a especificação da quantidade de vezes que será executado. Para alterar os valores e quantidades dos pods e nós, essas informações devem ser inseridas nas variáveis e matrizes do algoritmo.

