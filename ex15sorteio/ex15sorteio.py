from random import choice, shuffle
alunos = []

for i in range (1, 5):
    aluno = str(input(f'{i}º Aluno: '))
    alunos.append(aluno)

sorteio = choice(alunos)
ordem_apresentacao = alunos[:]
shuffle(ordem_apresentacao)

print(f'O aluno escolhido foi: {sorteio}.')
print(f'A ordem de apresentação será: {ordem_apresentacao}.')