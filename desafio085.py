lista = [[],[]]
dados = 0

for i in range(7):
    dados = int(input(f'Digite o {i+1}º número: '))
    if dados % 2 == 0:
        lista[0].append(dados)
    else:
        lista[1].append(dados)

print('-+-'*20)
lista[0].sort()
lista[1].sort()
print(f'Os números pares são: {lista[0]}')
print(f'Os números impares são : {lista[1]}')
