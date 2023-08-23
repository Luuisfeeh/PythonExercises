lista = []
resp = cont = 0

while True:
    valor = int(input('Digite um número para ser adicionado : '))

    if valor not in lista:
        lista.append(valor)
        print('Adicionando valor..')
    else:
        print('Valor já existe na lista, não foi adicionado!!')

    resp = str(input('Deseja adicionar mais um número?[S/N] ')).strip().upper()
    if resp == 'N':
        break


print('__'*16)
print('Valores que foram adicionados: ')
for c in sorted(lista):
    print(c, end='->')
