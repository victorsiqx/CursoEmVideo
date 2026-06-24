from datetime import date

ano_nasc = int(input('Ano de nascimento: '))

ano_atual = date.today().year

idade =  ano_atual - ano_nasc

print(f'Quem nasceu em {ano_nasc} tem {idade} anos em {date.today().year}.')

if idade > 18:
    print(f'Você deveria já deveria ter se alistado há {idade-18} anos.\nSeu alistamento foi em {ano_atual - (idade-18)}.')
elif idade == 18:
    print('É hora de se alistar IMEDIATAMENTE!')
else:
    print(f'Ainda faltam {18-idade} anos para o alistamento.\nSeu alistamento será em {ano_atual+(18-idade)}.')

