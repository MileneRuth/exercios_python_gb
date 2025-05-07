from random import randint
from time import sleep
itens = ('Pedra','Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas opções são:
 [ 0 ] PEDRA
 [ 1 ] PAPEL
 [ 2 ] TESOURA''')
jogador = int(input('Qual e sua jogada? '))
print('\033[1:34mJO\033[m')
sleep(1)
print('\033[1:35mKEN\033[m')
sleep(1)
print('\033[1:33mPO !!!\033[m')
sleep(1)
print('\033[1:31m-=\033[m' * 30)
print('O computador escolheu \033[1:33m{}\033[m'.format(itens[pc]))
print('Jogador jogou \033[1:32m{}\033[m'.format(itens[jogador]))
print('\033[1:31m-=\033[m' * 30)
if pc == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada invalida')
elif pc == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Jogada invalida')
elif pc == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada invalida')
