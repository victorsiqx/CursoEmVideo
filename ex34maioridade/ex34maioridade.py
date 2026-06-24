from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0

for c in range (1, 8):
    nasc = int(input(f'Em que ano a {c}º pessoa nasceu? '))
    idade = ano_atual - nasc
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Ao todo temos {maiores} pessoas maiores.')
print(f'Ao todo temos {menores} pessoas menores.')
