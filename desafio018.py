import math
ang = float(input('Digite o ângulo que você deseja: '))
angu = math.radians(ang)
seno = math.sin(angu)
cosseno = math.cos(angu)
tang = math.tan(angu)
print('O Cosseno desse ângulo é {:.2f}'.format(cosseno))
print('O Seno desse ângulo é {:.2f}'.format(seno))
print('A Tangente desse ângulo é {:.2f}'.format(tang))