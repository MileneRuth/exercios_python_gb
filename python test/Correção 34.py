salario = float(input('digite aqui seu salario: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O salario {:.2f} com o reajuse vai para {:.2f}'.format(salario,novo))