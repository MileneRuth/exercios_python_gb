from datetime import date
ano = int(input('Que ano quer analisar? coloque 0 para analisar o ano atual:  '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('o ano {}. é BISSEXTO'.format(ano))
else:
    print('O ano {}. não e BISSEXTO'.format(ano))