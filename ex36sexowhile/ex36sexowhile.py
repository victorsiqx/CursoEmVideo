sexo = str(input('Informe o seu sexo [M/F]: ')).upper().strip()[0]

while sexo not in ('M','F'):
    sexo = str(input('Dados Inválidos. Por favor, informe o seu sexo [M/F]: ')).upper().strip()[0]

print(f'Sexo {sexo} registrado com sucesso.')
    
