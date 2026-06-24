# Exercício 27: Calculadora de Média Escolar

Este programa calcula a média aritmética de um aluno a partir de duas notas e classifica sua situação escolar (Reprovado, Recuperação ou Aprovado) com base em critérios pré-definidos.

## Funcionalidades
* Recebe duas notas como valores decimais (`float`).
* Calcula a média aritmética simples das notas.
* Classifica o desempenho do aluno utilizando a estrutura condicional `if/elif/else`:
    * Média abaixo de 5.0: Reprovado.
    * Média entre 5.0 e 6.9: Recuperação.
    * Média de 7.0 ou superior: Aprovado.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Conceitos:** Operadores aritméticos, estruturas condicionais (`if`, `elif`, `else`) e operadores lógicos (`and`).

## O que aprendi
* Como encadear múltiplas condições utilizando `elif` para cobrir diferentes faixas de valores.
* A importância de operadores lógicos como `and` para definir intervalos numéricos precisos (`media >= 5 and media <= 6.9`).
* Como transformar uma regra de negócio (tabela de notas) em um código funcional.

---
*Desenvolvido como parte do Curso de Python - Mundo 1.*