print(20*'-=-')
print('\033[1;34mBem vindo ao programa de natação.\033[m')
idade = int(input('Digite sua idade para iniciar: '))
if idade <= 9:
    print('Com a idade de {}anos você se enquadra em \033[1:33mMIRIM\033[m'.format(idade))
elif idade > 9 and idade < 14:
    print('com essa idade de {}anos você se enquadra em \033[1:32mINFANTIL\033[m'.format(idade))
elif idade > 14 and idade < 19:
    print('Com a idade de {}anos você se enquadra em \033[1;34mJUNIOR\033[m'.format(idade))
elif idade == 20:
    print('com {}anos você e um \033[1;35mSÊNIOR\033[m'.format(idade))
else:
    print('com {} anos você e um \033[1;31mMASTER\033[m'.format(idade))
print('obrigada, por enquanto e isso \033[1;31m<3\033[m')
print(20*'-=-')