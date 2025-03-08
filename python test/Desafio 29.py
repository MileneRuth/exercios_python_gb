from time import sleep
print('Sera que vcê será multado ')
tem = float(input('Digite quanto tempo durou a viagem: '))
dis = float(input('qual e a distancia da viagem: '))
print('PROCESSANDO...')
sleep(2)
re = (tem * dis)
if re <= 80:
    print('É parceito você será multado')
else:
    print('Suave, siga em paz ')
