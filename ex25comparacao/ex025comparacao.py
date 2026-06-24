num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))

print(f'O primeiro valor é maior.' if num1 > num2 else ('O segundo valor é maior.' if num2 > num1 else 'Os valores são iguais.'))