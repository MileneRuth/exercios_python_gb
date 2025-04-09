print('\033[1;32mEmprestimo Consignado\033[m')
valor = float(input('Digite o valor da casa R$: '))
sl = float(input('Quanto você receb por mês R$: '))
anos = valor / sl
print('Você paraga R${:.2f} por tantos anos'.format(anos))
