km = int(input('Qual é a distância da sua viagem? '))

passagem_curta = km*0.5
passagem_longa = km*0.45

if km <= 200:
    print(f'Você está prestes a começar uma viagem de {km}Km.\nE o preço da sua passagem será de R${passagem_curta:.2f}.')
    
else:
    print(f'Você está prestes a começar uma viagem de {km}Km.\nE o preço da sua passagem será de R${passagem_longa:.2f}.')
