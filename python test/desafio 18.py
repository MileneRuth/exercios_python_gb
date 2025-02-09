from math import radians,sin,cos,tan
ang = float(input("Digite o ângulo: "))
s = sin(radians(ang))
c = cos(radians(ang))
t = tan(radians(ang))
print("o ângulo: {:.2f} \nCorresponde ao seno: {:.2f} \nÉ o cosseno: {:.2f} \nÉ sua tangente: {:.2f}".format(ang, s, c, t))