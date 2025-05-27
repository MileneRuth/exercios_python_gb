n = int(input('Digite um núemro: '))
primo = True
for c in range(2,n):
    if n % c == 0:
        primo = False
        break
if primo:
    print('O  número {} é primo'.format(n))
else:
    print('O número {} não e primo'.format(n))
