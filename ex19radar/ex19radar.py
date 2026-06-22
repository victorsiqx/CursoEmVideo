from rich import print

velocidade_atual = int(input('Qual a velocidade atual do carro? '))

multa = (velocidade_atual - 80) * 7

if velocidade_atual > 80:
    print(f'[red]MULTADO! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de[/] [yellow]R${multa:.2f}.[/]')
    print('[yellow]Tenha um bom dia! Dirija com segurança.[/]')
else:
    print('[green]Tenha um bom dia! Dirija com segurança.[/]')

