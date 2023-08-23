lista = (int(input('Digite um valor: ')),int(input('Digite outro valor: ')),int(input('Digite qualquer valor: ')),int(input('Digite mais um valor: ')))
pares = 0
print("____"*10)
print(f'Você digitou esses valores: {lista}')
print(f'O valor 5 apareceu {lista.count(5)}')
if 2 in lista:
    print(f'O valor 2 está na posição {lista.index(2)+1}')
else:
    print('O valor 2 não foi digitado!')
for c in lista:
    if c % 2 == 0:
        pares += 1
print(f'Nessa lista foi digitado {pares} números pares')