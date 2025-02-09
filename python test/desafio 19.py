import random
a1 = str(input('Digite o nome do 1° aluno: '))
a2 = str(input('Digite o nome do 2° aluno: '))
a3 = str(input('Digite o nome do 3° aluno: '))
a4 = str(input('Digite o noem do 4° aluno: '))
alunos = [a1, a2, a3, a4]
escolhido = random.choice(alunos)
print('O aluno que ira apagar o quadra e o: {}'.format(escolhido))