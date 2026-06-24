print('='*30)
print('  LOJA SIQUEIRA - PAGAMENTO')
print('='*30)
preco = float(input('Preço das compras: R$ '))

print("""FORMAS DE PAGAMENTO
[1] À vista Dinheiro/Cheque
[2] À vista Cartão
[3] 2x no Cartão
[4] 3x ou mais no Cartão         
""")

opcao = int(input('Qual é a opção? '))

if opcao == 1:
    novo_preco = preco - preco*0.10
    print(f'Sua compra de R${preco:.2f} vai custar R${novo_preco:.2f} no final.')

elif opcao == 2:
    novo_preco = preco - preco*0.05
    print(f'Sua compra de R${preco:.2f} vai custar R${novo_preco:.2f} no final.')


elif opcao == 3:
    print(f'O preço final da sua compra é de R${preco:.2f}.')
    

elif opcao == 4:
    novo_preco = preco + preco*0.2
    parcelas = int(input('Quantas parcelas vão ser? '))
    print(f'Sua compra será parcelada em {parcelas}x de R${novo_preco/parcelas:.2f} COM JUROS.')
    print(f'Sua compra de R${preco:.2f} vai custar R${novo_preco:.2f} no final.')

else:
    print('Opção Invalida. Reinicie o programa e tente novamente.')
    