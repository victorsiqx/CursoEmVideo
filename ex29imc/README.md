# Exercício 29: Calculadora de IMC (Índice de Massa Corporal)

Este programa calcula o IMC de uma pessoa a partir do seu peso e altura e, em seguida, classifica o resultado em categorias de saúde padronizadas pela OMS.

## Funcionalidades
* Recebe o peso (Kg) e a altura (m) como valores decimais.
* Calcula o IMC utilizando a fórmula: $IMC = peso / (altura^2)$.
* Classifica o resultado em cinco categorias:
    * Abaixo do Peso: IMC < 18.5
    * Peso Ideal: 18.5 ≤ IMC ≤ 25
    * Sobrepeso: 25 < IMC ≤ 30
    * Obesidade: 30 < IMC ≤ 40
    * Obesidade Mórbida: IMC > 40
* Exibe o valor do IMC formatado com uma casa decimal.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Conceitos:** Operadores aritméticos, potenciação, estruturas condicionais (`if`, `elif`, `else`) e formatação de strings.

## O que aprendi
* Como estruturar uma lógica de "classificação por faixas" utilizando `elif` para evitar testes redundantes.
* A importância da ordem das condições: ao testar as faixas do menor para o maior, o código se torna extremamente eficiente.
* Como aplicar fórmulas matemáticas (incluindo o uso de potência) dentro de um fluxo de dados.

---
*Desenvolvido como parte do Curso de Python - Mundo 1.*