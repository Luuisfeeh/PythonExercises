from random import randint
import time

def sorteio(lista):
    print('Sorteando 5 valores da lista: ',end='')
    for c in range(5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n} ',end='',flush=True)
        time.sleep(0.25)
    print('PRONTO!!')

def somaPar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'A soma dos valores pares em {lista}, é igual à {soma}')



l = list()
sorteio(l)
somaPar(l)