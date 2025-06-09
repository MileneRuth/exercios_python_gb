frase = str(input('Digite uma frase: ')).strip().replace(" ","").upper()
print(frase)
for letra in frase[:: -1]:
    if frase == frase:
        print ('E uma palídromo')
    else:
        print('não e um políndromo')
print('fim') 