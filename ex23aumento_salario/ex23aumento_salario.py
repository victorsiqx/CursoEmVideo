salario = float(input('Qual é o salário do funcionário? R$ '))
novo_salario = salario+salario*0.10 if salario > 1250 else salario+salario*0.15

print(f'Quem ganhava R${salario:.2f} passa a ganhar {novo_salario:.2f} agora.')