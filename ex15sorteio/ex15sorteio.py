from random import choice, shuffle
alunos = []

for i in range (1, 5):
    aluno = str(input(f'{i}º Aluno: '))
    alunos.append(aluno)

sorteio = choice(alunos)
#ordem_apresentacao = alunos[:]
shuffle(alunos)

print(f'O aluno escolhido foi: {sorteio}.')
print(f'A ordem de apresentação será: {alunos}.')