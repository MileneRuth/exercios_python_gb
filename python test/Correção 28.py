from random import randint
from time import sleep
pc = randint(0,5)
print('-=-' * 20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar ...')
print('-=-' * 20)
game = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if game == pc:
    print('PARABÉNS! você acertou ',)
else:
    print('GANHEI!, Eu pensei no número {} e não no {}'.format(pc, game))
