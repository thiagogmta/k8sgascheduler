# k8sgaScheduler
**Algoritmo para alocação inteligente de recursos em cluster kubernetes**

> Artefato proposto no artigo intitulado: K8sGAScheduler: Algoritmo para alocação inteligente de recursos em cluster kubernetes apresentado no WGRS – Workshop de Gerência e Operação de Redes e Serviços - 2024. Autores: Thiago Guimarães Tavares (IFTO), Carlos Eduardo santos (IFTO), Kleber Vieira Cardoso (UFG), Antonio Oliveira-Jr (UFG)

## Introdução

O Kubernetes é uma plataforma de código aberto amplamente utilizada para gerenciar cargas de trabalho e serviços em contêineres. No entanto, a otimização da alocação de pods é uma questão complexa que requer soluções avançadas. Este projeto apresenta o K8sGAScheduler, um algoritmo inteligente desenvolvido para otimizar a alocação de recursos em clusters Kubernetes. Nossa abordagem leva em conta o consumo de recursos, a comunicação entre os pods e as restrições de capacidade dos nós.

- O objetivo é encontrar a melhor alocação possível de pods, visando maximizar a eficiência do cluster.

É importante mencionar que este código é uma avaliação do modelo matemático proposto para o K8sGAScheduler e, nesta fase, não é executável diretamente dentro do Kubernetes. A finalidade deste projeto é validar a formulação matemática e o algoritmo de alocação.

## Dependências

Para rodar este repositório localmente, é necessário ter as seguintes dependências instaladas:

- Python 3.8+: Linguagem de programação principal utilizada no projeto.
- Bibliotecas Python:
  - numpy: Para operações matemáticas e manipulação de arrays.
  - matplotlib: Para visualização de dados e geração de gráficos.

## Teste experimental



## Documentação

[Wiki - k8sGaScheduler](docs/documentacao.md)