matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor parar [{l},{c}]: '))
print('-+-'*24)
pares = terceira = maior = 0
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^3}]',end='')
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            terceira += matriz[l][c]
        if l == 1:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
    print()
print('-+-' * 24)
print(f'A soma de todos os valores pares foram {pares}')
print(f'A soma de todos os valores da terceira coluna é {terceira}')
print(f'O maior número da segunda linha é o {maior}')