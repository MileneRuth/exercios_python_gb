num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {} '.format(num,bin(num)))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {} '.format(num, oct(num)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {} '.format(num, hex(num)))
else:
    print('opção invalida tente as disponiveis 1, 2 e 3 ')