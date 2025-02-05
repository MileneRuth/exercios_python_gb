from math import cos,sin, tan
ang = float(input('Digite um angulo: '))
s = sin(ang)
c = cos(ang)
t = tan(ang)
print('O angulo escolido foi: {:.2f} \nSeu seno: {:.2f} \nSeu cosseno: {:.2f} \nÉ por fim sua tangente: {:.2f}'.format(ang, s, c, t ))