lista = list()
pares = list()
impar = list()
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    resp = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if resp == 'N':
        break
for c in lista:
    if c % 2 == 0:
        pares.append(c)
    else:
        impar.append(c)
pares.sort()
impar.sort()
print('_-_'*20)
print(f'Os valores digitados foram esses: {lista}')
print(f'Os número pares colocados na lista são: {pares}')
print(f'Os números impares colocados na lista são: {impar}')