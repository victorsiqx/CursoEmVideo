# Exercício 28: Classificador de Atletas

Este programa calcula a idade de um atleta com base em seu ano de nascimento e o classifica automaticamente em uma categoria esportiva, utilizando critérios de faixas etárias.

## Funcionalidades
* Calcula a idade atual utilizando o ano de nascimento do atleta.
* Define a categoria esportiva através de uma estrutura condicional encadeada:
    * Até 9 anos: MIRIM
    * Até 14 anos: INFANTIL
    * Até 19 anos: JÚNIOR
    * Até 25 anos: SÊNIOR
    * Acima de 25 anos: MASTER
* Exibe a classificação correspondente.

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Bibliotecas:** `datetime` (para obter o ano atual).
* **Conceitos:** Aritmética de datas, estruturas condicionais (`if`, `elif`, `else`).

## O que aprendi
* A importância da **ordem das condições** em um `if/elif` encadeado: note que, ao testar `idade <= 9` primeiro, não preciso verificar se o número é maior que 0, pois o código já filtra de forma sequencial.
* Como criar sistemas de classificação que escalam facilmente; caso surjam novas categorias no futuro, basta adicionar novos `elif`.

---
*Desenvolvido como parte do Curso de Python - Mundo 1.*