distancia = float(input('Qual é a distancia de sua viagem: '))
print('Você esrtá começando uma viagem de {}Km'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia *0.45
print(' É o preço da sua passagem vai ser de R${:.2f}'.format(preço))