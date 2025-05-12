from time import sleep
import emoji
print('Contagem regressiva')
for cont in range(10,-1, -1):
    print(cont, sleep(1))
print(emoji.emojize('BUM :fireworks:', language = 'alias'))