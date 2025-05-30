n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[1;33m', end= ' ')
    else:
        print('\033[1;31m',end=' ')
    print('{} '.format(c))
