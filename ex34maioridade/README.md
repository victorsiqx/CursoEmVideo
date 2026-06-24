# Exercício 34: Analisador de Maioridade

Este programa solicita o ano de nascimento de sete pessoas, calcula suas idades com base no ano atual e apresenta a contagem de quantos indivíduos são maiores de idade e quantos são menores.

## Funcionalidades
* Itera sete vezes utilizando um laço `for`.
* Calcula a idade de cada pessoa dinamicamente (usando `datetime`).
* Utiliza variáveis contadoras (`maiores` e `menores`) para acumular os resultados conforme o usuário insere os dados.
* Exibe o resultado final da contagem.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas:** `datetime` (para obter o ano atual).
* **Conceitos:** Laços de repetição (`for`), acumuladores, estruturas condicionais (`if/else`) e aritmética de datas.

## O que aprendi
* A importância dos **acumuladores**: entendi que, para contar itens dentro de um loop, preciso de uma variável iniciada em zero que seja incrementada (`+= 1`) sempre que uma condição for atingida.
* Como aplicar lógica em larga escala: o mesmo código processa uma ou sete pessoas sem precisar de modificações na estrutura, bastando apenas alterar o range do `for`.
* A versatilidade de combinar a biblioteca `date` com laços para criar programas que se mantêm atualizados automaticamente ao longo dos anos.

---
*Desenvolvido como parte do Curso de Python - Mundo 2.*