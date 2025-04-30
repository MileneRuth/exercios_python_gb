from time import sleep
print('-=-'*20)
print('\033[1:33mANALISANDO TRIANGULOS\033[m')
print('-=-'*20)
a = float(input('Digite o primeiro seguimento: '))
b = float(input('Digite o segundo seguimento: '))
c = float(input('Digite o terceiro seguimento: '))
print('\033[1:34mANALISANDO...\033[m')
sleep(2)
resultado = a < b + c and b < a + c and c < a + b
if resultado:
     equi = a == b and b == c and c == a
     iso = (a == b and a != c) or (a == c and a != b) or (b == c and b != a)
     if equi:
         print('Esse trigulo e \033[1:32mEquilátero\033[m')
     elif iso:
         print('Esse tringulo e \033[1:33mIsósceles\033[m')
     else:
         print('Esse triangulo e um \033[1:3mEscaleno\033[m')
else:
    print('Não forma um tringulo')


