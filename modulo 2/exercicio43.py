print('Vamos ver seu indice corporal')
peso = float(input('Qual é seu peso atual: '))
altura = float(input('Qual é sua altura: '))
imc = peso/pow(altura,2)
if imc < 18.5:
    print('Você esta com baixo peso')
elif imc <= 24.9:
    print('Seu peso está normal')
elif imc <= 29.9:
    print('Você está com sobrepeso')
elif imc <= 34.9:
    print('Obesidade grau 1 ')
elif imc <= 39.9:
    print('Obesidade grau 2')
else:
    print('Obesidade grau 3')
print('Obrigado por classificar com a gente')
