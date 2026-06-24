# Exercício 30: Gerenciador de Pagamentos (Loja Siqueira)

Este programa simula o sistema de caixa de uma loja, calculando o valor final de uma compra de acordo com a forma de pagamento escolhida pelo cliente.

## Funcionalidades
* Recebe o preço original da compra.
* Exibe um menu de opções para o usuário.
* Aplica lógicas financeiras distintas baseadas na escolha:
    * **Opção 1 (À vista Dinheiro/Cheque):** 10% de desconto.
    * **Opção 2 (À vista Cartão):** 5% de desconto.
    * **Opção 3 (2x no Cartão):** Preço normal, sem juros.
    * **Opção 4 (3x ou mais no Cartão):** 20% de juros, com cálculo de valor por parcela.
* Valida a entrada do usuário, tratando opções inválidas.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Conceitos:** Menu de opções, estruturas condicionais (`if`, `elif`, `else`), cálculos financeiros e formatação de saída.

## O que aprendi
* Como construir uma interface de console baseada em menu (`print` com múltiplas linhas).
* A aplicação prática de porcentagens em contextos financeiros (descontos vs. juros).
* A importância de estruturar o código para lidar com o "fluxo principal" e também com "erros do usuário" (o `else` final).

---
*Desenvolvido como parte do Curso de Python - Mundo 1.*