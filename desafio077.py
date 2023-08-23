lista = ('CASA','VIOLAO','PORTA','GARRAFA','GRAVIOLA','ESTRUTURA','CELULAR','ALIANÇA','PERNA','BOLA','TRANSPORTE','JOGO','GOIABA')
for c in lista:
    print(f'\nNa palavra {c} tem essas vogais ', end='')
    for letra in c:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
