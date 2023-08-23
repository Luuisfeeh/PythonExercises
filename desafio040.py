n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))
n4 = float(input('Digite sua quarta nota: '))
media = (n1 + n2 + n3 + n4 ) / 4
print('Sua nota foi {:.1f}'.format(media))

if media < 5:
    print('Infelizmente você foi REPROVADO.')
elif 7 > media >= 5:
    print('Você ainda tem uma chance, está de RECUPERAÇÃO!')
elif media >= 7:
    print('Muito bom, você foi APROVADO!')
