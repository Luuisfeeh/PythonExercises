from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n = 0
while n != 5:
    print('\033[0;37;40m[ 1 ] somar\033[m')
    print('\033[0;37;40m[ 2 ] multiplicar\033[m')
    print('\033[0;37;40m[ 3 ] maior\033[m')
    print('\033[0;37;40m[ 4 ] novos números\033[m')
    print('\033[0;37;40m[ 5 ] sair do programa\033[m')
    print('--' * 15)
    n = int(input('>>>>>Escolha uma opção: '))
    if n == 1:
        soma = n1 + n2
        print('A soma entre os valores \033[0;31m{}\033[m e \033[0;34m{}\033[m é equivalente a \033[0;35m{}\033[m!'.format(n1,n2,soma))
        print('--' * 15)
    elif n == 2:
        mult = n1 * n2
        print('A multiplicação entre os valores \033[0;31m{}\033[m e \033[0;34m{}\033[m é equivalente a \033[0;35m{}\033[m!'.format(n1,n2,mult))
        print('--' * 15)
    elif n == 3:
        if n1 == n2:
            print('Você escreveu números iguais bobão! ')
            print('--' * 15)
        elif n1 > n2:
            print('O \033[0;31m{}\033[m é o maior dos valores!'.format(n1))
            print('--' * 15)
        else:
            print('O \033[0;34m{}\033[m é o maior dos valores!'.format(n2))
            print('--' * 15)
    elif n == 4:
        n1 = int(input('Digite outro valor para o primeiro: '))
        n2 = int(input('Digite outro valor para o segundo: '))
        print('--' * 15)
    elif n == 5:
        print('--' * 15)
    else:
        print('-+-' * 12)
        print('ERRO X_X Digite um dos valores abaixo POR FAVOR!')
        print('-+-' * 12)
    sleep(2)
print('Obrigado pela experiência!!')