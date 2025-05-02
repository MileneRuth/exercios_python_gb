peso = float(input('Qual e seu peso? (Kg): '))
altura = float(input('Qual é sua altura? (m): '))
imc = peso/ (altura ** 2)
print('O IMC dessa pessoa e de {:.2f}'.format(imc))
if imc < 18.5:
    print('Você esta abaixo do peso normal')
elif 18.5 < imc < 25:
    print('Parebéns você esta com Peso normal')
elif 25 <= imc < 30:
    print('Você está em Sobrepeso')
elif 30 <= imc < 40:
    print('Você está em Obessidade mórbida, cuidado ')