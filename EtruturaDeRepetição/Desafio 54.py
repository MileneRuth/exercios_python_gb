from datetime import date
ano = date.today().year
for c in range(1,8):
    data = int(input('Digite a data de nascimento da {}° pessoa: '.format(c)))
    idade = ano - data
    if idade >= 21:
        print('maior de idade com {} anos.'.format(idade))
    else:
        print('menor de idade com {} anos.'.format(idade))

