salario = float(input('digite aqui seu salario: '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('O salario {} com o reajuse vai para {}'.format(salario,novo))