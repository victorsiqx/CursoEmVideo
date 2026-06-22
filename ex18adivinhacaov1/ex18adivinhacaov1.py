from rich import print
from random import randint
from time import sleep

print('[green]=-=[/]'*19)
print('[bold yellow]Vou pensar em um número entre 0 e 5. Tente adivinhar...[/]')
print('[green]=-=[/]'*19)

comp = randint(0, 5)
palpite = int(input('Em que número eu pensei? '))

print('[yellow]PROCESSANDO...[/]')

sleep(2)

if palpite == comp:
    print(f'[green]PARABÉNS! Você conseguiu me vencer! Pensamos no número {comp}.[/]')
else:
    print(f'[red]GANHEI! Eu pensei no número {comp} e não no {palpite}.[/]')


