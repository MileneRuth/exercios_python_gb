nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('\033[1;35mque nome bonito!\033[m')
elif nome == 'pedro' or nome == 'maria' or nome == 'Paulo':
    print('Seu nome e bem popular no Brasil')
else:
    print('\033[1;36mSeu nome e bem normal.\033[m')
print('tenho um bom dia, \033[1;33m{}\033[m'.format(nome))