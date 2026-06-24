# Exercício 33: Listagem de Números Pares

Este programa exibe todos os números pares situados no intervalo de 1 a 50, utilizando uma técnica otimizada de iteração.

## Funcionalidades
* Itera sobre o intervalo de 2 a 50.
* Utiliza o parâmetro de passo (`step`) da função `range` para saltar de 2 em 2, focando apenas nos números pares.
* Exibe os números na mesma linha utilizando o parâmetro `end=' '` do comando `print`.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Conceitos:** Estruturas de repetição (`for`), intervalos customizados (`range`) e manipulação de saída de console.

## O que aprendi
* A eficácia de usar o parâmetro `step` (passo) na função `range(start, stop, step)`. Em vez de verificar se cada número é par com um `if`, o próprio `range` já gera a sequência correta, economizando processamento e linhas de código.
* Como utilizar o argumento `end` no `print` para controlar a formatação da saída, permitindo listar vários itens na mesma linha.

---
*Desenvolvido como parte do Curso de Python - Mundo 2.*