n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digiete o terceiro valor: '))
resultado = n1 < n2 and n1 > n2
if n3 < resultado:
    print('o menor entre {}, {}, {} e o {}'.format(n1, n2,n3, resultado))
else:
    print('o menor resultado e menor e {}'.format(resultado))
