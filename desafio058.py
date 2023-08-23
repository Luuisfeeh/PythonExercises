from random import randint

print('Sou seu computador...')
print('Vou pensar em um número entre 0 e 10. \n Tente adivinhar...')
numero = randint(0,10) #Blibioteca utilizando para randomizar X coisas
n = int(input('Em que número eu pensei? ')) #Tentativa do jogador
palpites = 0
while n != numero:
    palpites += 1
    if n > numero:
        print('Um pouco MENOS... Tente de novo.')
        n = int(input('Em que número eu pensei? '))
    else:
        print('Um pouco MAIS... Tente de novo.')
        n = int(input('Em que número eu pensei?'))

print('Acertouu!! Com apenas {} tentativas, meus parabéns.'.format(palpites))