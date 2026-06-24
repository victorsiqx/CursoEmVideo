# Exercício 31: Jogo Jokenpô

Este programa permite que o usuário jogue o clássico "Pedra, Papel e Tesoura" contra o computador, que sorteia sua jogada de forma aleatória.

## Funcionalidades
* **Validação de Entrada:** Utiliza um laço `while True` para garantir que o usuário escolha apenas opções válidas (1, 2 ou 3).
* **Efeito de Jogo:** Implementa pequenos atrasos (`sleep`) para criar a expectativa do "JO-KEN-PÔ".
* **Lógica de Jogo:** Compara a jogada do jogador com a do computador baseando-se nas regras tradicionais do jogo.
* **Exibição:** Mostra claramente o que cada um escolheu através de uma lista de mapeamento.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas:** `random` (para a escolha do computador), `time` (para o efeito de espera).
* **Conceitos:** Listas, laços de repetição (`while`), estruturas condicionais (`if`, `elif`, `else`).

## O que aprendi
* Como criar um "loop de validação": o programa não prossegue enquanto o usuário não digitar um valor válido, uma prática fundamental para evitar erros em sistemas reais.
* A utilidade das listas para mapear números (1, 2, 3) em strings legíveis ('Pedra', 'Papel', 'Tesoura').
* Como estruturar uma lógica de vitória com múltiplas condições, cobrindo todos os cenários possíveis (vitória, derrota e empate).

---
*Desenvolvido como parte do Curso de Python - Mundo 1.*