print('GERADOR DE PA')
print('--' * 20)
n1 = int(input('Digite o elemento: '))
n2 = int(input('Digite a razão: '))
termo = n1
cont = 1
while cont <= 10:
    print('{} -> '.format(termo),end='')
    termo += n2
    cont += 1
print('FIM')
