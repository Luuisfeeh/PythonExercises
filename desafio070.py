print('--'*16)
print(' Loja SUPER Baratão')
print('--'*16)

total = caro = barato = cont = 0

nominho = " "
while True:
    nome = str(input('Qual produto você comprou? ')).strip()
    valor = float(input('O valor desse produto? R$'))
    total += valor
    cont += 1
    if cont == 1 or valor < barato:
        barato = valor
        nominho = nome
    if valor >= 1000:
        caro += 1
    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Deseja colocar mais um produto no carrinho? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O valor total da sua compra foi {total:.2f}')
print(f'Em suas compras, {caro} foram acima de R$1000,00')
print(f'{nominho} foi o produto mais barato, custando apenas R${barato:.2f}')