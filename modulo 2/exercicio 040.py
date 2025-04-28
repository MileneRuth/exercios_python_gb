nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirsndo {:.2f} e {:.2f}, a média do aluno é {:.2f}'.format(nota1, nota2, media))
if 7 > media >=  5 :
    print('O aluno esta de recuperação')
elif media < 5:
    print('O aluno esta reprovado')
else:
    print('O aluno esta aprovado')