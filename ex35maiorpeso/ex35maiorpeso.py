maior_peso = 0
menor_peso = 0

for c in range (1,6):
    peso = float(input(f'Peso da {c} pessoa:  '))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

print(f'O maior peso foi de {maior_peso}kgs.')
print(f'O menor peso foi de {menor_peso}kgs.')