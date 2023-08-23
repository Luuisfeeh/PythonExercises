nota1 = float(input('Qual foi sua nota no primeiro bimestre? '))
nota2 = float(input('Qual foi sua nota no segundo bimestre? '))
nota3 = float(input('Qual foi sua nota no terceiro bimestre? '))
nota4 = float(input('Qual foi sua nota no quarto bimestre? '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print('Suas notas nesse ano foram \n Primeiro Bimestre -> {} \n Segundo Bimestre -> {} \n Terceiro Bimestre -> {} \n Quarto Bimestre -> {} \n Sua média é -> {:.1f}!!'.format(nota1,nota2,nota3,nota4,media))