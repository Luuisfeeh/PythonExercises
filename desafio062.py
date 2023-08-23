print('GERADOR DE PA')
print('--' * 20)
n1 = int(input('Digite o elemento: '))
n2 = int(input('Digite a razão: '))
termo = n1
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += n2
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer a mais? '))
print('Progressão finalizada com {} tantos termos mostrados.'.format(total))
