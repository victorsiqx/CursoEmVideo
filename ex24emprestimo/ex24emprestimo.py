valor_casa = float(input('Qual o valor da casa? '))
salario = float(input('Salário do comprador: '))
ano_pagar = int(input('Quantos anos de financiamento? '))

prestacao = valor_casa/(ano_pagar*12)
prestacao_proibida = salario*0.3

if prestacao > prestacao_proibida:
    print(f'Para pagar uma casa de {valor_casa:.2f} em {ano_pagar} anos a prestação será de R${prestacao:.2f}.\nEmpréstimo NEGADO!')
else:
    print(f'Para pagar uma casa de {valor_casa:.2f} em {ano_pagar} anos a prestação será de R${prestacao:.2f}.\nEmpréstimo PODE SER CONCEDIDO!')
