from datetime import date
atual = date.today().year
nas = int(input('Ano de nascimento: '))
idade = atual - nas
print('Quem nasceu em {} tem {} anos em {}.'.format(nas, idade, atual))
if idade == 18:
    print('Voce tem que se alista IMEDIATAMENTE! ')
elif idade < 18:
    saldo = 18 - idade
    print('Você não tem a idade nercessaria ainda, que e de 18 anos.\n ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
