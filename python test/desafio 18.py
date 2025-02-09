import math
ang = float(input('Digite um angulo que você deseja: '))
s = math.sin(math.radians(ang))
c = math.cos(math.radians(ang))
t = math.tan(math.radians(ang))
print('O ângulo de {} \nTem o seno: {:.2f} \nO cosseno: {:.2f} \nE sua tamgemte: {:.2f} '.format(ang, s, c, t))