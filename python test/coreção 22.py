nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome....')
print('Seu nome maiúsculo é {}'.format(nome.upper()))
print('Seu nome minúsculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} tantas letras'.format(nome.find(' ')))