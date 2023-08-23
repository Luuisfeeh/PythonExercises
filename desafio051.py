print('='*30)
print('    10 TERMOS DE UMA PA ')
print('='*30)
n1 = int(input('Primeiro elemento: '))
r1 = int(input('Razão: '))

ultimo = n1 + (10-1)*r1

for c in range(n1, ultimo+1, r1):
    print('{} '.format(c), end='-> ')
print('\n ACABOU')