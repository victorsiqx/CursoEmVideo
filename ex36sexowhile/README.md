# Exercício 36: Validador de Entrada (Sexo)

Este programa solicita que o usuário informe seu sexo ("M" ou "F") e utiliza um laço de repetição para garantir que, caso o dado informado seja inválido, o programa continue solicitando a entrada até que o usuário forneça um valor aceito.

## Funcionalidades
* **Padronização:** Utiliza os métodos `.upper()` e `.strip()` para limpar espaços em branco e garantir que a entrada seja tratada corretamente, independentemente de o usuário digitar em minúsculas ou com espaços.
* **Validação de Loop:** Emprega a estrutura `while` para manter o programa em execução enquanto a entrada não pertencer ao conjunto esperado `('M', 'F')`.
* **Indexação:** Utiliza `[0]` para capturar apenas a primeira letra, caso o usuário digite a palavra inteira (ex: "Masculino" vira "M").

## Tecnologias Utilizadas
* **Linguagem:** Python
* **Conceitos:** Laços de repetição (`while`), métodos de strings e manipulação de conjuntos (`tuples`).

## O que aprendi
* A importância de "blindar" o código contra erros do usuário: o `while` funciona aqui como uma barreira de segurança.
* A versatilidade de encadear métodos de string (`.upper().strip()[0]`) para transformar dados "sujos" em dados prontos para validação em apenas uma linha.
* Como utilizar o operador `not in` para checar de forma concisa se um valor é inválido.

---
*Desenvolvido como parte do Curso de Python - Mundo 2.*