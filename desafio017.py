import math
ops = float(input('Comprimento do cateto oposto: '))
adj = float(input('Comprimento do cateto adjacente: '))
hip = math.sqrt(ops**2 + adj**2)
print('A hipotenusa vai medir {:.2f}'.format(hip))