# Exercício 26: Simulador de Alistamento Militar

Este programa calcula a idade de um usuário com base no seu ano de nascimento e determina a situação do seu alistamento militar obrigatório (se ainda falta tempo, se está no prazo ou se já passou do prazo).

## Funcionalidades
* Obtém o ano atual automaticamente utilizando a biblioteca `datetime`.
* Calcula a idade exata com base no ano de nascimento fornecido.
* Define a situação do usuário:
    * **Abaixo de 18:** Informa quantos anos faltam e o ano exato do alistamento.
    * **18 anos:** Alerta que o alistamento é imediato.
    * **Acima de 18:** Calcula há quantos anos o alistamento deveria ter ocorrido e informa o ano que isso aconteceu.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas:** `datetime` (para manipulação de datas).
* **Conceitos:** Manipulação de tempo, estruturas condicionais (`if`, `elif`, `else`) e aritmética de datas.

## O que aprendi
* Como utilizar o módulo `datetime` para tornar o código independente de atualizações manuais de ano.
* A lógica de utilizar múltiplas condições (`if/elif/else`) para cobrir todos os cenários possíveis de uma regra de negócio.
* Como realizar projeções temporais (calcular anos futuros ou passados baseados em uma variável de entrada).

---
*Desenvolvido como parte do Curso de Python - Mundo 1.*