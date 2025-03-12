viagem = float(input('Qual foi a distancia da viagem? '))
if viagem <= 200 :
    print('será cobrado uma taxa de R$0,50. você pagará R$ {}'.format(viagem+ 0,50))
else:
    print('Para viagens acima de 200km serão cobrado R$0,45. você pagara R${}'.format(viagem+0,45))