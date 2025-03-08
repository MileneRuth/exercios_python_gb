velu = float(input('Qual e a velocidade atual do carro: '))
if velu >80:
    print("MULTADO! Voceê execedeu o limite permitido que é de 80km/h")
    multa = (velu -80) * 7
    print('Você deve pagar uma multa no valor de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança ')