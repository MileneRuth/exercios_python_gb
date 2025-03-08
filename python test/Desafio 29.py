from time import sleep
print('Sera que vcê será multado ')
tem = float(input('Digite quanto tempo durou a viagem: '))
dis = float(input('qual e a distancia da viagem: '))
print('PROCESSANDO...')
sleep(2)
re = (dis / tem)
if re <= 80:
    print('É amigão, prepara o bolso. Você percorreu: {:.2f}km \n Isso ira custa R${:.2f}'.format(re,re * 7))
else:
    print('Suave, siga em paz ')
