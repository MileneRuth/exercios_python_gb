distancia = float(input('Qual e a distancia da sua viagem: '))
print('Você esta preste a coeçar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('É o preço da sua passagem será de R${:.2f}'.format(preço))