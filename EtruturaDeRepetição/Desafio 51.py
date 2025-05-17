soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite um valor: '))
    if c % 2 == 0:
        s = soma + n
print('A soma dos {}  digitos pares é  {}'.format(cont,s))