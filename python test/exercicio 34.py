salario = float(input('Digete seu salario: '))
if salario <= 1250.00:
    nsalario = salario * 1.10
else:
    nsalario = salario * 1.15
print('O seu salario {} com o reajuste vai para {}'.format(salario, nsalario))