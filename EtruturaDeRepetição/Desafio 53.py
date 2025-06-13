frase = str(input('Digite uma frase: ')).strip().replace(" ","").upper()
print(frase)
invertida = frase[:: -1]
print(invertida)
if frase == invertida:
    print('E um palíndromo!')
else:
    print('Não é um palíndromo')