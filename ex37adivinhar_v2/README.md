# Exercício 37: Jogo da Adivinhação Inteligente

Este programa aprimora o clássico jogo de adivinhação. O computador sorteia um número entre 1 e 10, e o usuário deve tentar acertar. A diferença fundamental é que o programa fornece "pistas" (Mais ou Menos) após cada palpite errado, além de contabilizar o número total de tentativas até a vitória.

## Funcionalidades
* **Lógica de Feedback:** Fornece dicas ao jogador se o número sorteado é maior ou menor que o palpite atual.
* **Contador de Tentativas:** Registra quantas jogadas foram necessárias para alcançar o objetivo.
* **Loop de Controle:** Utiliza uma estrutura `while not acertou` que mantém o jogo rodando até que o objetivo seja cumprido.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas:** `random` (para o sorteio).
* **Conceitos:** Laços de repetição (`while`), estruturas condicionais aninhadas (`if/else`) e variáveis de estado (flags booleanas).

## O que aprendi
* Como usar uma variável de estado (`acertou = False`) para controlar o fluxo do `while` de forma muito mais legível que um `while True`.
* A implementação de algoritmos de busca básica: ao dar pistas, transformei o jogo de uma simples tentativa e erro em uma busca lógica (similar a uma busca binária).
* Como acumular dados de desempenho (o contador `tentativas`) para dar um resumo final ao usuário sobre o seu sucesso.

---
*Desenvolvido como parte do Curso de Python - Mundo 2.*