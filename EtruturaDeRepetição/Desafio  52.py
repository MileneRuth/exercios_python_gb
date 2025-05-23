p = int(input('Digite um número: '))
r = int(input('Razão: '))
decimo = p + (10 - 1 ) * r
for c in range(p, decimo + r, r):
    print('{}'.format(c), end= ' ')
print('Fim ')