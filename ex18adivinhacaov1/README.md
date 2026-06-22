# Exercício 19: O Jogo da Adivinhação

Este programa é um jogo interativo onde o computador "pensa" em um número aleatório entre 0 e 5, e o usuário deve tentar adivinhar qual é esse número.

## Funcionalidades
* Gera um número inteiro aleatório entre 0 e 5 utilizando o módulo `random`.
* Adiciona um efeito de "delay" (espera) para simular o processamento do computador.
* Utiliza a biblioteca `rich` para fornecer uma interface visualmente atraente no terminal (cores e negrito).
* Compara o palpite do usuário com o número sorteado e exibe o resultado (vitória ou derrota).

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas:** `rich` (estilização), `random` (números aleatórios), `time` (controle de tempo).
* **Conceitos:** Estruturas condicionais (`if/else`), entrada de dados, importação de pacotes e formatação de texto.

## O que aprendi
* A importância de bibliotecas de terceiros como a `rich` para melhorar a experiência do usuário (UX) no terminal.
* O uso de `sleep(2)` para criar interações mais realistas, "humanizando" o tempo de resposta do software.
* Como aplicar uma estrutura lógica simples (`if/else`) para criar um jogo funcional.

---
*Desenvolvido como parte do Curso de Python - Mundo 1.*