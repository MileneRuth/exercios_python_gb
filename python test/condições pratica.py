nome = str(input('Qual e sue nome: ')).strip()
if nome == 'Gustavo':
    print("que nome lindo você tem!")
else:
    print('Seu nome é tão comum')
print('Bom dia, {}'.format(nome.lower()))