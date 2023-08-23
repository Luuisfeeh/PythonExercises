import random

print('-=-' *10)
print('  VAMOS JOGAR PAR OU IMPAR? ')
print('-=-' *10)
count = 0
nAleatorio = random.randint(0,10)
soma = 0
resp = str(input('Quer jogar? [S/N] ')).strip().upper()
print('-=-' *10)
if resp == 'S':
    n = int(input('Qual número você quer chutar? '))
    print('-=-' * 10)
    soma = n + nAleatorio
    IP = str(input('Impar ou Par?? [I/P] ')).strip().upper()
    print('-=-' * 10)
    while True:
        if soma%2 == 0 :
            print(f'Seu número foi {n} e eu escolhi o {nAleatorio}. A soma deles foi {soma} então é PAR!')
            print('-=-' * 10)
            if IP == 'P':
                print('Droga você ganhou de mim :/. Vamos tentar dnv...')
                print('-=-' * 10)
                nAleatorio = random.randint(0, 100)
                count += 1
                n = int(input('Qual número você quer chutar? '))
                IP = str(input('Impar ou Par?? [I/P] ')).strip().upper()
                print('-=-' * 10)
            else:
                print(f'Que pena você PERDEUU! Você ganhou {count}!')
                break
        else:
            print(f'Seu número foi {n} e eu escolhi o {nAleatorio}. A soma deles foi {soma} então é IMPAR!')
            print('-=-' * 10)
            if IP == 'I':
                print('Droga você ganhou de mim :/. Vamos tentar dnv...')
                print('-=-' * 10)
                nAleatorio = random.randint(0, 100)
                count += 1
                n = int(input('Qual número você quer chutar? '))
                IP = str(input('Impar ou Par?? [I/P] ')).strip().upper()
                print('-=-' * 10)
            else:
                print(f'Que pena você PERDEUU! Você ganhou {count}!')
                break

elif resp == 'N':
    print('Tudo bem eu entendo. Volte sempre!')
else:
    print('ERROR X__X. FIM DO PROGRAMA')