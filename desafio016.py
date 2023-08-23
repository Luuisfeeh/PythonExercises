from math import trunc
num = float(input('Digite um número: '))
inteiro = trunc(num)
print('O número {} tem a parte inteira {}'.format(num,inteiro))

num = float(input('Digite um número: '))
print('O número {} tem a parte inteira {}'.format(num, int(num)))