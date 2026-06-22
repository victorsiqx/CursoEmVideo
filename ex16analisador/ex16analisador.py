nome = str(input('Digite o seu nome completo: ')).strip()
qtdLetras = len(nome) - nome.count(" ")
primeiro_nome = nome.split()

print(f'Analisando seu nome...\nSeu nome em MAIÚSCULAS é: {nome.upper()}.\nSeu nome em MINÚSCULAS é {nome.lower()}.')
print(f'Seu nome tem ao todo {qtdLetras} letras.\nSeu primeiro nome é {primeiro_nome[0]} e tem {len(primeiro_nome[0])} letras.')