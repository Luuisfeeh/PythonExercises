def leiaInt(n):
    while True:
        n = input('Digite um número: ')
        if n.isnumeric():
            return int(n)
            break
        else:
            print('ERRO X__X Digite um número inteiro válido.')



print('-+-'*22)
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')
