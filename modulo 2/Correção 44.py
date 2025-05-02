print('{:=^40}'.format('LOJAS MILENE'))
preco = float(input('Preço das compras R$: '))
print('''FORMA DE PAGAMENTO
[ 1 ] á vista dinheiro
[ 2 ] á vista cartão debito
[ 3 ] 2x no cartão credito
[ 4 ] 3x ou mais cartão de credito''')
opcao = int(input('Qual opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcela em 2x de {} '.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/ 100)
    totparc = int(input('Quantas parcelas? '))
    parcelas = total / totparc
    print('Sua compra será parcela em {} x de R${:.2f} COM JUROS '.format(totparc, parcelas))
else:
    total = preco
    print('\033[1:31mOPÇÃO INVALIDA DE PAGAMENTO\033[m')
print('Sua compra de R${:.2f} vai custa R${:.2f} no final'.format(preco, total))