print('vamos saber se você esta aprovado')
notas1 = float(input('qual foi sua 1 nota: '))
notas2 = float(input('Qual foi sua 2 nota: '))
resultado = (notas1 + notas2) / 2
if resultado <= 5.0:
    print('Sua nota foi {} isso significa \033[1;31mREPROVADO\033[m'.format(resultado))
elif resultado >= 5.0 and resultado <= 6.9:
    print('sua nota foi {} isso signica \033[1;33mRECUPERAÇÃO\033[m'.format(resultado))
elif resultado >= 7.0:
    print('Sua nota foi {:.2f} isso significa \033[1;32mAPROVADO\033[m'.format(resultado))

