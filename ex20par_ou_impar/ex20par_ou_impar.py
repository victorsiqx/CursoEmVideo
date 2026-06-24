from rich import print

num = int(input('Me diga um número qualquer: '))

if num % 2 == 0:
    print(f'O número {num} é [green]PAR![/]')
else:
    print(f'O número {num} é [blue]IMPAR![/]')
