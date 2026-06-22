salario = float(input('Qual é o salário do funcionário? R$ '))
aumento = 0.15
novo_salario = salario+(salario*aumento)

print(f'Um funcionário que ganhava {salario}, com 15% de aumento, passa a receber R${novo_salario:.2f}.')