n1 = int(input('Digite um número para converter: '))
binario = bin(n1)
octal = oct(n1)
hexadecimal = hex(n1)

print('[1] Para Binário \n[2] Para Octal \n[3] Para Hexadecimal')
escolha = int(input('Escolha uma opção: '))

if escolha == 1:
    print('O número {} em binário é igual {}'.format(n1,binario[2::]))
elif escolha == 2 :
    print('O número {} em Octal é igual {}'.format(n1, octal[2::]))
elif escolha == 3:
    print('O número {} em Hexadecimal é igual {}'.format(n1,hexadecimal[2::]))
else:
    print('Escolha um número certo!!')