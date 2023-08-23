def leiaInt(s):
    while True:
        try:
            i = int(input(s))
        except (ValueError, TypeError):
            print('ERROR X__X Digite um número Inteiro!')
            continue
        except (KeyboardInterrupt):
            print('ENTRADA DE DADOS INTERROMPIDA POR USUARIO!!')
            return 0
        else:
            return i


def leiaReal(s):
    while True:
        try:
            r = float(input(s))
        except (ValueError, TypeError):
            print('ERROR X__X Digite um número Real!')
            continue
        except (KeyboardInterrupt):
            print('ENTRADA DE DADOS INTERROMPIDA POR USUARIO!!')
            return 0 
        else:
            return r


# print('-+-'*22)
# n = leiaInt('Digite um número Inteiro: ')
# r = leiaReal('Digite um número Real: ')
# print(f'Você digitou o número {n} como Inteiro e {r} como Real')
