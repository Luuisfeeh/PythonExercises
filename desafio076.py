produtos = ('Teclado', 150, 'Mouse', 122, 'Headset', 210,'Monitor', 1670, 'Microfone', 230, 'SounBar', 565 )
print('_'*40)
print(f'{"Listagem de Preços":^40}')
print('_'*40)
for c in range(0, len(produtos)):
    if c % 2 == 0:
        print(f'{produtos[c]:.<30}', end='')
    else:
        print(f'R${produtos[c]:>5.2f}')
print('_'*40)