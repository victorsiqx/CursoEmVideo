# Exercício 38: Menu Interativo de Operações

Este programa oferece uma interface de menu no terminal onde o usuário pode realizar diversas operações matemáticas com dois números escolhidos, alterar esses números ou encerrar o sistema.

## Funcionalidades
* **Gerenciamento de Estado:** O usuário pode manter dois números na memória e alterá-los a qualquer momento através da opção [4].
* **Operações Matemáticas:**
    * [1] Soma
    * [2] Multiplicação
    * [3] Identificação do Maior valor
* **Controle de Fluxo:** Implementa uma estrutura de loop infinito (`while True`) que só é interrompida pela escolha da opção de saída [5].
* **Tratamento de Erros:** Valida entradas inválidas dentro do menu, solicitando nova escolha do usuário.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas:** `time` (para pausar a interface após cada operação).
* **Conceitos:** Loop infinito, estruturas condicionais (`if/elif/else`), manipulação de variáveis e funções built-in (`max`).

## O que aprendi
* A importância do **ciclo de vida do programa**: entendi como manter uma aplicação ativa até uma condição de parada (o `break` na opção 5).
* Como atualizar variáveis globais (`num1`, `num2`) dinamicamente durante a execução do programa.
* A criação de uma experiência de usuário (UX) básica no terminal, usando `sleep(2)` e delimitadores (`print('-'*20)`) para tornar a leitura mais agradável.

---
*Desenvolvido como parte do Curso de Python - Mundo 2.*