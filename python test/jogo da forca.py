import random
palavras = ["gato","tigre","cachorro"]
palavraesc = random.choice(palavras)
letras = ['-'] * len(palavraesc)
vidas = 6
while vidas > 0 and "-" in letras:
    print("".join("Digite uma letra: "))
    print(f"Vidas restantes: {vidas}")
    chute = input("Digite uma letra: ").lower()
    if chute in palavraesc:
        print('ihuul na mosca!')
        for i in range(len(palavraesc)):
            if palavraesc[i] == chute:
                letras[i] = chute
    else:
        print("não foi dessa vez!")
        vidas -= 1
if "-" not in letras:
    print(f"Parabéns! era isso mesmo: {palavraesc}")
else:
    print(f"Game over! você deveria ter dito: {palavraesc}")