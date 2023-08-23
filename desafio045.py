import random
import time

print('Suas opções:\n'
      '[ 0 ] PEDRA \n'
      '[ 1 ] PAPEL \n'
      '[ 2 ] TESOURA \n'
      '[ 3 ] SAIR')
escolha = int(input('Qual é a sua jogda? '))
pc = random.randint(0,2)
time.sleep(1.2)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(0.5)
print('PO!!!')


if escolha == 0:
    if pc == 0:
        print('-=' * 12)
        print('Computador jogou PEDRA')
        print('Jogador jogou PEDRA')
        print('-=' * 12)
        print('EMPATE')
    elif pc == 1:
        print('-=' * 12)
        print('Computador jogou PAPEL')
        print('Jogador jogou PEDRA')
        print('-=' * 12)
        print('COMPUTADOR VENCEU')
    elif pc == 2:
        print('-=' * 12)
        print('Computador jogou TESOURA')
        print('Jogador jogou PEDRA')
        print('-=' * 12)
        print('JOGADOR VENCEU')
elif escolha == 1:
     if pc == 0:
         print('-=' * 12)
         print('Computador jogou PEDRA')
         print('Jogador jogou PAPEL')
         print('-=' * 12)
         print('JOGADOR VENCEU')
     elif pc == 1:
         print('-=' * 12)
         print('Computador jogou PAPEL')
         print('Jogador jogou PAPEL')
         print('-=' * 12)
         print('EMPATE')
     elif pc == 2:
         print('-=' * 12)
         print('Computador jogou TESOURA')
         print('Jogador jogou PAPEL')
         print('-=' * 12)
         print('COMPUTADOR GANHOU')
elif escolha == 2:
    if pc == 0:
        print('-=' * 12)
        print('Computador jogou PEDRA')
        print('Jogador jogou TESOURA')
        print('-=' * 12)
        print('COMPUTADOR VENCEU')
    elif pc == 1:
        print('-=' * 12)
        print('Computador jogou PAPEL')
        print('Jogador jogou TESOURA')
        print('-=' * 12)
        print('JOGADOR VENCEU')
    elif pc == 2:
        print('-=' * 12)
        print('Computador jogou TESOURA')
        print('Jogador jogou TESOURA')
        print('-=' * 12)
        print('EMPATE')
elif escolha == 3:
    print('VOCÊ SAIU DO JOGO ;(')
else:
    print('OPÇÂO INVÀLIDA!!')