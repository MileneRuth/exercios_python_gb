print('\033[1;32mEmprestimo Consignado\033[m')
casa = float(input('Digite o valor da casa R$: '))
sl = float(input('Quanto você recebe por mês R$: '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
minimo = sl * 30 / 100
print('Você para pagar uma casa de R${:.2f} em {} anos. '.format(casa, anos), end='')
print('a Prestação será de R${:.2f}'.format(prestação))
if prestação <= minimo:
    print('Emprestimo pode ser \033[1;32mConcedido\033[m')
else:
    print('Emprestimo \033[1;31mNegado\033[m')