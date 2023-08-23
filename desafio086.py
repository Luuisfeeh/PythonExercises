matriz = list()
dados = [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
for i in dados:
    resp = int(input(f'Digite um valor para {i}: '))
    matriz.append(resp)
count = 0
print('-=-'*24)
for c in matriz:
    if count <= 2:
        print(f'[{c:3}]',end='')
    elif count <= 5:
        if count == 3:
            print('')
        print(f'[{c:3}]', end='')
    elif count > 5:
        if count == 6:
            print('')
        print(f'[{c:3}]', end='')
    count += 1
    