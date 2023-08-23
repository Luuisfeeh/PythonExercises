soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Digite o {}° número: '.format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n
print('A soma dos {} números pares digitados é {}'.format(cont, soma))