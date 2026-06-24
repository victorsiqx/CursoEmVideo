from random import randint
from time import sleep

print('''Vamos jogar JOKENPÔ!
Escolha:
[1] Pedra
[2] Papel
[3] Tesoura          
      ''')

jogadas = [' ', 'Pedra', 'Papel', 'Tesoura']
comp = randint(1, 3)

while True:
        jogador = int(input('Qual é a sua jogada? '))
        if 1 <= jogador <=3:
             break
        print('Opção Inválida! Tente novamente.')

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ!!!')
sleep(0.5)

print(f'''========================
Computador jogou {jogadas[comp]}     
Jogador jogou {jogadas[jogador]}
========================    ''')

if jogador == 1 and comp == 3:
    print('Jogador Venceu!')
elif jogador == 2 and comp == 1:
    print('Jogador Venceu!')
elif jogador == 3 and comp == 2:
    print('Jogador Venceu!')
elif jogador == comp:
    print('EMPATE!')
else:
    print('Computador Venceu!')

