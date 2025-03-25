from time import sleep
print('-=-'* 20)
print('ANALISADOR DE RETÂNGULO')
print('-=-' * 20)
n1 = float(input('Digite o primeiro seguimento: '))
n2 = float(input('Digite o segundo seguimento: '))
n3 = float(input('Digite o terceiro seguimento: '))
if n1 < n2+n3 and n2 < n1+n2 and n3 < n1 + n2:
    print('ESSES SEGUIMENTOS FORMAM UM TRIÂNGULO')
else:
    print('NÃO FORMAM UM TRIÂNGULO')