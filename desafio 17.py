import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Cumprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir: {:.2f}'.format(hi))