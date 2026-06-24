# Exercício 35: Analisador de Pesos

Este programa solicita o peso de cinco pessoas, analisa cada valor inserido e identifica automaticamente qual foi o maior e o menor peso registrado.

## Funcionalidades
* Itera cinco vezes utilizando um laço `for`.
* Implementa uma lógica de comparação para rastrear o maior e o menor valor em tempo real.
* Utiliza a verificação `if c == 1` para inicializar as variáveis com o primeiro peso lido, garantindo que a comparação funcione corretamente independentemente dos valores digitados.
* Exibe os resultados finais após o processamento de todas as entradas.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Conceitos:** Laços de repetição (`for`), estruturas condicionais (`if/else`) e lógica de inicialização de variáveis de controle.

## O que aprendi
* A importância de inicializar as variáveis de controle (`maior_peso` e `menor_peso`) com o primeiro valor recebido. Isso evita erros lógicos que ocorreriam se inicializássemos, por exemplo, com `0` (o que faria o `menor_peso` ficar travado em zero, por exemplo).
* Como atualizar variáveis de estado dentro de um loop, sobrescrevendo os valores antigos apenas quando uma nova condição de "máximo" ou "mínimo" é encontrada.
* O uso de lógica encadeada para realizar verificações múltiplas em cada etapa da repetição.

---
*Desenvolvido como parte do Curso de Python - Mundo 2.*