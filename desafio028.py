from random import randint

print('-+-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-+-' * 20)

numero = randint(0,5) #Blibioteca utilizando para randomizar X coisas
n = int(input('Em que número eu pensei? ')) #Tentativa do jogador
print('Processando...')
if n == numero :
    print('Parabéns, você adivinhou meu número!!')
else:
    print('Essa não, o número que eu pensei era {}'.format(numero))
print('Obrigado por participar!')