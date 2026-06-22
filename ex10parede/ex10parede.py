larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg*alt
litrotinta = area/2

print(f'Sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².')
print(f'Para pintar essa parede, você precisara de {litrotinta}l de tinta. ')