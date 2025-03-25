from time import sleep
print('-=-' * 20)
print('ANALISANDO TRIÂGULOS')
print('-=-' * 20)
a = float(input('Digite o primeiro seguimento: '))
b = float(input('Digite o Segundo seguimento: '))
c = float(input('digite o terceiro seguimento: '))
print('ANALISANDO....')
sleep(2)
resultado = [a,b,c]
if resultado == a < b+c:
    print('OPAA, podemos fazer u tringulo com esses seguimentos ')
else:
    print('Infelizmente já não podemos fazer um triangulo')