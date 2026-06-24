valores = []

for c in range (0,3):
    valor = int(input(f'{c+1}º Valor: '))
    valores.append(valor)

print(f'O menor valor digitado foi {min(valores)}.\nO maior valor digitado foi {max(valores)}.')
