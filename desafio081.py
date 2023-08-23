lista = list()

while True:
    valor = int(input('Adicione um valor: '))
    lista.append(valor)
    print('Valor foi colocado na lista!')
    resp = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if resp == 'N':
        break

print(f'Nessa lista possuimos {len(lista)} valores')
print(f'Os valores em ordem decrescente são: {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não foi colocado na lista!')
