n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;33m', end= ' ')
        tot += 1
    else:
        print('\033[1;31m',end=' ')
    print('{} '.format(c))
print('\n \033[m0 número {} foi divisível {} vezes'.format(n,tot))
if tot == 2:
    print('E por isso que ele e PRIMO ')
else:
    print('Esse número NÂO e primo ')