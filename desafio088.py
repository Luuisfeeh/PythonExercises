from random import randint
from time import sleep
print('-=-'*12)
print('          JOGO DA CENA          ')
print('-=-'*12)
lista = list()
jogos = list()
resp = int(input('Quantos jogos você deseja fazer? '))
jogo = 0
print('-+'*4,'GERANDO SEUS JOGOS','-+'*4)
sleep(2)
for j in range(resp):
    for n in range(6):
        jogo = randint(1,60)
        if jogo in lista:
            while jogo in lista:
                jogo = randint(1,60)
        lista.append(jogo)
    lista.sort()
    jogos.append(lista[:])
    lista.clear()

for c, d in enumerate(jogos):
    print(f'JOGO {c+1}: {d}')
    sleep(1)
print('-+'*5,'<BOA SORTE>','-+'*5)
