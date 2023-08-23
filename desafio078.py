lista = []
maior = menor = 0
for c in range(0,5):
    lista.append(int(input(f'Digite o valor para posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print('++'*25)
print(f'O maior número digitado foi {maior} na posição ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f'{i}...',end='')
print()
print(f'O menor número digitado foi {menor} na posição ',end='')
for i,v in enumerate(lista):
    if v == menor:
        print(f'{i}...',end='')
print()
