from random import randint
comp = randint(1, 10)
acertou = False
tentativas = 0
print('''Sou seu computador... Acabei de pensar em um numero entre 1 e 10.
Será que você consegue adivinhar qual foi? 
''')

while not acertou:
        palpite = int(input('Qual é seu palpite? '))
        tentativas += 1
        if palpite == comp:
            acertou = True
        else:
            if palpite < comp:
                print('Mais... tente novamente.')
            else:
                print('Menos... tente novamente.')

print(f'Acertou com {tentativas} tentativas.')
