resp = media = soma = count = 0
maior = menor = 0
while resp != 'N':
    n1 = int(input('Digite um número: '))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    soma += n1
    count += 1
    if maior <= n1:
        maior = n1
    else:
        menor = n1
    if resp != 'S' or 'N':
        print('Mensagem inválida. X__X')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
media = soma/count
print('Você digitou {} número e a média foi {:.2f}'.format(count,media))
print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))