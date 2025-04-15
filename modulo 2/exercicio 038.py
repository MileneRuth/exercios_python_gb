print('Entre 2 valores vamos ver qual e o maior ')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('o valor maior entre {} , {} e o {}'.format(n1,n2, n1))
elif n2 > n1:
    print('o valor mior entre {}, {} e o {}'.format(n2,n1,n2))
elif n1 == n2:
    print('não a valor maior os valores {} , {}.  são iguais'.format(n1,n2))