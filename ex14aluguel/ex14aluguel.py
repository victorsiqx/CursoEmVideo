PRECO_POR_DIA = 60
PRECO_POR_KM = 0.15

dias_alugado = int(input('Quantos dias alugados? '))
km_rodados = int(input('Quantos Km rodados? '))

preco_aluguel = (dias_alugado*PRECO_POR_DIA) + (km_rodados*PRECO_POR_KM)

print(f'O total a pagar é de R${preco_aluguel:.2f}.')
