from time import sleep

num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
while True:

    print('''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair do programa
        ''')

    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        print(f'A soma entre {num1}+{num2} é {num1+num2}.')      
    elif opcao == 2:
        print(f'A multiplicaação entre {num1}x{num2} é {num1*num2}.')
    elif opcao == 3:
        print(f'Entre {num1} e {num2} o maior valor é {max(num1, num2)}.')
    elif opcao == 4:
        print('Informe os números novamente: ')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Encerrando o programa. Volte sempre!')
        break
    else:
        print('Opção Invalida. Escolha a opção novamente.')
    print('-'*20)
    sleep(2)

